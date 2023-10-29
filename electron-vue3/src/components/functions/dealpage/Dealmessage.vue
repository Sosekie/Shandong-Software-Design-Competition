<template>
  <div>
    <section class="messageBox">
      <div class="word">单条查询</div>
      <input type="text" class="miaoshu" placeholder="诉求描述" />
      <div class="line">————————————or————————————</div>
      <div class="word">批量查询</div>
      <div class="func">
        <button>诉求导入</button>
        <div class="discrip">?导入格式说明</div>
      </div>
    </section>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  name: "MessageBox",
};
</script>

<style scoped>
section {
  display: absolute;
  top: 50%;
  left: 50%;
  width: 20rem;
  height: 10rem;
  background-color: #fff;
}
.messageBox .func {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
}
</style>