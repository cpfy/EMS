<template>
  <div class="bg">
  </div>
  <div v-if="this.$store.state.userType==='student'" style="height: 111px;">
    <Student_Nav active-index2="7-1"></Student_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='teacher'" style="height: 111px;">
    <Teacher_Nav active-index2="6-1"></Teacher_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='admin'" style="height: 111px;">
    <Admin_Nav active-index2="5-1"></Admin_Nav>
  </div>
</template>

<script>
import Admin_Nav from "../components/Admin_Nav";
import Teacher_Nav from "../components/Teacher_Nav";
import Student_Nav from "../components/Student_Nav";
export default {
  name: "personalInfo",

  components: {
    Student_Nav,
    Teacher_Nav,
    Admin_Nav
  }

}
</script>

<style scoped>
.bg {
  background: url("../assets/homePage/bg_home.png");
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  background-size: 100% 100%;
  opacity: 0.4;
}
</style>