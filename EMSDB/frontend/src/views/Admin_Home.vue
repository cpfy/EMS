<template>
  <div class="background" style="height: 111px;">
    <Admin_Nav></Admin_Nav>
  </div>
  <div class="" style="border: solid;position:absolute;left: 0; margin-top: 158px">


  </div>
</template>

<script>
import Admin_Nav from "../components/Admin_Nav";
export default {
  name: "Admin_Home",
  components: {
    Admin_Nav
  }
}
</script>

<style scoped>
.background {
  background: url("../assets/homePage/bg_home.png");
  width: 100%;
  height: 100%;
  position: fixed;
  left:0;
  top:0;
  background-size: 100% 100%;
}
</style>