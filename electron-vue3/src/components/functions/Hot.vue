<template>
  <div class="dig">
    <div class="messageBox" v-if="bol" @click="close">
      <div class="boardout" @click.stop="">
        <div class="board">
          <div class="word">导入您关注的文本素材</div>
          <img src="../../assets/linehori.png" alt="" />
          <div class="func">
            <button>文件导入</button>
          </div>
        </div>
        <div class="chaxun">确定</div>
      </div>
    </div>
    <div class="left">
      <div class="up" v-loading="loading">
        <div class="chart1">
          <div class="simititle">增量式舆情热点</div>
          <iframe
            src="new_hot(2).html"
            name="topFrame"
            scrolling="No"
            frameborder="0"
            class="topFrame"
          ></iframe>
        </div>
        <div class="chart2">
          <div class="simititle">舆情热点事件</div>
          <iframe
            src="hot_point(2).html"
            name="topFrame"
            scrolling="No"
            frameborder="0"
            class="topFrame"
          ></iframe>
        </div>
      </div>
      <div class="down">
        <div class="simititle">当前热点</div>
        <div class="words">
          <div class="key">热点词</div>
          <div class="list">
            <div class="word" v-for="item in items">
              {{ item.title }}
            </div>
          </div>
        </div>
        <div
          class="sentence"
          onmouseout="this.start();"
          onmouseover="this.stop();"
          scrolldelay="400"
          direction="up"
          behavior="scroll"
        >
          <div class="blog" v-for="item in items2">
            <img src="../../assets/point.png" alt="" />
            <div class="tent">{{ item.title }}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="righthot">
      <div class="up">
        <div
          class="blockhot"
          onmouseout="this.start();"
          onmouseover="this.stop();"
          scrolldelay="400"
          direction="up"
          behavior="scroll"
        >
          <div class="simititle">潜在热点</div>
          <div class="things" v-for="item in items3">
            <div class="time">
              <div class="year">{{ item.year }}</div>
              <div class="date">{{ item.date }}</div>
            </div>
            <div class="static">{{ item.content }}</div>
          </div>
        </div>
      </div>
      <div class="down">
        <button type="submit" @click="toggle">数据上传</button>
      </div>
    </div>
  </div>
</template>

