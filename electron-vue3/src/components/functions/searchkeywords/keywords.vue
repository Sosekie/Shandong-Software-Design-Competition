<template>
  <div class="body">
    <section>
      <div class="Back">
        <span>小麦</span>
        <span>虫害</span>
        <span>农业</span>
        <span>袁隆平</span>
        <span>白菜价格</span>
        <span>猪肉</span>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.body {
  margin: 0;
  padding: 0;
  width: 66.5rem;
  height: 16rem;
}
section {
  position: absolute;
  width: 20.6rem;
  height: 18.3rem;
  overflow: hidden;
}
.Back {
  width: 100%;
  height: 100%;
}
.Back span {
  position: absolute;
  width: auto;
  height: auto;
  font-size: 1.5rem;
  border-radius: 0.5rem;
  padding: 0.5rem;
  /* border-radius: 1rem; */
}
.Back span:nth-child(n) {
  top: 80%;
  left: 10%;
  animation: animate 7s linear infinite;
  color: #edffef;
  background: #55a55e;
  box-shadow: 0px 71px 134px rgba(85, 165, 94, 0.1),
    0px 35.9437px 58.4156px rgba(85, 165, 94, 0.0675),
    0px 14.2px 21.775px rgba(85, 165, 94, 0.05),
    0px 3.10625px 7.74687px rgba(85, 165, 94, 0.0325);
}
.Back span:nth-child(2n) {
  top: 80%;
  left: 40%;
  animation: animate 6s linear infinite;
  color: #ecfbff;
  background: #3a7f92;
  box-shadow: 0px 71px 134px rgba(58, 127, 146, 0.1),
    0px 35.9437px 58.4156px rgba(58, 127, 146, 0.0675),
    0px 14.2px 21.775px rgba(58, 127, 146, 0.05),
    0px 3.10625px 7.74687px rgba(58, 127, 146, 0.0325);
}
.Back span:nth-child(3n) {
  top: 90%;
  left: 65%;
  animation: animate 12s linear infinite;
  color: #f4f2ff;
  background: #5e5498;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
}
.Back span:nth-child(4n) {
  top: 60%;
  left: 70%;
  animation: animate 5s linear infinite;
  color: #fff2ec;
  background: #9b715d;
  box-shadow: 0px 71px 134px rgba(155, 113, 93, 0.1),
    0px 35.9437px 58.4156px rgba(155, 113, 93, 0.0675),
    0px 14.2px 21.775px rgba(155, 113, 93, 0.05),
    0px 3.10625px 7.74687px rgba(155, 113, 93, 0.0325);
}
.Back span:nth-child(5n) {
  top: 80%;
  left: 50%;
  animation: animate 10s linear infinite;
  color: #ecf4ff;
  background: #2c5fa6;
  box-shadow: 0px 71px 134px rgba(44, 95, 166, 0.1),
    0px 35.9437px 58.4156px rgba(44, 95, 166, 0.0675),
    0px 14.2px 21.775px rgba(44, 95, 166, 0.05),
    0px 3.10625px 7.74687px rgba(44, 95, 166, 0.0325);
}
.Back span:nth-child(6n) {
  top: 70%;
  left: 20%;
  animation: animate 7s linear infinite;
  color: #fff7ff;
  background: #7d257d;
  box-shadow: 0px 71px 134px rgba(125, 37, 125, 0.1),
    0px 35.9437px 58.4156px rgba(125, 37, 125, 0.0675),
    0px 14.2px 21.775px rgba(125, 37, 125, 0.05),
    0px 3.10625px 7.74687px rgba(125, 37, 125, 0.0325);
}

@keyframes animate {
  0% {
    transform: scale(0.5) translateY(3rem) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: scale(1.2) translateY(-9rem) rotate(0deg);
    opacity: 0;
  }
}
</style>