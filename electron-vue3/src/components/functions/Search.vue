<template>
  <div class="dig">
    <div class="up">
      <div class="titlewords">今日各类舆情情况</div>
      <!-- <div class="digtotal">total</div> -->
    </div>
    <div class="themeword">该主题词情感分析</div>
    <div class="middle">
      <div class="simititle">情感分析</div>
      <Emotion></Emotion>
    </div>
    <div class="down">
      <div class="downleft">
        <Keywords></Keywords>
      </div>
      <div class="downright">
        <div class="messageblock" v-for="item in items">
          <div class="message">
            <div class="lei">农业</div>
            <div class="messagesingle">
              <div class="contents">{{ item.content }}</div>
              <div class="type">{{ item.type }}</div>
              <div class="date">{{ item.date }}</div>
              <div class="point">热度：{{ item.point }}</div>
            </div>
            <div class="messagesingle">
              <div class="contents">{{ item.content }}</div>
              <div class="type">{{ item.type }}</div>
              <div class="date">{{ item.date }}</div>
              <div class="point">热度：{{ item.point }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script scoped>
import * as echarts from "echarts";
import LocationSelect from "./datepicker/LocationSelect.vue";
import Keywords from "./searchkeywords/keywords.vue";
import Emotion from "./emotion/emotion.vue";

export default {
  name: "Dig",
  data() {
    return {
      show: false,
      items: [
        {
          content:
            "这几个项目都是市北区的老大难问题，问政青岛里边也曝光过，只是到现在也没有搞定。主要是钉子户比较多，比如说瑞昌路三角片区拆了2000多户，还剩20户钉子户，就是攻不动了。一个钉子户至少能让100户回迁做不了，孰轻孰重？不强力一点拆掉能行吗？ ​",
          type: "城市建设",
          date: "20220304",
          point: "80",
        },
        {
          content:
            "本人第一次于2021年11月份以及第二次2022年3月10日左右，在青岛福彩中心微信公众账号里申请在李家女姑小区南门门头设立福彩站点，因第一次距离不够，政策发生变化后进行了第二次申请，但是第二次一直没等到场地勘测距离人员的消息，4月12日我拨打青岛福彩中心业务部电话81978085咨询福彩工作人员，工作人员回复说：已经去实地勘测过，与福彩站点（双元路店）站号37022257相距250米（因青岛地区规定乡镇站点保护距离是400米）所以不符合规定，我提出质疑说现场本人也进行过勘测肯定不能是250米，工作人员说：下去勘测的工作人员是不会乱写记录的，工作人员再去落实一下情况。过了15分钟，我再一次致电青岛福彩中心业务部，工作人员的回复变成了同事写错了行，不是距离问题。是因为在我申请的场地的周边已经有人于2月份已经申请了，然后我又跟她说本人于2021年11月份在此场地周边进行过第一次申请，因距离不够不允许立站（因为当时青岛福彩的距离保护政策是1000米），第二次申请的时候本人于3月份特别打过青岛福彩电话说明此情况第一次已经勘察了这一次距离一定可以，因为第一次已经勘察过距离了，你们都有记录，工作人员回复让我重新申请，并未告知周边已有人申请，现在又回复我说2月份已经有人申请，也并未告知我2月份申请的是否通过，如果通过，那为何至今没有开门营业？周边也并未见福彩的门头呢？为何勘测人员明知周边已经有人申请的情况下还会去勘测距离呢？难道福彩可以只是单纯申请位置不营业吗？之前听说站点37022257和福彩工作人员关系很好，结合福彩公职工作人员不合逻辑的推脱，其中的缘由是否耐人寻味呢？要求山东福彩介入调查！！@山东福彩@山东发布 @问政山东",
          type: "经济管理",
          date: "20220413",
          point: "14",
        },
        {
          content:
            " @青岛交通运输 明确说了使用便捷青岛app实名绿色二维码乘车码乘车不需要再刷一码通。16.30左右在王家村车站坐37路车，司机说不知道有这个通知，按照司机要求我扫了。我想弄明白，我到底要不要扫一码通？ ​",
          type: "民生社保",
          date: "20220410",
          point: "25",
        },
        {
          content:
            "王沙路修路好几段是单车道，等公交车的人还站在马路上，本来就一个车道，人一站在那不但堵车，等车的人还有危险，公交车到站一停后面的车都堵起来了，今天为了躲避马路上等车的那几个人（照片上画红圈的就是等公交车的人），前车突然急刹车，导致追尾堵车！王沙路修路工程要到7月份才结束，早高峰晚高峰更是因为公交车停车、乘客等车等原因堵的要命，相关部门能不能好好规划一下？@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
          type: "交通运输",
          date: "20220404",
          point: "20",
        },
        {
          content:
            "顶牛了，违章停车占一排车道！@青岛交警 @李沧交警 @青岛交通正接触 @青岛交通广播FM897 2青岛 ​",
          type: "交通运输",
          date: "20220401",
          point: "25",
        },
        {
          content:
            "虎山花苑B区北门门前这条路被违章停车占据，又成了一条单行线！ 2青岛 ​",
          type: "交通运输",
          date: "20220329",
          point: "13",
        },
        {
          content:
            "#问政山东#疫情期间基层党员站岗无怨无悔，但自己家的拆迁款要回来怎么这么费劲！青岛市崂山区沙子口街道北崂社区老房子手续齐全，沙子口街道和开发商海尔集团、青岛畅远置业有限公司都认可，畅远置业有限公司和沙子口街道政府来回踢皮球，成天说研究就是不给解决，开发商拒绝和我们对话，畅远置业工作人员王文浩态度恶劣，扬言能办也不给办！沙子口街道政府领导更是今天拖明天，明天拖后天，就是不解决，疫情值班站岗基层党员分文不取，但要自己该要的钱就这么难吗？",
          type: "民生社保",
          date: "20220329",
          point: "24",
        },
        {
          content:
            "洛阳路和四流南路路口红绿灯🚥红灯坏了不亮，手慢了没拍下三个全黑灯的画面@青岛交通 @青岛交通广播FM897 ​",
          type: "交通运输",
          date: "20220321",
          point: "18",
        },
        {
          content:
            "滨江路每天早晚路两边都停满了车，尤其是海岸锦城小区门口和滨江路信号灯下面，会车过不去，行人都没有地方走，能不管理一下，弄上限停标志和摄像头，什么时候才能解决这种乱停车现象，给市民一个安全出行环境。@市北交警 @青岛交通广播FM897 @青岛交警 @青岛交通违章 ​​​ 2青岛 ​",
          type: "交通运输",
          date: "20220410",
          point: "15",
        },
        {
          content:
            "应该是辆营运车辆，在汽车东站路边乱停接送，上班高峰时间别车堵路导致后面路段车辆拥堵。这种没素质没别品的司机应该再回回炉了！@青岛生活情报 @青岛发布 @青岛公安 @青岛交通广播FM897 ​",
          type: "交通运输",
          date: "20220414",
          point: "20",
        },
        {
          content:
            " 特殊时期，公交车的人挤满了，还有大量穿校服的，希望能管管，感觉有点危险啊。多少座坐多少人，像深圳公交车似的，多了乘坐下一班车。会不会更好一些呢？着急坐车的，可以考虑早到车站等待！ 2青岛·北村小区 L仙女Axia的微博视频 ​",
          type: "交通运输",
          date: "20220411",
          point: "24",
        },
        {
          content:
            "我们家隔壁好像有人在家暴 但今天是我第一天搬过来 不知道是隔壁还是楼下？ 我能听到的东西撞墙的声音，能听到一个男人咬着牙说是不是没完了？不知道要不要报警？一方面不能确定是哪一家，另外一方面也没办法完全确定是存在暴力行为的@青岛公安 但是那个男人咬着牙恶狠狠说话的声音真的很可怕。这个声音大概十分钟就会出现一次，应该是从晚上11点左右就开始了，中间停了很长一段时间，现在又开始了。 ​",
          type: "民生社保",
          date: "20220411",
          point: "13",
        },
      ],
      classes: [
        {
          class: "安全监管",
          num: "12",
        },
        {
          class: "城市管理",
          num: "15",
        },
        {
          class: "交通运输",
          num: "7",
        },
        {
          class: "经济管理",
          num: "23",
        },
        {
          class: "科教文卫",
          num: "6",
        },
        {
          class: "民生社保",
          num: "33",
        },
      ],
    };
  },
  methods: {
    toggle() {
      this.show = true;
      console.log(this.show);
    },
    close() {
      this.show = false;
      console.log(this.show);
    },
  },
  components: {
    LocationSelect,
    Keywords,
    Emotion,
  },
};
</script>

<style scoped>
.dig {
  width: 67.5rem;
  height: 37rem;
  /* border: 1px solid; */
  display: flex;
  flex-direction: column;
}
.messageBox {
  width: 80%;
  height: 100%;
  margin: 2.5rem 0rem 0rem 3.5rem;
  position: fixed;
  left: 0;
  top: 0;
  background-color: #0000;
  color: #5e5498;
  z-index: 2;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  /* transition: all 200ms ease-in-out; */
}
.dig .up {
  display: flex;
  flex-direction: row;
}
.dig .up .titlewords {
  height: 2.5rem;
  width: 30rem;
  /* padding: 0.2rem 1.5rem; */
  text-align: left;
  color: #1b2767;
  border-bottom: solid 0.01rem #dce3eb;
  font-size: 1.8rem;
  font-weight: 900;
  font-family: YaHei;
  display: flex;
}
.dig .up .digtotal {
  height: 2.5rem;
  width: 30rem;
  /* padding: 0.2rem 1.5rem; */
  text-align: right;
  color: #1b2767;
  border-bottom: solid 0.01rem #dce3eb;
  font-size: 1.8rem;
  font-weight: 900;
  font-family: YaHei;
  display: flex;
}
.dig .themeword {
  margin-top: 1rem;
  position: related;
  width: 10rem;
  height: 1.5rem;
  text-align: left top;
  color: #5e5498;
  border-bottom: solid 0.01rem #dce3eb;
  font-size: 1rem;
  font-weight: 900;
  font-family: YaHei;
}
.dig .middle {
  display: flex;
  width: 66.5rem;
  height: 16rem;
  flex-direction: row;
  align-items: flex-end;
  justify-content: flex-end;
  margin-right: 1rem;
  margin-bottom: 1rem;
}
.simititle {
  position: absolute;
  width: 10rem;
  height: 2rem;
  display: flex;
  margin: -0.05rem 0 0 -0.05rem;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background: #5e5498;
  box-shadow: 0px 11px 134px rgba(94, 84, 152, 0.5),
    0px 25.9437px 58.4156px rgba(94, 84, 152, 0.375),
    0px 4.2px 21.775px rgba(94, 84, 152, 0.2),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.125);
  border-radius: 0.5rem 0rem 0rem 0rem;
  color: #f4f2ff;
  font-size: 1.2rem;
  font-weight: 900;
  font-family: YaHei;
  transition: all 500ms ease-in-out;
  opacity: 1;
  z-index: 1;
}
.dig .middle .classblock {
  padding: 1rem 1rem;
  margin: 1rem;
  letter-spacing: normal;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  background-color: #fff;
  transition: all 200ms ease-in-out;
}
.dig .middle .classblock .lei {
  height: 1.6rem;
  width: 7rem;
  text-align: center;
  font-size: 1.2rem;
  font-weight: 500;
  font-family: YaHei;
  letter-spacing: normal;
  border-bottom: solid 0.01rem #dce3eb;

  transition: all 200ms ease-in-out;
}
.dig .middle .classblock .leinum {
  margin-top: 0.2rem;
  height: 1rem;
  width: 7rem;
  font-size: 1rem;
  font-weight: 900;
  font-family: YaHei;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  transition: all 200ms ease-in-out;
}
.dig .middle .classblock .leinum .wordslei {
  font-size: 0rem;
  font-weight: 500;
  transition: all 100ms ease-in-out;
}
.dig .middle .classblock:hover .lei {
  height: 1.6rem;
  width: 8rem;
  letter-spacing: 0.2rem;
}
.dig .middle .classblock:hover .leinum {
  width: 7rem;
}
.dig .middle .classblock:hover .leinum .wordslei {
  font-size: 0.8rem;
  font-weight: 500;
}
.dig .middle .classblock:hover {
  padding: 1rem 2rem;
}