<script scoped>
export default {
  name: "Hot",
  data() {
    return {
      bol: false,
      loading: false,
      items: [
        {
          title: "海底捞",
        },
        {
          title: "星巴克",
        },
        {
          title: "赶人",
        },
        {
          title: "失望",
        },
        {
          title: "微信",
        },
        {
          title: "谷爱凌",
        },
        {
          title: "冬奥会",
        },
        {
          title: "雅培",
        },
        {
          title: "民生问题",
        },
        {
          title: "奶粉",
        },
      ],
      items2: [
        {
          title:
            "音九言六:之前全红婵等运动员被恶意抢注商标的事件、逍遥镇胡辣汤事件还历历在目，不是个例了，甚至可以说是猖狂了",
        },
        {
          title:
            "环球时报:国家知识产权局今天发布通告，依法打击恶意抢注“冰墩墩”、“谷爱凌”等商标注册。",
        },
        {
          title:
            "沧海缘月:（一）在主观上，实施商标抢注的当事人都具有恶意，即明知或应知他人在先创意、使用商标的情况而抢先向商标局申请注册。（二）申请人采取了不正当手段，在商标注册申请书和提供的相关材料中不真实地填报了有关事项。（三）注册成功，在客观上，被抢注的对象是他人在先使用并有一定影响的商标。",
        },
        {
          title: "心灵辅导:该查，但是不应该罚款，补缴即可",
        },
        {
          title: "金色de秋天:新规不应该只对新时段的适用吗？",
        },
        {
          title: "羽田共:做个小生意，还得交税",
        },
        {
          title: "落花有情199704:好害怕，因为买卖东西,去年流水有点高,担心呀",
        },
        {
          title: "日月星河sky:我们国家可以没有星巴克，但是不能没有人民警察",
        },
        {
          title: "知你故来风:这星巴克也太气人了呀！好大的官威啊！",
        },
        {
          title:
            "玖玖超爱喝酒:其他品牌一定要严格控制好，孩子喝的奶粉一定要做好，马虎不得",
        },
        {
          title: "诺才才:竟然有这么大的危害，看得我你都有点后怕了",
        },
        {
          title: "axenr:这种给别人打标签的行为真是迷惑",
        },
        {
          title:
            "晓格格殿下:了解顾客的需求啊，这不正常吗？很多高星酒店十几年前就开始这么做了",
        },
        {
          title:
            "张小凡有点烦:海底捞老板四川人在中国赚那么多人家扭头就转新加坡籍了，我们应该一起抵制",
        },
        {
          title: "那个元宵ismyle:标记顾客偏好挺正常的，但是有的词句不太喜欢",
        },
        {
          title:
            "不是你家薇薇:试问现在哪个地方不给顾客打标，只是没让顾客发现罢了",
        },
      ],
      items3: [
        {
          year: "2022",
          date: "3.23",
          content:
            "海关总署日前发布公告，提醒消费者“暂不通过任何渠道购买”以及“立即暂停食用”美国雅培公司旗下相关婴幼儿产品。",
        },
        {
          year: "2022",
          date: "3.26",
          content:
            "近日，雅培官网宣布召回3款婴儿配方奶粉，中国市场涉及到1款——喜康宝贝添婴儿营养补充剂产品。",
        },
        {
          year: "2022",
          date: "3.29",
          content:
            "2月18日，美国FDA宣布，雅培一工厂发现致病细菌。不到48小时，中华人民共和国海关总署发布“雅培中国召回其销售的一款特医产品”，提醒消费者立刻暂停食用雅培“喜康宝贝添”母乳强化剂。",
        },
        {
          year: "2022",
          date: "4.4",
          content:
            "奶粉出现问题已经不是一次两次了，奶粉作为低幼儿宝宝的重要营养来源，一旦出现问题，危害大就是本身就身体发育未完善的孩子",
        },
        {
          year: "2022",
          date: "4.8",
          content:
            "这个标题太吓人，帮大家划一下重点：在中国大陆销售的产品中，除喜康宝贝添婴儿营养补充剂，其他产品是安全的！那么海淘奶粉有必要吗？",
        },
        {
          year: "2022",
          date: "4.11",
          content:
            "作为一个母婴博主，不得不说一句大实话，自从三聚氰胺事件之后，中国国产奶粉的1段奶粉，执行标准是最高最严格的，家长们真的可以放心的选择国产奶粉，特别是1段奶粉，性价比高还安心。",
        },
        {
          year: "2022",
          date: "4.16",
          content:
            "目前为止国内奶标准高于国际标，很多人就喜欢看营销文，不喜欢看有数据的国家标准",
        },
        {
          year: "2022",
          date: "4.20",
          content: "我觉得还是坚持母乳或者用我们国产的奶粉放心一点",
        },
        {
          year: "2022",
          date: "4.23",
          content: "10多位婴儿出现小肠坏死等问题，甚至1例病亡",
        },
        {
          year: "2022",
          date: "4.24",
          content: "让你们买国产的，你们不信，非要买进口的、海淘的。",
        },
      ],
    };
  },
  methods: {
    toggle() {
      this.bol = !this.bol;
    },
    close() {
      this.bol = !this.bol;
    },
    iframeLoad() {
      this.loading = true;
      const iframe = this.$refs.Iframe;
      if (iframe.attachEvent) {
        // IE
        iframe.attachEvent("onload", () => {
          this.loading = false;
        });
      } else {
        // 非IE
        iframe.onload = () => {
          this.loading = false;
        };
      }
    },
    mounted() {
      this.iframeLoad();
    },
  },
};
</script>

<style scoped>
.dig {
  width: 67.5rem;
  height: 36rem;
  /* border: 1px solid; */
  display: flex;
  flex-direction: row;
}
.left {
  flex: 50rem;
  margin-right: 0rem;
  display: flex;
  flex-direction: column;
}
.left .up {
  flex: 18rem;
  margin-bottom: 1rem;
  display: flex;
  flex-direction: row;
}
.left .up .simititle {
  position: absolute;
  width: auto;
  padding: 0 1rem;
  height: 2rem;
  display: flex;
  margin: -0.5rem 0 0 -0.5rem;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background: #5e5498;
  box-shadow: 0px 11px 134px rgba(94, 84, 152, 0.5),
    0px 25.9437px 58.4156px rgba(94, 84, 152, 0.375),
    0px 4.2px 21.775px rgba(94, 84, 152, 0.2),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.125);
  border-radius: 0rem 0rem 0.5rem 0rem;
  color: #f4f2ff;
  font-size: 1.2rem;
  font-weight: 900;
  font-family: YaHei;
  transition: all 500ms ease-in-out;
  opacity: 1;
  z-index: 1;
}
.left .up .chart1 {
  flex: 25rem;
  margin-right: 1rem;
  border: 0.2rem solid #f4f2ff;
  box-shadow: inset 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}
