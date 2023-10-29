<template>
  <div class="container">
    <div class="innerContainer">
      <img src="../assets/background.png" class="background" alt="" />
      <div class="headBar">
        <div class="search">
          <img src="../assets/search.png" alt="" />
          <input type="text" placeholder="欢迎使用大音希声视频配乐工具！" />
        </div>
      </div>
      <div class="headBar_shadow"></div>
      <div class="leftBar">
        <div class="up">
          <router-link to="/Home"
            ><div class="logo">
              <img src="../assets/logo.jpg" alt="" />
            </div>
          </router-link>
          <router-link to="/">
            <button class="dig">
              <img src="../assets/shipin.png" alt="" />
              <span class="words">演示视频</span>
            </button>
          </router-link>
          <router-link to="/Remen">
            <button class="dig">
              <img src="../assets/remen.png" alt="" />
              <span class="words">乡旅热门</span>
            </button>
          </router-link>
          <router-link to="/Picture">
            <button class="dig">
              <img src="../assets/picture.png" alt="" />
              <span class="words">单图配乐</span>
            </button>
          </router-link>
          <router-link to="/Video">
            <button class="hot">
              <img src="../assets/video.png" alt="" />
              <span class="words">视频配乐</span>
            </button>
          </router-link>
          <router-link to="/Album">
            <button class="deal">
              <img src="../assets/album.png" alt="" />
              <span class="words">多图生成</span>
            </button>
          </router-link>
        </div>
        <div class="middle"></div>
        <div class="down">
          <router-link to="/Home"
            ><button class="home">
              <img src="../assets/home.png" alt="" />
              <span class="words">主页</span>
            </button>
          </router-link>
        </div>
      </div>
      <div class="leftBar_shadow"></div>
      <div class="content">
        <div class="messageBox" v-if="col" @click="close">
          <div class="boardout" @click.stop="">
            <div class="board">
              <div class="word">数据收集</div>
              <img src="../assets/linehori.png" alt="" />
              <div class="workname">收集主题</div>
              <input type="text" class="miaoshu" placeholder="请输入收集主题" />
              <div class="workname">舆情收集范围</div>
              <div class="func">
                <div class="func1">
                  <DatePicker></DatePicker>
                </div>
                <div class="func2">
                  <LocationSelect></LocationSelect>
                </div>
              </div>
            </div>
            <div class="chaxun">
              <button @click="close">收集</button>
            </div>
          </div>
        </div>
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import ElementUI from "element-ui";
Vue.use(ElementUI);

import DatePicker from "./functions/datepicker/DatePicker.vue";
import LocationSelect from "./functions/datepicker/LocationSelect.vue";

export default {
  data() {
    return {
      col: false,
    };
  },
  methods: {
    collect() {
      this.col = !this.col;
      console.log(this.col);
    },
    close() {
      this.col = !this.col;
      console.log(this.col);
    },
  },
  components: {
    DatePicker,
    LocationSelect,
  },
};
</script>

<style>
.background {
  position: absolute;
}
.router-link-active {
  text-decoration: none;
  color: #838383;
}
a {
  text-decoration: none;
  color: #838383;
}
.innerContainer {
  width: 100%;
  height: 100%;
  background-color: #fff;
  display: flex;
  font-family: YouYuan;
}
Background {
  z-index: 1;
}
.content {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.leftBar {
  background-color: #fffe;
  position: absolute;
  width: 3.5%;
  height: 100%;
  overflow: hidden;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  transition: all 300ms ease-in-out;
  font-size: 0.8rem;
  color: #838383;
  z-index: 5;
}
.leftBar_shadow {
  background-color: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.3);
  position: absolute;
  width: 3.5%;
  height: 100%;
  overflow: hidden;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  transition: all 200ms ease-in-out;
  font-size: 0.8rem;
  color: #838383;
  z-index: 1;
}
.leftBar:hover {
  width: 4%;
  background-color: #fff;
}
.leftBar .up {
  flex: 12rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
}
.leftBar .up .logo img {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 1.5rem;
}
.leftBar img {
  width: 1.2rem;
  height: 1.2rem;
  filter: drop-shadow(0 0 0.01rem #838383);
}
.leftBar .dig,
.hot,
.deal,
.home {
  background-color: #83838300;
  border: 0;
  height: 2.2rem;
  width: 4rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  transition: all 200ms ease-in-out;
  font-size: 0.8rem;
  font-weight: 100;
  text-align: center;
  font-family: YouYuan;
}
.leftBar .dig:hover,
.hot:hover,
.deal:hover,
.home:hover {
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  width: 5rem;
  color: #838383;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.2);
}
.leftBar .dig:focus,
.hot:focus,
.deal:focus,
.home:focus {
  width: 5rem;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  color: #838383;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.2);
}
.leftBar .home img {
  display: inline-block;
  width: 1.6rem;
  height: 1.5rem;
}
.leftBar .dig .words {
  display: none;
}
.leftBar .hot .words {
  display: none;
}
.leftBar .deal .words {
  display: none;
}
.leftBar .home .words {
  display: none;
}
.leftBar .dig:hover img {
  display: none;
}
.leftBar .dig:hover .words {
  display: inline-block;
}
.leftBar .hot:hover img {
  display: none;
}
.leftBar .hot:hover .words {
  display: inline-block;
}
.leftBar .deal:hover img {
  display: none;
}
.leftBar .deal:hover .words {
  display: inline-block;
}
.leftBar .home:hover img {
  display: none;
}
.leftBar .home:hover .words {
  display: inline-block;
}

.leftBar .middle {
  flex: 14.5rem;
  -webkit-app-region: drag;
}
.leftBar .down {
  flex: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
}

.headBar {
  background-color: #fffe;
  position: absolute;
  width: 100%;
  height: 5%;
  overflow: hidden;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  -webkit-app-region: drag;
  z-index: 5;
}
.headBar_shadow {
  background-color: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  position: absolute;
  width: 100%;
  height: 5%;
  overflow: hidden;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  -webkit-app-region: drag;
  z-index: 1;
  box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.3);
}
.headBar .collect {
  margin-right: 1rem;
  padding: 0.2rem;
  border: 0.1rem solid #838383;
  border-radius: 1rem;
  transition: all 200ms ease-in-out;
}
.headBar .collect button {
  width: auto;
  height: 1rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border: 0;
  background-color: #83838300;
  -webkit-app-region: no-drag;
}
.headBar .collect img {
  width: 1rem;
  height: 1rem;
  transition: all 200ms ease-in-out;
}
.headBar .collect:hover img {
  width: 0rem;
  height: 0rem;
}
.headBar .collect .cc {
  color: #5e5498;
  font-family: YaHei;
  font-size: 0rem;
  transition: all 200ms ease-in-out;
}
.headBar .collect:hover .cc {
  font-size: 0.8rem;
  display: block;

  color: #f4f2ff;
}
.headBar .collect:hover {
  background: #5e5498;
  box-shadow: 0px 11px 134px rgba(94, 84, 152, 0.5),
    0px 25.9437px 58.4156px rgba(94, 84, 152, 0.375),
    0px 4.2px 21.775px rgba(94, 84, 152, 0.2),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.125);
  border-radius: 0.5rem;
  border: 0;
}

