<template>
  <div class="p-home e-container">
    <div class="e-container-header"></div>

    <div class="e-container-body p-home__body">
      <img class="p-home__body-img" alt="Vue logo" src="../assets/logo.svg">
    </div>

    <div class="e-container-footer"></div>
  </div>
</template>

<script>
import { setTimeout } from "timers";
export default {
  mounted() {
    setTimeout(() => {
      this.$router.push({ name: "Register" });
    }, 2000);
  },
  methods: {
    onLogo() {}
  }
};
</script>

<style lang="stylus">
.p-home {
  background: #2e3191;
}

.p-home__body {
  text-align: center;
}

.p-home__body-img {
  width: 150px;
  height: 75px;
}
</style>