.left .up .chart2 {
  flex: 25rem;
  border: 0.2rem solid #fff2ec;
  box-shadow: inset 0px 71px 134px rgba(155, 113, 93, 0.1),
    0px 35.9437px 58.4156px rgba(155, 113, 93, 0.0675),
    0px 14.2px 21.775px rgba(155, 113, 93, 0.05),
    0px 3.10625px 7.74687px rgba(155, 113, 93, 0.0325);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}
.left .up iframe {
  width: 23.5rem;
  height: 17rem;
  padding: 0rem;
  margin: 0rem;
  /* border: 1px solid #000; */
}
.left .down {
  flex: 18rem;
  padding: 0 1rem;
  background-color: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}

.left .down .simititle {
  position: absolute;
  width: 10rem;
  height: 2rem;
  display: flex;
  margin: -0.4rem 0 0 38.7rem;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background: #5e5498;
  box-shadow: 0px 11px 134px rgba(94, 84, 152, 0.5),
    0px 25.9437px 58.4156px rgba(94, 84, 152, 0.375),
    0px 4.2px 21.775px rgba(94, 84, 152, 0.2),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.125);
  border-radius: 0rem 0rem 0rem 0.5rem;
  color: #f4f2ff;
  font-size: 1.2rem;
  font-weight: 900;
  font-family: YaHei;
  transition: all 500ms ease-in-out;
  opacity: 1;
  z-index: 5;
}

.left .down .words {
  flex: 3rem;
  width: 47rem;
  /* height: 5rem; */
  margin: 1rem 0 0rem 0;
  display: flex;
  flex-direction: column;
  align-items: left;
  justify-content: left;
}
.left .down .words .key {
  height: 2rem;
  width: 10rem;
  /* padding: 0.2rem 1.5rem; */
  text-align: left;
  color: #6b738d;
  border-bottom: solid 0.01rem #dce3eb;
  font-size: 1.5rem;
  font-weight: 700;
  font-family: YaHei;
  display: flex;
  flex-direction: column;
  align-items: left;
  justify-content: left;
  background-color: #fff;
  /* box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325); */
}
.left .down .words .list {
  height: 3rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: left;
  font-size: 0.8rem;
  color: #a6a6a6;
  overflow: scroll;
  white-space: nowrap;
}
.left .down .words .list .word {
  padding: 0.2rem 0.4rem;
  margin: 0rem 0.2rem;
  border-radius: 0.2rem;
  white-space: nowrap;
  font-weight: 900;
}
.left .down .words .list .word:nth-child(n) {
  color: #55a55e;
  background: #edffef;
  box-shadow: 0px 71px 134px rgba(85, 165, 94, 0.1),
    0px 35.9437px 58.4156px rgba(85, 165, 94, 0.0675),
    0px 14.2px 21.775px rgba(85, 165, 94, 0.05),
    0px 3.10625px 7.74687px rgba(85, 165, 94, 0.0325);
}
.left .down .words .list .word:nth-child(2n) {
  color: #3a7f92;
  background: #ecfbff;
  box-shadow: 0px 71px 134px rgba(58, 127, 146, 0.1),
    0px 35.9437px 58.4156px rgba(58, 127, 146, 0.0675),
    0px 14.2px 21.775px rgba(58, 127, 146, 0.05),
    0px 3.10625px 7.74687px rgba(58, 127, 146, 0.0325);
}
.left .down .words .list .word:nth-child(3n) {
  color: #5e5498;
  background: #f4f2ff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
}
.left .down .words .list .word:nth-child(4n) {
  color: #9b715d;
  background: #fff2ec;
  box-shadow: 0px 71px 134px rgba(155, 113, 93, 0.1),
    0px 35.9437px 58.4156px rgba(155, 113, 93, 0.0675),
    0px 14.2px 21.775px rgba(155, 113, 93, 0.05),
    0px 3.10625px 7.74687px rgba(155, 113, 93, 0.0325);
}
.left .down .words .list .word:nth-child(5n) {
  color: #2c5fa6;
  background: #ecf4ff;
  box-shadow: 0px 71px 134px rgba(44, 95, 166, 0.1),
    0px 35.9437px 58.4156px rgba(44, 95, 166, 0.0675),
    0px 14.2px 21.775px rgba(44, 95, 166, 0.05),
    0px 3.10625px 7.74687px rgba(44, 95, 166, 0.0325);
}
.left .down .words .list .word:nth-child(6n) {
  color: #7d257d;
  background: #fff7ff;
  box-shadow: 0px 71px 134px rgba(125, 37, 125, 0.1),
    0px 35.9437px 58.4156px rgba(125, 37, 125, 0.0675),
    0px 14.2px 21.775px rgba(125, 37, 125, 0.05),
    0px 3.10625px 7.74687px rgba(125, 37, 125, 0.0325);
}
.left .down .sentence {
  flex: 10rem;
  width: 47rem;
  /* border: 0.01rem solid #0bedae77; */
  margin: 0 0 1rem 0;
  display: flex;
  flex-direction: column;
  overflow: scroll;
  white-space: nowrap;
}

