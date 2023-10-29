<template>
  <div class="body">
    <section>
      <div class="Back">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
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
}
section {
  position: absolute;
  width: 72rem;
  height: 40.5rem;
  overflow: hidden;
}
.Back {
  width: 100%;
  height: 100%;
}
.Back span {
  position: absolute;
  width: 4rem;
  height: 4rem;
  background-color: #0bedae;
  filter: drop-shadow(0 0 0.5rem #0bedae);
  /* border-radius: 1rem; */
}
.Back span:nth-child(3n + 1) {
  background: transparent;
  border: 0.2rem solid #0bedae;
}
.Back span:nth-child(1) {
  top: 50%;
  left: 50%;
  animation: animate 15s linear infinite;
}
.Back span:nth-child(2) {
  top: 80%;
  left: 40%;
  animation: animate 18s linear infinite;
}
.Back span:nth-child(3) {
  top: 10%;
  left: 65%;
  animation: animate 22s linear infinite;
}
.Back span:nth-child(4) {
  top: 60%;
  left: 70%;
  animation: animate 20s linear infinite;
}
.Back span:nth-child(5) {
  top: 15%;
  left: 25%;
  animation: animate 24s linear infinite;
}
.Back span:nth-child(6) {
  top: 70%;
  left: 20%;
  animation: animate 17s linear infinite;
}
.Back span:nth-child(7) {
  top: 85%;
  left: 90%;
  animation: animate 21s linear infinite;
}
.Back span:nth-child(8) {
  top: 30%;
  left: 80%;
  animation: animate 19s linear infinite;
}
.Back span:nth-child(9) {
  top: 40%;
  left: 10%;
  animation: animate 23s linear infinite;
}
.Back span:nth-child(10) {
  top: 90%;
  left: 10%;
  animation: animate 24s linear infinite;
}
.Back span:nth-child(11) {
  top: 100%;
  left: 30%;
  animation: animate 34s linear infinite;
}
.Back span:nth-child(12) {
  top: 100%;
  left: 70%;
  animation: animate 16s linear infinite;
}
.Back span:nth-child(13) {
  top: 100%;
  left: -5%;
  animation: animate 23s linear infinite;
}
.Back span:nth-child(14) {
  top: 100%;
  left: 90%;
  animation: animate 15s linear infinite;
}
.Back span:nth-child(15) {
  top: 100%;
  left: 50%;
  animation: animate 20s linear infinite;
}
.Back span:nth-child(16) {
  top: 70%;
  left: 35%;
  width: 10rem;
  height: 10rem;
  border-radius: 5rem;
  animation: animate1 50s linear infinite;
}
.Back span:nth-child(17) {
  top: 100%;
  left: 15%;
  width: 5rem;
  height: 5rem;
  border-radius: 5rem;
  animation: animate1 50s linear infinite;
}
.Back span:nth-child(18) {
  top: 100%;
  left: -5%;
  width: 10rem;
  height: 10rem;
  border-radius: 5rem;
  animation: animate1 40s linear infinite;
}
.Back span:nth-child(19) {
  top: 110%;
  left: 90%;
  width: 10rem;
  height: 10rem;
  border-radius: 5rem;
  animation: animate1 50s linear infinite;
}
.Back span:nth-child(20) {
  top: 60%;
  left: 72%;
  width: 5rem;
  height: 5rem;
  border-radius: 5rem;
  animation: animate1 50s linear infinite;
}

@keyframes animate {
  0% {
    transform: scale(0) translateY(0) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: scale(1) translateY(-25rem) rotate(360deg);
    opacity: 0;
  }
}
@keyframes animate1 {
  0% {
    transform: scale(0) translateY(0) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: scale(1) translateY(-50rem) rotate(360deg);
    opacity: 0;
  }
}
</style>