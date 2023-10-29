<template>
  <div class="remen">
    <div class="remen_leftbar">
      <div class="remen_container">
        <div class="box" v-for="item in cards">
          <img :src=item.url />
          <div class="box_title">{{item.box_title}}</div>
          <div class="box_tents">
            {{item.box_tents}}
          </div>
        </div>
      </div>
      <div class="remen_emo"><Emotion></Emotion></div>
    </div>
    <div class="remen_rightbar">
      <div class="remen_song">
        <div class="remen_titlewords">热门配乐</div>
        <div class="remen_song_lists">
          <div class="remen_song_list" v-for="item in items">
            <div class="remen_song_list_rank">
              {{item.remen_song_list_rank}}
            </div>
            <div class="remen_song_list_up">
              <div class="remen_song_list_title">
                {{item.remen_song_list_title}}
              </div>
<!--              <audio ref="audio" src="" controls="controls" style="height: 100%;weight:25%"></audio>-->
            </div>
            <div class="remen_song_list_up">
              <div class="remen_song_list_artist">
                作者：{{item.remen_song_list_artist}}
              </div>
              <div class="remen_song_list_emo">
                情绪值：{{item.remen_song_list_emo}}
              </div>
              <div class="remen_song_list_times">
                被匹配次数：{{item.remen_song_list_times}}
              </div>
            </div>
          </div>
        </div>
      </div>
<!--      <div class="remen_num">15日活跃人数</div>-->
    </div>
  </div>
</template>

<script>
  import Emotion from "./graph/emotion_like.vue";
export default {
  data() {
    return {
      cards: [
        {
          url:require("../../assets/picture4remen/card_1.jpg"),
          box_title:'杨家山里的月季花谷你去过吗',
          box_tents:'在杨家山里藏着一个世外桃源，漫山遍野的月季花含苞待放，适合御剑飞行，适合拍照，适合约会，还能遛娃，还能樱桃采摘！',
        },
        {
          url:require("../../assets/picture4remen/card_2.jpg"),
          box_title:'青山渔村-牌坊好美',
          box_tents:'整个渔村红瓦黄墙，层叠错落，拍照绝绝子，非常出片。不仅有美景，海边晓饭馆也值得推荐哦。',
        },
        {
          url:require("../../assets/picture4remen/card_3.jpg"),
          box_title:'亲子游玩好去处 二月二农场',
          box_tents:'可以自己做豆腐，做海凉粉等，还有小红军乐园可以畅玩一整天，一起来二月二农场亲近小动物体验乡村生活吧！',
        },
        {
          url:require("../../assets/picture4remen/card_4.jpg"),
          box_title:'青岛海神庙露营打卡，面朝大海春暖花开',
          box_tents:'海与浪，温与柔，爱与不爱，皆自由。这个夏天，来海神庙看海吧！',
        },
        {
          url:require("../../assets/picture4remen/card_5.jpg"),
          box_title:'沿着海边一路向北',
          box_tents:'走在沿海公路，吹着海风，感受一丝喧嚣外的宁静',
        },
      ],
      items: [
        {
          remen_song_list_rank:'1',
          remen_song_list_title:'how it feels to love you',
          remen_song_list_artist:'aimless',
          remen_song_list_emo:'0.349742',
          remen_song_list_times:'16'
        },
        {
          remen_song_list_rank:'2',
          remen_song_list_title:'夜空下的幻想',
          remen_song_list_artist:'余日秋山',
          remen_song_list_emo:'0.233506',
          remen_song_list_times:'13'
        },
        {
          remen_song_list_rank:'3',
          remen_song_list_title:'Children`s Introduction',
          remen_song_list_artist:'西原健一郎',
          remen_song_list_emo:'0.999998',
          remen_song_list_times:'11'
        },
        {
          remen_song_list_rank:'4',
          remen_song_list_title:'Normand Corbeil - 暴雨',
          remen_song_list_artist:'三亩地',
          remen_song_list_emo:'0.989386',
          remen_song_list_times:'9'
        },
        {
          remen_song_list_rank:'5',
          remen_song_list_title:'Lost In Your Eyes (ft Per Rinaldo)',
          remen_song_list_artist:'Timecop1983',
          remen_song_list_emo:'0.128668',
          remen_song_list_times:'7'
        },
        {
          remen_song_list_rank:'6',
          remen_song_list_title:'ワールド・ワイド・ボクシステム',
          remen_song_list_artist:'Annabel',
          remen_song_list_emo:'0.595077',
          remen_song_list_times:'5'
        },
        {
          remen_song_list_rank:'7',
          remen_song_list_title:'Five O\' Clock',
          remen_song_list_artist:'Away the ways',
          remen_song_list_emo:'0.981233',
          remen_song_list_times:'3'
        },
        {
          remen_song_list_rank:'8',
          remen_song_list_title:'So In Love (Original Mix)',
          remen_song_list_artist:'Brock Berrigan',
          remen_song_list_emo:'0.832692',
          remen_song_list_times:'2'
        },
      ]
    }
  },
  components: {
    Emotion,
  },
};
</script>


