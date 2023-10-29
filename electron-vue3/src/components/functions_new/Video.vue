<template>
  <div class="video">
    <div class="leftbar">
      <div class="titlewords">视频素材</div>
      <div class="file-list-uploading">
        <el-upload
          class="upload-picture"
          action="http://www.fuqianshi.cn:8001/file/upload"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :before-remove="beforeRemove"
          :on-success="handleSuccess"
          :limit="9"
          multiple
          :on-exceed="handleExceed"
          :file-list="fileList"
          list-type="picture"
        >
          <el-button size="small" type="primary">点击上传</el-button>
        </el-upload>
      </div>
      <el-button size="small" type="primary" class="select">选中确认</el-button>
    </div>
    <div class="rightbar">
      <div class="rightbar_up">
        <div class="rightbar_up_left">
          <div>
            <div v-if="playerOptions.sources[0].src !== 'null'">
              <videoPlayer
                class="video-player vjs-custom-skin"
                ref="videoPlayer"
                :playsinline="true"
                :options="playerOptions"
              >
              </videoPlayer>
            </div>
          </div>
          <el-button size="small" type="primary" class="output"
            @click="exportVideo">视频导出</el-button
          >
        </div>
        <div class="rightbar_up_right">
          <div class="titlewords">视频情绪值</div>
          <div class="tents">{{ emo.emoValue }}</div>
          <div class="titlewords">音乐情绪值</div>
          <div class="tents">{{ emo.musicEmo }}</div>
          <div class="titlewords">匹配损失</div>
          <div class="tents">{{ emo.musicEmoDis }}</div>
        </div>
      </div>
      <div class="rightbar_down">
        <div
          class="musicblock"
          v-for="(item, index) in musicList"
          :key="index + 2"
        >
          <div class="music_title">{{ item.title }}</div>
          <div class="music_author">{{ item.artist }}</div>
          <audio ref="audio" :src="item.url" controls="controls" @play="play(item)"></audio>

          <div class="music_loss">
            匹配误差：{{ item.dis.toString().slice(0, 6) }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
//引入视频播放组件
import "video.js/dist/video-js.css";
import { videoPlayer } from "vue-video-player";
const service = axios.create({
  // axios中请求配置有baseURL选项，表示请求URL公共部分
  baseURL: "http://tim-wcx.ltd:5000",
});
export default {
  components: {
    videoPlayer,
  },
  data() {
    return {
      fileList: [],
      imgShow: "",
      currentSrc: "",
      nextSong: "",
      musicList: [],
      emo: {
        emoValue: "请选择图片",
        musicEmo: "请选择音乐",
        musicEmoDis: "请选择音乐"
      },

      processedVideoPath: '',  //处理好的视频地址，仅用来后端传参
      musicUrl: '',   //当前选择的音乐地址
      playerOptions: {
        autoplay: false, //如果true,浏览器准备好时开始回放。
        muted: false, // 是否静音。
        loop: false, // 是否循环播放。
        preload: "false", // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
        language: "zh-CN",
        aspectRatio: "16:9", // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
        fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
        sources: [
          {
            type: "video/mp4", //mp4格式视频,若为m3u8格式，type需设置为 application/x-mpegURL
            src: "null", //url地址
          },
        ],
        notSupportedMessage: "此视频暂无法播放，请稍后再试", //允许覆盖Video.js无法播放媒体源时显示的默认信息。
        controlBar: {
          timeDivider: true,
          durationDisplay: true,
          remainingTimeDisplay: false,
          fullscreenToggle: true, //是否显示全屏按钮
        },
      },
    };
  },
  methods: {
    handleRemove(file, fileList) {
      this.$axios({
        method: "POST",
        url: "api/delete",
        params: {
          fileName: file.qnName,
        },
      });
    },
    handlePreview(file, fileList) {
      console.log("选择了文件");
      //console.log(file, fileList)
      let message = this.$message({
        message: '正在智能分析中，视频分析花费时间较长，大约需要十秒，请稍等；请确认图片右上角均已出现绿色勾号后再点击分析！',
        type: "info",
        duration: 0
      });
      this.playerOptions.sources[0].src = file.url;
      service({
        method: "GET",
        url: "matchMusicForVideo",
        params: {
          videoUrl: "http://" + file.videoUrl,
        },
      }).then((res) => {
        message.close()
        console.log(res.data)
        this.$message({
          message: '匹配成功！注意：点击“视频导出”前请确认已播放选中的配乐，否则导出不成功',
          type: "success",
        });
        this.emo.emoValue = res.data.emoValue.toString().slice(0,6)
        this.musicList = res.data.musicList
        this.processedVideoPath = res.data.processedVideoPath
      });
    },
    handleExceed(files, fileList) {
      this.$message.warning(
        `当前限制选择 9 个文件，本次选择了 ${files.length} 个文件，共选择了 ${
          files.length + fileList.length
        } 个文件`
      );
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`确定移除 ${file.name}？`);
    },
    handleSuccess(response, file, fileList) {
      //上传图片后将云服务器中的图片信息存到list
      let url = response.data.imgUrl;
      let name = response.data.qnName;
      let obj = fileList[fileList.length - 1];
      obj["qnName"] = name;
      obj["videoUrl"] = url;
      fileList[fileList.length - 1] = obj;
    },

    play(item){
      this.emo.musicEmo = item.value.toString().slice(0,6)
      this.emo.musicEmoDis = item.dis.toString().slice(0,6)
      this.musicUrl = item.url
    },
    exportVideo(){
      let message = this.$message({
        message: '正在合成视频与背景音乐,合成时间较长，大约需要30秒，请耐心等待；若失败，请检查您是否播放配乐后再导出',
        type: 'info',
        duration: 0
      })
      service({
        method: 'get',
        headers: {
          "content-type": "application/json", // 默认值
          Authorization: "Bearer " + sessionStorage.getItem("access_token"),
        },
        url: 'exportVideo',
        params: {
          processedVideoPath: this.processedVideoPath,
          musicUrl: this.musicUrl
        },
        responseType: 'arraybuffer',
      }).then(res => {
        const blob = new Blob([res.data])
        const link = document.createElement('a')
        link.download = "output.mp4" // a标签添加属性
        link.style.display = 'none'
        link.href = URL.createObjectURL(blob)
        document.body.appendChild(link)
        link.click() // 执行下载
        URL.revokeObjectURL(link.href)  // 释放 bolb 对象
        document.body.removeChild(link) // 下载完成移除元素
        message.close()
        this.$message({
          message: '导出成功！',
          type: 'success'
        })
      })

    }
  },
};
</script>


