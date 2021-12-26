<template>
  <div class="bg">
    <Teacher_Nav></Teacher_Nav>
  </div>
</template>

<script>
import Teacher_Nav from "../components/Teacher_Nav";
export default {
  name: "Teacher_Home",
  components:{
    Teacher_Nav
  }
}
</script>

<style scoped>
.bg {
  background: url("../assets/homePage/bg_home.png");
  width: 100%;
  height: 100%;
  position: fixed;
  left:0;
  top:0;
  background-size: 100% 100%;
}
</style>