<style>
.remen_titlewords {
  height: 8%;
  width: 100%;
  /* padding: 0.2rem 1.5rem; */
  text-align: center;
  color: #fff;
  /*border-bottom: solid 0.01rem #dce3eb;*/
  font-size: 1rem;
  font-weight: 900;
  font-family: YaHei;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #1b2767;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
  margin:0 0 2% 0;
}

.remen {
  margin: 3% 1% 0.5% 4%;
  width: 94%;
  height: 90%;
  display: flex;
  flex-direction: row;
  align-items: space-between;
  justify-content: space-between;
}
.remen_leftbar {
  position: relative;
  width: 62%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}
.remen_container {
  position: relative;
  height: 56%;
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  /* padding: 1%; */
  /* background: #fffe; */
  /* overflow: hidden; */
  margin-bottom: 2%;
}
.box {
  flex: 1;
  overflow: hidden;
  height: 100%;
  width: 100%;
  transition: all 0.5s;
  margin: 0 1% 0 0;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
  /*border-radius: 2%;*/
  border: 2px solid #fffc;
  background-color: #fffc;
}
.box:nth-last-child(1) {
  flex: 1;
  overflow: hidden;
  height: 100%;
  transition: all 0.5s;
  margin: 0;
}
.box > img {
  height: 85%;
  object-fit: cover;
  transition: all 0.5s;
}
.box_tents {
  display: none;
  padding: 2%;
}
.box_title {
  margin-bottom: 2%;
  width: 100%;
  overflow: hidden;
}
.box:hover .box_title {
  width: 200%;
}
.box:hover {
  flex-basis: 40%;
}
.box:hover > img {
  height: 80%;
}
.box > img:hover {
  height: 93%;
}
.box:hover .box_tents {
  display: block;
  width: 96%;
  height: 96%;
  color: #555;
  font-size: 0.8rem;
}
.box_func {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  display: none;
}
.box:hover .box_func {
  display: block;
}
.box_func > img {
  width: 10%;
  display: block;
}

.remen_emo {
  position: relative;
  height: 42%;
  width: 100%;
  background: #fffe;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
Emotion{
  position: relative;
  width: 100%;
  height: 100%;
}
.remen_rightbar{
  position: relative;
  width: 37%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.remen_song{
  position: relative;
  height: 100%;
  width: 100%;
  padding: 0 0% 0% 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  /* padding: 1%; */
  /* background: #fffe; */
  /* overflow: hidden; */
  /*margin-bottom: 3%;*/
  /*border: 2px solid #fffc;*/
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);

}
.remen_song_lists{
  position: relative;
  width: 100%;
  height: 110%;
  padding: 0 10% 0% 0;
  overflow: scroll;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;

}
.remen_song_list_rank{
  position: absolute;
  margin: 3% 0 0 0;
  left: 0;
　width: 10%;
　height: 10%;
  background-color: #1b2767;
  color: #fff;
  padding: 1%;
  font-size: 1.2rem;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);

}
.remen_song_list{

  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  /*margin: 2%;*/
  padding: 2% 0 0 0;
  margin: 0 0 2% 0;
  background-color: #fffe;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
  transition: all 500ms ease-in-out;
}
.remen_song_list:hover{
  padding: 4% 0 0 0;
}
.remen_song_list_up{
  width: 92%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin: 0 2% 0 6%;
}

.remen_song_list_title {
  /*margin: 0 5% 0 0;*/
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  font-family: YaHei;
  color: #1b2767;
  line-height: 1.8rem;
  font-size: 1.2rem;
  overflow: scroll;
  border-bottom: solid 0.01rem #dce3eb;
}
.remen_song_list_artist {
  margin: 1rem 0rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: YouYuan;
  color: #000e;
  line-height: 1rem;
  font-size: 1rem;
  overflow: scroll;
}
.remen_song_list_emo {
  margin: 1rem 0rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: YouYuan;
  color: #000e;
  line-height: 1rem;
  font-size: 1rem;
  overflow: scroll;
}
.remen_song_list_times{
  margin: 1rem 1rem 1rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: YouYuan;
  color: #000e;
  line-height: 1rem;
  font-size: 1rem;
  overflow: scroll;
}

.remen_num{
  position: relative;
  height: 41%;
  width: 100%;
  background: #fffe;
  border: 2px solid #fffc;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.5);
}
</style>