.left .down .sentence .blog {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: left;
  margin-bottom: 0.5rem;
}
.left .down .sentence .blog img {
  width: 0.8rem;
  height: 0.6rem;
  margin-right: 0.5rem;
}
.left .down .sentence .blog .tent {
  font-size: 0.8rem;
  color: #000000;
  overflow: scroll;
  white-space: nowrap;
  opacity: 0.9;
  padding: 0.2rem 0 0 0;
  border-bottom: solid 0.01rem #dce3eb;
  line-height: 1.3rem;
}
.righthot {
  flex: 16.5rem;
  display: flex;
  flex-direction: column;
}
.righthot .up {
  flex: 30rem;
  padding: 0 1rem;
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
  overflow: scroll;
  height: 29rem;
}

.righthot .up .simititle {
  position: absolute;
  width: 10rem;
  height: 2rem;
  display: flex;
  margin: -0.4rem 0 0 6.7rem;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background: #5e5498;
  box-shadow: 0px 11px 134px rgba(94, 84, 152, 0.5),
    0px 25.9437px 58.4156px rgba(94, 84, 152, 0.375),
    0px 4.2px 21.775px rgba(94, 84, 152, 0.2),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.125);
  border-radius: 0rem 0rem 0rem 0.5rem;
  color: #f4f2ff;
  font-size: 1.2rem;
  font-weight: 900;
  font-family: YaHei;
  transition: all 500ms ease-in-out;
  opacity: 1;
  z-index: 5;
}

