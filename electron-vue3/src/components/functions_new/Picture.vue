<template>
  <div class="picture">
    <div class="leftbar">
      <div class="titlewords">项目素材</div>
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
    </div>
    <div class="rightbar">
      <div class="rightbar_up">
        <div class="rightbar_up_left">
          <div v-if="imgShow !== 'null'" class="rightbar_up_left_img">
            <img
              :src="imgShow"
              style="position: relative; width: 100%; height: 100%"
            />
          </div>
        </div>
        <div class="rightbar_up_right">
          <div class="titlewords">图片情绪值</div>
          <div class="tents">{{ emo.emoValue }}</div>
          <div class="titlewords">音乐情绪值</div>
          <div class="tents">{{emo.musicEmo}}</div>
          <div class="titlewords">匹配损失</div>
          <div class="tents">{{emo.musicEmoDis}}</div>
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
// 创建axios实例（访问flask服务器）
import axios from "axios";
import {Message} from "element-ui";

const service = axios.create({
  // axios中请求配置有baseURL选项，表示请求URL公共部分
  baseURL: "http://tim-wcx.ltd:5000",
  // 超时
  timeout: 10000,
});
export default {
  data() {
    return {
      fileList: [],
      imgShow: "null",
      currentSrc: "",
      emo: {
        emoValue: "请选择图片",
        musicEmo: "请选择音乐",
        musicEmoDis: "请选择音乐"
      },
      musicList: [],
    };
  },
  methods: {
    handleRemove(file, fileList) {
      this.$axios({
        method: "POST",
        url: "file/delete",
        params: {
          fileName: file.qnName,
        },
      });
    },
    handlePreview(file, fileList) {
      let message = this.$message({
        message: '正在智能分析中，请确认图片右上角均已出现绿色勾号后再点击分析！',
        type: "info",
        duration: 0
      });
      console.log("选择了文件");
      //console.log(file, fileList)
      this.imgShow = file.url;
      service({
        method: "GET",
        url: "singleImgEmo",
        params: {
          imgUrl: "http://" + file.imgUrl,
        },
      }).then((res) => {
        //console.log(res.data)
        this.emo.emoValue = res.data.emoValue.toString().slice(0,6)
        this.musicList = res.data.musicList
        message.close()
        this.$message({
          message: '匹配成功！注意：点击“视频导出”前请确认已播放选中的配乐，否则导出不成功',
          type: "success",
        });
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
      //上传图片后将response中的图片信息存到list
      fileList.forEach((item) => {
        let url = item.response.data.imgUrl;
        let name = item.response.data.qnName;
        let obj = item;
        obj["qnName"] = name;
        obj["imgUrl"] = url;
        item = obj;
      });
    },

    play(item){
      this.emo.musicEmo = item.value.toString().slice(0,6)
      this.emo.musicEmoDis = item.dis.toString().slice(0,6)
    }

  },
};
</script>


<style>
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
.picture {
  margin: 4% 1% 1% 4.5%;
  width: 94%;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
.leftbar {
  z-index: 2;
  width: 21%;
  height: 96%;
  padding: 1%;
  background: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  display: flex;
  flex-direction: column;
  /* align-items: space-between;
  justify-content: space-between;*/
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
.file-list-uploading{
  height: 85%;
  overflow: scroll;
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
  height: 100%;
  width: 77.5%;
  background: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
.rightbar_up_left_img {
  height: 100%;
  width: 100%;
  background-color: #000;
  overflow: scroll;
}
.rightbar_up_left_img img {
  position: relative;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.rightbar_up_right {
  height: 91%;
  width: 17%;
  background: #fff;
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
  height: 90%;
  width: 30.3%;
  padding: 1%;
  margin: 0 1.5% 0 0;
  background: #fff;
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
