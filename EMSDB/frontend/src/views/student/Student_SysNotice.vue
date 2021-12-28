<template>
  <div class="bg">
  </div>

  <div style="height: 111px;">
    <Student_Nav active-index2="5-1"></Student_Nav>

  </div>

</template>

<script>
import Student_Nav from "../../components/Student_Nav";

export default {
  name: "Student_SysNotice",
  components: {
    Student_Nav
  }
}

</script>

<style scoped>
.bg {
  background: url("../../assets/homePage/bg_home.png");
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  background-size: 100% 100%;
  opacity: 1;
}
</style>