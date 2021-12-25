<template>
  <div class="background" style="height: 111px;">
    <Student_Nav></Student_Nav>
  </div>
  <div class="" style="border: solid;position:absolute;left: 0; margin-top: 158px">


  </div>
</template>

<script>
import Student_Nav from "../components/Student_Nav";
export default {
  name: "Student_Home",
  components:{
    Student_Nav
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