.messageBox {
  width: 100%;
  height: 100%;
  margin: 2.5rem 0rem 0rem 3.5rem;
  position: fixed;
  left: 0;
  top: 0;
  background-color: #fffa;
  z-index: 2;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.messageBox .boardout {
  width: 30rem;
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
  background-color: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  border-radius: 0.2rem 0.2rem 0 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.messageBox .board .word {
  width: 30rem;
  text-align: left;
  color: #1b2767;
  font-size: 1.8rem;
  font-weight: 900;
  font-family: YaHei;
}
.messageBox .board img {
  width: 30rem;
  height: 0.05rem;
  margin-top: 0.5rem;
}
.messageBox .board .workname {
  width: 29rem;
  margin-top: 0.5rem;
  outline: medium;
  color: #605498;
  font-size: 1rem;
  font-weight: 900;
  font-family: YaHei;
}
.messageBox .board input {
  width: 29rem;
  margin: 0.5rem;
  padding: 0.5rem;
  border: 0;
  border-radius: 0.2rem;
  background-color: #fff;
  outline: medium;
  font-size: 0.8rem;
  font-weight: 100;
  text-align: left;
  font-family: YouYuan;
  -webkit-app-region: no-drag;
  color: #5e5498;
  background: #f4f2ff;
  box-shadow: inset 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
}
.messageBox .func {
  width: 30rem;
  margin: 1rem 0.5rem 0rem 0.5rem;
  display: flex;
  flex-direction: row;
  align-items: baseline;
  justify-content: left;
}
.messageBox .func .func1,
.func2 {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 3rem;
}
.messageBox .func LocationSelect {
  margin-top: 2rem;
}
.messageBox .chaxun {
  padding: 0.5rem 1rem;
  margin: 0;
  width: 31rem;
  background-color: #fff;
  border-radius: 0 0 0.2rem 0.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 900;
}
.messageBox .chaxun button {
  padding: 0.2rem 0;
  width: 31rem;
  border: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background: #5e5498;
  box-shadow: 0px 11px 134px rgba(94, 84, 152, 0.5),
    0px 25.9437px 58.4156px rgba(94, 84, 152, 0.375),
    0px 4.2px 21.775px rgba(94, 84, 152, 0.2),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.125);
  border-radius: 0.5rem;
  color: #f4f2ff;
  font-size: 1.2rem;
  font-weight: 900;
  font-family: YaHei;
}

.headBar .search {
  width: 18rem;
  height: 1.5rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: #fff;
  border-radius: 1rem;
  color: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  -webkit-app-region: no-drag;
  transition: all 200ms ease-in-out;
}
.headBar .search:hover {
  width: 20rem;
}
.headBar .search:hover input {
  width: 17.5rem;
}
.headBar .search img {
  margin-top: 0.2rem;
  margin-right: 0.2rem;
  width: 1rem;
  height: 1rem;
  filter: drop-shadow(0 0 0.3rem #838383);
}
.headBar .search input {
  width: 15.5rem;
  background-color: #0000;
  border: 0;
  outline: medium;
  color: #838383;
  opacity: 1;
  font-size: 1rem;
  filter: drop-shadow(0 0 0.03rem #fff);
  font-weight: 100;
  text-align: center;
  font-family: YouYuan;
  -webkit-app-region: no-drag;
  transition: all 200ms ease-in-out;
}
.headBar .search input::-webkit-input-placeholder {
  color: #838383;
  opacity: 0.8;
  font-weight: 100;
  text-align: center;
}
</style>