<style>
img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}
.titlewords {
  height: 1.5rem;
  width: 100%;
  /* padding: 0.2rem 1.5rem; */
  text-align: center;
  color: #1b2767;
  border-bottom: solid 0.01rem #dce3eb;
  font-size: 1rem;
  font-weight: 900;
  font-family: YaHei;
  display: flex;
  align-items: center;
  justify-content: center;
}
.tents {
  margin: 0 1rem 1rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: Lucida Handwriting;
  color: #797c8c;
  line-height: 1.8rem;
  font-size: 1.2rem;
  overflow: scroll;
}
.music_title {
  margin: 0 1rem 0rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: YaHei;
  color: #1b2767;
  line-height: 1.8rem;
  font-size: 1.2rem;
  overflow: scroll;
  border-bottom: solid 0.01rem #dce3eb;
}
.music_author {
  margin: 0 1rem 1rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: YaHei;
  color: #1b2767aa;
  line-height: 1rem;
  font-size: 1rem;
  overflow: scroll;
}
.music_loss {
  margin: 1rem 1rem 1rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: yahei;
  color: #1b2767aa;
  line-height: 1rem;
  font-size: 1rem;
  overflow: scroll;
}
.video {
  margin: 4% 1% 1% 4.5%;
  width: 94%;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
.leftbar {
  position: relative;
  z-index: 2;
  width: 21%;
  height: 96%;
  padding: 1%;
  background: #fffe;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
.file-list-uploading {
  margin: 2% 0 0 0;
  overflow: scroll;
  height: 85%;
}
.el-button {
  background: #1b2767;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  color: #fff;
  border: 0;
  border-radius: 0;
  width: 10rem;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
.el-upload {
  width: 18rem;
}
.select {
  z-index: 5;
  position: absolute;
  bottom: 0%;
  border-radius: 2rem 2rem 0 0rem;
  width: 10rem;
}
.rightbar {
  z-index: 3;
  width: 76%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}
.rightbar_up {
  height: 68%;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
.rightbar_up_left {
  position: relative;
  z-index: 5;
  height: 100%;
  width: 77.5%;
  background: #fffe;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
.output {
  position: absolute;
  bottom: 0%;
  right: 0%;
  border-radius: 1rem 0rem 0 0rem;
  width: 10rem;
}
.rightbar_up_right {
  height: 91%;
  width: 17%;
  background: #fffe;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);

  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
  padding: 2%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}
.rightbar_down {
  height: 30%;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  overflow: scroll;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
.musicblock {
  z-index: 6;
  height: 90%;
  width: 30.3%;
  padding: 1%;
  margin: 0 1.5% 0 0;
  background: #fffe;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  transition: all 200ms ease-in-out;
}
.musicblock:hover {
  padding: 1% 5%;
}
</style>
