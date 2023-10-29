<template>
    <div class="yanshi">
        <div class="yanshi_leftbar">
            <div class="yanshi_leftbar_up">
                <div v-if="page1" class="yanshi_video">
                    <videoPlayer
                            class="video-player vjs-custom-skin"
                            ref="videoPlayer"
                            :playsinline="true"
                            :options="playerOptions1"
                    >
                    </videoPlayer>
                </div>
                <div v-if="page2" class="yanshi_video">
                    <videoPlayer
                            class="video-player vjs-custom-skin"
                            ref="videoPlayer"
                            :playsinline="true"
                            :options="playerOptions2"
                    >
                    </videoPlayer>
                </div>
            </div>
            <div class="yanshi_leftbar_down">
                <div class="titlewords">联系方式：</div>
                <div class="yanshi_tents_down">
                    <div class="yanshi_tents_down_message">
                        负责人范同学：
                    </div>
                    <div class="yanshi_tents_down_message">
                        电话：17864233873、18781361821
                    </div>
                    <div class="yanshi_tents_down_message">
                        微信：QX3343790025
                    </div>
                    <div class="yanshi_tents_down_message">
                        QQ:  1485411976
                    </div>
                </div>
            </div>
        </div>
        <div class="yanshi_rightbar">
            <div class="titlewords">欢迎使用《大音希声》&《再过故人庄》</div>
            <div class="yanshi_tents">
                左侧为本项目五分钟演示视频。点击播放后，视频右下方有全屏按钮，欢迎观看。
            </div>
            <div class="titlewords">关于《大音希声》：</div>
            <div class="yanshi_tents">
                <p>
                    《大音希声》配乐及视频合成平台为本网页，左侧功能栏有“乡旅热门”、“照片配乐”、“视频配乐”、”多图生成“等功能，欢迎使用体验。
                </p>
                <p>
                    如对使用方法有所疑惑请查看左侧演示视频，使用过程中遇到困难请联系负责人范同学。
                </p>
            </div>
            <div class="titlewords">关于《再过故人庄》：</div>
            <img src="../../assets/video/小程序二维码.jpg" style="height: 10rem;width: auto" alt="" class="yanshi_img"/>
            <div class="yanshi_tents">
                <p>
                    《再过故人庄》小程序为乡村旅游动态配乐小程序，当前为测试版，即将上线。请扫描上方二维码申请访问，并备注您的身份。若审核不及时请电话联系负责人范同学。
                </p>
                <p>
                    小程序使用过程中如有遇到问题请查看左侧“小程序介绍”展示视频。
                </p>
            </div>
            <div class="yanshi_pages">
                <button  class="yanshi_page" v-on:click="pageselectpage1">
                    <div v-if="page1" class="yanshi_bofang1">
                        <img src="../../assets/bofang.png" style="height: auto;width: 1rem" alt=""/>
                    </div>
                    演示视频
                </button >
                <button  class="yanshi_page" v-on:click="pageselectpage2">
                    <div v-if="page2" class="yanshi_bofang2">
                        <img src="../../assets/bofang.png" style="height: auto;width: 1rem" alt=""/>
                    </div>
                    小程序介绍
                </button >
            </div>
        </div>
    </div>
</template>

<script>
import { videoPlayer } from 'vue-video-player'
import 'video.js/dist/video-js.css'

export default {
    data() {
        return {
            page1:true,
            page2:false,
            playerOptions1: {
                autoplay: false, //如果true,浏览器准备好时开始回放。
                muted: false, // 是否静音。
                loop: false, // 是否循环播放。
                preload: "false", // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                language: "zh-CN",
                aspectRatio: "1920:1080", // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                sources: [
                    {
                        type: "video/mp4", //mp4格式视频,若为m3u8格式，type需设置为 application/x-mpegURL
                        src: require("../../assets/video/山软视频.mp4"), //url地址
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
            playerOptions2: {
                autoplay: false, //如果true,浏览器准备好时开始回放。
                muted: false, // 是否静音。
                loop: false, // 是否循环播放。
                preload: "false", // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                language: "zh-CN",
                aspectRatio: "1920:1080", // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                sources: [
                    {
                        type: "video/mp4", //mp4格式视频,若为m3u8格式，type需设置为 application/x-mpegURL
                        src: require("../../assets/video/讲解视频.mp4"), //url地址
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
        }
    },
    components: {
        videoPlayer
    },
    methods:{
        pageselectpage1:function () {
            this.page1 = true;
            this.page2 = false;
            console.log(this.page1);
            console.log(this.page2)
        },
        pageselectpage2:function () {
            this.page1 = false;
            this.page2 = true;
            console.log(this.page1);
            console.log(this.page2)
        }
    }
};
</script>


<style>
button{
    border: 0;
}
.yanshi_bofang1{
    position: absolute;
    left: 0.5rem;
    top: 0.4rem;
}
.yanshi_bofang2{
    position: absolute;
    left: 0.5rem;
    top: 3.4rem;
}
.yanshi_pages{
    position: absolute;
    width: 10rem;
    height: 5rem;
    top: 52%;
    left: 0%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
}
.yanshi_page{
    width: 100%;
    padding: 0 0 0 1rem;
    height: 2rem;
    background-color: #1b2767;
    border-radius: 0 1rem 1rem 0;
    color: #fff;
    font-weight: 900;
    font-size: 1.05rem;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
}
.yanshi_page:hover{
    padding: 1rem 0 1rem 1rem;
    background-color: #1b2767aa;
}
.yanshi_img{
    margin: 1rem 0 0 7rem;
    box-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
}
.titlewords {
    height: 1.5rem;
    width: 100%;
    /* padding: 0.2rem 1.5rem; */
    text-align: center;
    color: #1b2767;
    border-bottom: solid 0.01rem #dce3eb;
    font-size: 1.1rem;
    font-weight: 900;
    font-family: YaHei;
    display: flex;
    align-items: center;
    justify-content: center;
}
.yanshi_tents_down_message{
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
}
p{
    margin: 0.5rem 0;
}
.yanshi_tents{
    margin: 0.5rem 0;
    text-indent: 2rem;
    line-height: 1.5rem;
}
.yanshi_tents_down{
    margin: 1rem 0;
    text-indent: 2rem;
    line-height: 1.5rem;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}
.yanshi {
    position: relative;
    margin: 4% 1% 1% 4.5%;
    width: 94%;
    height: 95%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;

    /*overflow: hidden;*/
}
.yanshi_leftbar{
    position: relative;
    height: 43rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
}
.yanshi_leftbar_up{
    position: relative;
    width: 64rem;
    height: 36rem;
    background-color: #fffe;
    overflow: hidden;
    box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
.yanshi_leftbar_down{
    position: relative;
    width: 62rem;
    height: 4rem;
    padding: 1rem;
    background-color: #fffd;
    box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
.yanshi_video{
    height: 100%;
    width: 100%;
}
.yanshi_rightbar{
    position: relative;
    height: 41rem;
    width: 23rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 1rem;
    background-color: #fffd;
    overflow: hidden;
    box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
</style>
