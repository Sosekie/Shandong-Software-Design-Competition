<template>
  <div class="dig">
    <div class="down">
      <div class="downup">
        <div class="dealcontent">
          <!-- <button @click="displayon">
            <img src="../../assets/point.png" alt="" />智能转办
          </button> -->
          <img src="../../assets/logo.jpg" alt="" />
          <div class="titlewords">您好！{{ user[0].name }}</div>
          <div class="tents">
            邮箱：
            {{ user[0].email }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script scoped>
import * as echarts from "echarts";
import LocationSelect from "./datepicker/LocationSelect.vue";
import Bar4dig from "./graph/bar4dig.vue";

export default {
  name: "Deal",
  data() {
    return {
      bol: false,
      play: false,
      key: 1,
      content: false,
      show: 1,
      user: [
        {
          name: "Admin",
          email: "3442137636@qq.com",
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
    displayon() {
      this.play = !this.play;
    },
    contentview() {
      this.content = !this.content;
    },
    getIndex(index) {
      this.key = index;
      console.log(this.key);
      this.show = 1;
    },
  },
  components: {
    LocationSelect,
    Bar4dig,
  },
};
</script>

<style scoped>
.dig {
  width: 67.5rem;
  height: 36rem;
  /* border: 1px solid; */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.dig .down {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 67.5rem;
  /* padding: 0 1rem 0 0; */
  height: 36rem;
}
.dig .down .downup {
  height: 25rem;
  display: flex;
  flex-direction: row;
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.down .dealcontent {
  position: related;
  padding: 1rem;
  background: #fff;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  width: 36.5rem;
  height: 12rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.down .dealcontent img {
  width: 4rem;
  border-radius: 2rem;
}
.down .dealcontent .titlewords {
  position: related;
  width: 15rem;
  height: 2rem;
  text-align: center;
  color: #5e5498;
  border-bottom: solid 0.01rem #dce3eb;
  font-size: 1.5rem;
  font-weight: 900;
  font-family: YaHei;
  margin: 1rem;
}
.down .dealcontent .tents {
  margin: 0 1rem 1rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: YouYuan;
  color: #797c8c;
  line-height: 1.8rem;
  font-size: 1.2rem;
  overflow: scroll;
  width: 34.5rem;
  height: 11rem;
}
.down .dealcontent button {
  position: absolute;
  border: 0;
  width: 10rem;
  height: 2rem;
  margin: 13rem 1rem 1rem 26.5rem;
  display: flex;
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
  transition: all 1000ms ease-in-out;
  opacity: 0;
}
.down .dealcontent button img {
  width: 1rem;
}
.down .dealcontent:hover button {
  opacity: 1;
}
</style>