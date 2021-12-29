<template>

  <a href="./template.xlsx" download="" > 点击下载成绩模板</a>
  <el-button
      size="mini"
      type="text"
      @click="download"
  >下载模板
  </el-button>

</template>

<script>

import Student_Nav from "../components/Student_Nav";

export default {
  components: {
    Student_Nav
  },
  mounted() {

  },
  data() {

    return {
      activeName: '',
      newPage: 1,
      index1: 0,
      index2: 9,
      itemNum: 9,


    }
  },
  methods: {
    download() {
      const a = document.createElement('a')
      a.setAttribute('download', "成绩模板")
      a.setAttribute('href', "./template.xlsx")
      a.click()
    },
  }
}
</script>

<style>
.el-table .warning-row {
  --el-table-tr-bg-color: var(--el-color-warning-lighter);
}

.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-lighter);
}
.bg {
  background: url("../assets/homePage/bg_home.png");
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  background-size: 100% 100%;
}

</style>