.righthot .up .blockhot .things {
  display: flex;
  margin-bottom: 1rem;
  flex-direction: column;
  background-color: #fff;
  box-shadow: 0px 7px 10px rgba(94, 84, 152, 0.1),
    0px 3.594px 5.842px rgba(94, 84, 152, 0.0675),
    0px 1.42px 2.77px rgba(94, 84, 152, 0.05),
    0px 0.311px 0.775px rgba(94, 84, 152, 0.0325);
  align-items: left;
  justify-content: center;
}
.righthot .up .blockhot .things:nth-child(n) {
  color: #55a55e;
  background: #edffef;
  box-shadow: 0px 71px 134px rgba(85, 165, 94, 0.1),
    0px 35.9437px 58.4156px rgba(85, 165, 94, 0.0675),
    0px 14.2px 21.775px rgba(85, 165, 94, 0.05),
    0px 3.10625px 7.74687px rgba(85, 165, 94, 0.0325);
}
.righthot .up .blockhot .things:nth-child(2n) {
  color: #3a7f92;
  background: #ecfbff;
  box-shadow: 0px 71px 134px rgba(58, 127, 146, 0.1),
    0px 35.9437px 58.4156px rgba(58, 127, 146, 0.0675),
    0px 14.2px 21.775px rgba(58, 127, 146, 0.05),
    0px 3.10625px 7.74687px rgba(58, 127, 146, 0.0325);
}
.righthot .up .blockhot .things:nth-child(3n) {
  color: #5e5498;
  background: #f4f2ff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
}
.righthot .up .blockhot .things:nth-child(4n) {
  color: #9b715d;
  background: #fff2ec;
  box-shadow: 0px 71px 134px rgba(155, 113, 93, 0.1),
    0px 35.9437px 58.4156px rgba(155, 113, 93, 0.0675),
    0px 14.2px 21.775px rgba(155, 113, 93, 0.05),
    0px 3.10625px 7.74687px rgba(155, 113, 93, 0.0325);
}
.righthot .up .blockhot .things:nth-child(5n) {
  color: #2c5fa6;
  background: #ecf4ff;
  box-shadow: 0px 71px 134px rgba(44, 95, 166, 0.1),
    0px 35.9437px 58.4156px rgba(44, 95, 166, 0.0675),
    0px 14.2px 21.775px rgba(44, 95, 166, 0.05),
    0px 3.10625px 7.74687px rgba(44, 95, 166, 0.0325);
}
.righthot .up .blockhot .things:nth-child(6n) {
  color: #7d257d;
  background: #fff7ff;
  box-shadow: 0px 71px 134px rgba(125, 37, 125, 0.1),
    0px 35.9437px 58.4156px rgba(125, 37, 125, 0.0675),
    0px 14.2px 21.775px rgba(125, 37, 125, 0.05),
    0px 3.10625px 7.74687px rgba(125, 37, 125, 0.0325);
}
.righthot .up .blockhot .things .time {
  padding: 0.1rem 0.4rem 0rem 0.4rem;
  height: 1.8rem;
  color: #6b738d;
  font-size: 1.5rem;
  font-weight: 500;
  font-family: YaHei;
  z-index: 1;
  display: flex;
  flex-direction: row;
  align-items: baseline;
  justify-content: left;
  border-bottom: solid 0.01rem #dce3eb;
}
.righthot .up .blockhot .things .time .date {
  font-size: 1rem;
  margin-left: 0.5rem;
  color: #b3b3b3;
}
.righthot .up .blockhot .things .static {
  color: #000;
  font-size: 0.8rem;
  font-family: YouYuan;
  opacity: 0.8;
  width: auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 0.2rem 0.5rem;
  line-height: 1.5rem;
}
.righthot .down {
  padding: 0 1rem;
  flex: 6rem;
  /* border: 0.1rem solid #778e9577;
  background-color: #778e9522; */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.righthot .down button {
  width: 16.3rem;
  height: 5.7rem;
  border: 0;
  background-color: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  color: #6b738d;
  font-size: 1rem;
  font-weight: 100;
  font-family: YouYuan;
  transition: all 200ms ease-in-out;
}
.righthot .down button:hover {
  background-color: #0bedae;
  color: #fff;
  font-weight: 500;
}

.messageBox {
  width: 100%;
  height: 100%;
  margin: 2.5rem 0rem 0rem 3.5rem;
  position: fixed;
  left: 0;
  top: 0;
  background-color: #0006;
  z-index: 2;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  /* transition: all 200ms ease-in-out; */
}
.messageBox .boardout {
  width: 20rem;
  margin: 0rem 7rem 5rem 0rem;
  border-radius: 0.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.messageBox .boardout .board {
  padding: 1rem;
  margin: 0;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 1),
    rgba(250, 251, 252, 0.8)
  );
  border-radius: 0.2rem 0.2rem 0 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.messageBox .board .word {
  width: 20rem;
  font-weight: 900;
  color: #687684;
}
.messageBox .board img {
  width: 20rem;
  height: 0.05rem;
  margin-bottom: 0.5rem;
}
.messageBox .func {
  width: 20rem;
  margin: 0.5rem 0.5rem 0rem 0.5rem;
  display: flex;
  flex-direction: row;
  align-items: baseline;
  justify-content: center;
}
.messageBox .func button {
  width: 5rem;
  height: 2rem;
  border: 0;
  border-radius: 0.2rem;
  background-color: #fff;
  filter: drop-shadow(1 1 0.01rem #000);
  font-weight: 900;
  color: #687684;
}
.messageBox .func .discrip {
  font-size: 0.6rem;
  font-weight: 900;
  color: #687684;
  filter: drop-shadow(1 1 0.01rem #000);
}
.messageBox .chaxun {
  padding: 0.5rem 1rem;
  margin: 0;
  width: 21rem;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 1),
    rgba(250, 251, 252, 1)
  );
  border-radius: 0 0 0.2rem 0.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  color: #687684;
}
</style>