.dig .down {
  height: 20.5rem;
  width: 67.5rem;
  display: flex;
  flex-direction: row;
}
.dig .down .downleft {
  width: 20.6rem;
  height: 18.3rem;
  display: flex;
  flex-direction: column;
  border: 0.2rem solid #f4f2ff;
  box-shadow: inset 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
}

.dig .down .downright {
  padding: 0 0 1rem 1rem;
  width: 45.5rem;
  height: 18.7rem;
  overflow: scroll;
}
.dig .down .messageblock {
  width: 42.5rem;
  display: flex;
  flex-direction: column;
}
.dig .down .message {
  display: flex;
  flex-direction: column;
  width: 43.5rem;
  margin: 0rem 0rem 1rem 0rem;
  padding: 0.5rem;
  background: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  color: #797c8c;
  /* text-shadow: 0.01rem 0.01rem 1px #797c8c; */
}
.dig .down .message .lei {
  width: 15rem;
  text-align: left;
  color: #1b2767;
  border-bottom: solid 0.01rem #dce3eb;
  font-size: 1.2rem;
  font-weight: 900;
  font-family: YaHei;
  display: flex;
}
.dig .down .message .messagesingle {
  display: flex;
  flex-direction: row;
  width: 41.5rem;
  margin: 0.2rem 0rem 0.2rem 0rem;
  padding: 1rem;
  background: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  color: #797c8c;
}
.dig .down .message .contents {
  overflow: hidden;
  white-space: nowrap;
  width: 26.5rem;
  margin-right: 0.5rem;
}
.dig .down .message .type,
.date,
.point {
  width: 6rem;
  overflow: hidden;
  white-space: nowrap;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border-left: solid 0.1rem #dce3eb;
}
.dig .down .message button {
  margin-left: 0.2rem;
  width: 1.2rem;
  height: 1.2rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border: 0;
  color: #edffef;
  background: #55a55e;
  box-shadow: 0px 71px 134px rgba(85, 165, 94, 0.1),
    0px 35.9437px 58.4156px rgba(85, 165, 94, 0.0675),
    0px 14.2px 21.775px rgba(85, 165, 94, 0.05),
    0px 3.10625px 7.74687px rgba(85, 165, 94, 0.0325);
  border-radius: 0.4rem;
}
.dig .down .message .blank {
  width: 2rem;
}
.dig .down .message img {
  height: 1.2rem;
  width: 0.2rem;
  margin: 0 0.5rem;
}
.dig .down .open {
  position: relative;
  top: -1.5rem;
  z-index: -1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 35.5rem;
  margin: 0rem 0.5rem 0rem 0.5rem;
  padding: 0.2rem 0.5rem;
  background: #fff;
  border-radius: 0.2rem;
  color: #797c8c;
  /* text-shadow: 0.01rem 0.01rem 1px #687684; */
}
.dig .down .open .opendown,
.words {
  height: 0rem;
  line-height: 1.5rem;
  overflow: scroll;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 0.8rem;
  background: #fff;
  transition: all 200ms ease-in-out;
}
.dig .down .messageblock {
  transition: all 200ms ease-in-out;
}
.dig .down .messageblock:hover .open .opendown {
  height: 0rem;
}
.dig .down .messageblock:hover .words {
  height: auto;
  padding: 1rem 0.5rem;
}
</style>