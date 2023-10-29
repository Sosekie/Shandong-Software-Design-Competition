<template>
    <div class="contentDeal2">
      <div class="left">2</div>
      <div class="middle">
        <div class="up">1</div>
        <div class="down">
          <div class="left">2</div>
          <div class="right">3</div>
        </div>
      </div>
      <div class="right"></div>
    </div>
</template>

<script scoped>
export default {
  name: "Deal",
};
</script>

<style scoped>
.contentDeal2 {
  flex: 34.5rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.left {
  flex: 15rem;
  height: 33.5rem;
  border: 1px solid #000;
}
.middle {
  flex: 40rem;
  height: 33.5rem;
  border: 1px solid #000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.middle .up {
  height: 10.5rem;
  width: 38rem;
  border: 1px solid #000;
  margin-bottom: 1rem;
}
.middle .down {
  width: 38rem;
  height: 22rem;
  border: 1px solid #000;
  display: flex;
}
.middle .down .left {
  flex: 27rem;
  height: 22rem;
  /* width: 29rem; */
  margin-right: 1rem;
  border: 1px solid #000;
}
.middle .down .right {
  flex: 10rem;
  height: 22rem;
  /* width: 8rem; */
  border: 1px solid #000;
}
.right {
  flex: 11.5rem;
  height: 33.5rem;
  border: 1px solid #000;
}
</style>