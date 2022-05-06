import cv2
import os
import time

# 视频路径
video_path = r'C:/Users/26390/Desktop/DC/大创视频/'
# 保存图片的路径
saved_path = r'C:/Users/26390/Desktop/DC/pictures/'
video_list = os.listdir(video_path)   # 视频列表
count = 3  # 截取视频帧的时间间隔（这里是每隔3秒截取一帧）
i = 0   # 遍历所有视频的所有的帧，用于找出符合条件的帧
j = 0  # 图片序号
for index, video_name in enumerate(video_list):
    # 开始读视频
    video_path_ = os.path.join(video_path, video_name)
    videoCapture = cv2.VideoCapture(video_path_)
    print("正在处理第{}个视频，总共{}个视频".format(index + 1, len(video_list)))
    while True:
        success, frame = videoCapture.read()
        FPS = videoCapture.get(5)
        if success:
            frameRate = int(FPS) * count  # 计算count秒会有多少帧，设定固定帧数
            # 保存图片
            if (i % frameRate == 0):
                saved_name = str(j) + '.jpg'
                cv2.imwrite(os.path.join(saved_path, saved_name), frame)  # 保存符合条件的帧图（frame）
                print('image of %s is saved' % saved_name)
                j += 1
            i += 1
            cv2.waitKey(0)
        else:
            print('video is all read')
            break
    videoCapture.release()
    time.sleep(5)
