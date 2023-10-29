#coding=utf-8




import os
import json
import pandas as pd
import torch
from PIL import Image
from torchvision import transforms
import cv2
from shutil import copyfile
from pydub import AudioSegment
import ffmpeg
import shutil

from model import resnet34

def add(a,b):
    return (a+b)

MAXSECOND = 15.0    # 最长视频秒数
TEMPDIR = "./temp/" # 临时缓存文件夹地址


# 预测视频情绪值
# 输入图片url
# 输出情绪类型和情绪值
def predict(img_url):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")     # 假如能用gpu就用0号gpu，没有就用cpu

    # 图像预处理：缩放，切割等
    data_transform = transforms.Compose(
        [transforms.Resize(256),
         transforms.CenterCrop(224),
         transforms.ToTensor(),
         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    # load image
    cap = cv2.VideoCapture(img_url)
    if (cap.isOpened()):
        ret, img = cap.read()
        img = Image.fromarray(img)
    # [N, C, H, W]
    img = data_transform(img)
    # expand batch dimension
    img = torch.unsqueeze(img, dim=0)

    # create model
    model = resnet34(num_classes=2).to(device)

    # load model weights
    weights_path = "./resNet34.pth"
    assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
    model.load_state_dict(torch.load(weights_path, map_location=device))

    # prediction
    model.eval()
    # 不对损失梯度进行跟踪
    with torch.no_grad():
        # predict class
        # 压缩batch维度
        output = torch.squeeze(model(img.to(device))).cpu()
        # 用softmax处理得到概率分布
        predict = torch.softmax(output, dim=0)
        # 用argmax得到最大值索引
        predict_cla = torch.argmax(predict).numpy()

    # 输出情绪值
    emoValue = float(predict[0].numpy())

    # 输出分类结果
    json_path = './class_indices.json'
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)
    with open(json_path, "r") as f:
        class_indict = json.load(f)
    emoType = class_indict[str(predict_cla)]

    return emoType, emoValue


# 前端需要控制一下输入的n不能超过120
# 根据情绪值匹配n个音乐
# 返回匹配的音乐列表
def musicMatch(n, emo):
    # 创建导出的列表
    musicList = []
    # 导入音乐库
    musicDB = pd.read_excel("./musicValue.xlsx")
    # 匹配
    for i, line in musicDB.iterrows():
        emoDis = abs(emo - line["value"])
        if len(musicList) < n:
            musicList.append([line["music"], line["value"], emoDis])
        else:
            musicList.sort(key=lambda li: li[2])
            if emoDis < musicList[n - 1][2]:
                musicList[n - 1][0] = line["music"]
                musicList[n - 1][1] = line["value"]
                musicList[n - 1][2] = emoDis
            else:
                break

    return musicList

# 导入视频并处理（裁剪至15秒内，并将视频存到temp里）
# 输入视频的url
# 返回视频是否超过xx秒（超过1，不超过0），处理好后的视频地址
def getVideo(video_url):
    video_url = getUrl(video_url)
    cap = cv2.VideoCapture(video_url)  # 打开视频文件
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 获得视频文件的帧宽
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 获得视频文件的帧高
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 获得视频文件的帧数
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # 获得视频文件的帧率
    video_length = frames / fps  # 计算视频长度/s

    # 创建存放处理后的视频的路径
    processed_video_path = os.path.join(TEMPDIR, "video.mp4")
    if not os.path.isdir(TEMPDIR):
        os.mkdir(TEMPDIR)

    if video_length > MAXSECOND:    # 如果原视频长度大于xx秒就裁剪
        flag = 1
        # 创建保存视频文件类对象
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(processed_video_path, fourcc, fps, (int(width), int(height)))

        # 设置帧读取的开始位置
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        pos = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 获得帧位置
        while pos <= MAXSECOND * fps:
            ret, frame = cap.read()  # 捕获一帧图像
            out.write(frame)  # 保存帧
            pos = cap.get(cv2.CAP_PROP_POS_FRAMES)

        out.release()
    else:                           # 如果原视频小于xx秒就直接复制一份到temp
        flag = 0
        copyfile(video_url, processed_video_path)  # 拷贝原视频到temp文件夹

    cap.release()
    return flag, processed_video_path

# 处理目标音乐
# 输入是音乐地址，处理好的视频地址（用于获取视频长度）
# 输出是处理好的音乐地址
def getMusic(music_path, video_path):
    # 读取音频文件
    wav = AudioSegment.from_wav(music_path)

    # 得到视频长度
    cap = cv2.VideoCapture(video_path)  # 打开视频文件
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 获得视频文件的帧数
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # 获得视频文件的帧率
    video_length = frames / fps  # 计算视频长度/s

    # 读取前xx秒的音频并保存在music.wav中
    processed_music_path = os.path.join(TEMPDIR, "music.wav")
    if not os.path.isdir(TEMPDIR):
        os.mkdir(TEMPDIR)
    wav[:video_length * 1000].export(processed_music_path, format="wav")

    return processed_music_path

# 拼接音乐和视频
# 输入是处理好的音乐和视频地址
# 输出是合并后的视频地址
def concatMV(music_path, video_path):
    video = ffmpeg.input(video_path)
    music = ffmpeg.input(music_path)

    output_path = os.path.join(TEMPDIR, "output.mp4")
    ffmpeg.concat(video, music, v=1, a=1).output(output_path).run()

    return output_path

# 对视频进行截图，截好的图片用于情绪分析
# 输入是处理好的视频地址
# 输入是存放截图的文件夹
def getEmoFrames(video_path):
    cap = cv2.VideoCapture(video_path)  # 打开视频文件
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 获得视频文件的帧数
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # 获得视频文件的帧率
    video_length = frames / fps  # 计算视频长度/s

    # 创建存放截图的文件夹
    cutimg_dir = os.path.join(TEMPDIR, "./cut/")
    if not os.path.isdir(cutimg_dir):
        os.mkdir(cutimg_dir)

    # 获取截图
    for t in range(int(video_length)):
        cap.set(cv2.CAP_PROP_POS_FRAMES, t * fps)
        ret, frame = cap.read()
        cutimg_path = os.path.join(cutimg_dir, "img_{}.jpg".format(t))
        cv2.imwrite(cutimg_path, frame)
    cap.release()

    # 将封面复制到temp
    cover_path = os.path.join(TEMPDIR, "cover.jpg")
    copyfile(os.path.join(cutimg_dir, "img_0.jpg"), cover_path)

    return cutimg_dir

# 计算视频的情绪值
# 输入是处理好的视频地址
# 输出是视频的情绪类型和情绪值
def videoEmo(video_path):
    frames_path = getEmoFrames(video_path)
    frame_list = os.listdir(frames_path)
    emo_list = []

    # 逐个截图判断其情绪值并存入emo_list
    for frame in frame_list:
        img_path = os.path.join(frames_path, frame)
        emo_list.append(predict(img_path))

    min_mean_dis = 2.0  # 情绪值之间的距离不会超过1

    # 计算每帧与其他帧情绪值的距离，选取离其他帧平均距离最小的帧的情绪值作为视频情绪值
    for i in range(len(emo_list)):
        mean_dis = 0.0
        for j in range(len(emo_list)):
            if i == j:
                continue
            mean_dis += (emo_list[i][1]-emo_list[j][1]) ** 2
        mean_dis = mean_dis/(len(emo_list)-1)
        if mean_dis < min_mean_dis:
            emo = emo_list[i]
            min_mean_dis = mean_dis

    emo_type = emo[0]
    emo_value = emo[1]

    return emo_type, emo_value

# 计算单张图片的情绪值
# 输入是单张图片的地址
# 输出是图片的情绪类型和情绪值
def singleImgEmo(img_url):
    emo_type, emo_value = predict(getUrl(img_url))
    return emo_type, emo_value

# 给url加前缀
def getUrl(url):
    return "http://" + url

# 清空temp文件夹
def clear_temp():
    if os.path.isdir(TEMPDIR):
        shutil.rmtree(TEMPDIR)


if __name__ == '__main__':
    # 图片配乐
    img_url = "rialb9qcc.hd-bkt.clouddn.com/299KAfqLUpoQG2NE.png"    # 输入图片url
    type, emo = singleImgEmo(img_url)
    print(type)
    print(emo)
    n = 3
    music = musicMatch(n, emo)
    print(music)

    # # 视频配乐
    # video_url = "rialb9qcc.hd-bkt.clouddn.com/vsavejCL29tqWMHKOQ.mp4"
    # flag, processed_video_path = getVideo(video_url)
    # if flag == 1:
    #     print("视频长度大于15秒！")
    #
    # type, emo = videoEmo(processed_video_path)
    # print(type)
    # print(emo)
    # cover_path = os.path.join(TEMPDIR, "cover.jpg")
    #
    # n = 3
    # music = musicMatch(n, emo)
    # print(music)
    #
    # music_path = os.path.join("./music database/", music[0][0]+".wav")
    # processed_music_path = getMusic(music_path, processed_video_path)
    # concatMV(processed_music_path, processed_video_path)

    # # 清除temp文件夹
    # clear_temp()


