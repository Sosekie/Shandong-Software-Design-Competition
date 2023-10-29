<template>
  <div class="selectbox">
    <el-select
      v-model="value"
      placeholder="选择地区"
      style="
        width: 7rem;
        height: 4rem;
        color: #000;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #f4f2ff;
      "
    >
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        style="width: 7rem; height: 2rem"
      >
      </el-option>
    </el-select>
  </div>
</template>

<script>
import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

Vue.use(ElementUI);

export default {
  data() {
    return {
      options: [
        {
          value: "Option1",
          label: "青岛市",
        },
        {
          value: "Option2",
          label: "济南市",
        },
        {
          value: "Option3",
          label: "潍坊市",
        },
        {
          value: "Option4",
          label: "烟台市",
        },
        {
          value: "Option5",
          label: "日照市",
        },
      ],
      value: "",
    };
  },
};
</script>
<style scoped>
.selectbox {
  width: 7rem;
  height: 4rem;
  overflow: hidden;
  margin: 0 1rem 1rem 1rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
</style>