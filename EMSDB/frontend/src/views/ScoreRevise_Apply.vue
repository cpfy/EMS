<template>
  <div class="bg">
  </div>
  <div style="height: 111px;">
    <Teacher_Nav active-index2="4-2"></Teacher_Nav>
  </div>
  <div class="bg_white"></div>


  <div class="form">
    <p class="head">成绩修改申请</p>
    <div style="height: 25px"></div>
    <el-form
        ref="ruleForm"
        :model="ruleForm"
        :rules="rules"
        class="demo-ruleForm"
        label-position="left"
        label-width="13%"
    >
      <div style="width: 70%;display: flex;justify-content: space-between">
        <el-form-item label-width="38%" label="学生姓名:" prop="studentName">
          <el-input v-model="ruleForm.studentName"></el-input>
        </el-form-item>
        <span style="width: 10%"></span>
        <el-form-item label-width="40%" label="学生学号:" prop="studentId">
          <el-input v-model="ruleForm.studentId"></el-input>
        </el-form-item>
      </div>

      <div style="width: 70%;display: flex;justify-content: space-between">
        <el-form-item label-width="38%" label="课程名称:" prop="courseName">
          <el-input v-model="ruleForm.courseName"></el-input>
        </el-form-item>
        <span style="width: 10%"></span>
        <el-form-item label-width="40%" label="开课院系:" prop="courseCollege">
          <el-input v-model="ruleForm.courseCollege"></el-input>
        </el-form-item>
      </div>

      <div style="width: 70%;display: flex;justify-content: space-between">
        <el-form-item label-width="38%" label="原有成绩:" prop="originScore">
          <el-input v-model="ruleForm.originScore"></el-input>
        </el-form-item>
        <span style="width: 10%"></span>
        <el-form-item label-width="40%" label="修改成绩:" prop="newScore">
          <el-input v-model="ruleForm.newScore"></el-input>
        </el-form-item>
      </div>

      <div style="height: 8px"></div>

      <div style="width: 75%;">
        <el-form-item label-width="16%" label="申请理由:" prop="applyReason">
          <el-input type="textarea" :rows="3" v-model="ruleForm.applyReason"></el-input>
        </el-form-item>
      </div>
      <div style="margin-left: 12%;">
        <el-form-item>
          <el-button @click="resetForm('ruleForm')">重置表单</el-button>
          <span style="margin-right: 25px;"></span>
          <el-button type="primary" @click="submitForm('ruleForm')">提交申请</el-button>
        </el-form-item>
      </div>


    </el-form>
  </div>

</template>

<script>
import Teacher_Nav from "../components/Teacher_Nav";
import qs from "qs";
export default {

  name: "Score_Revise",
  components: {
    Teacher_Nav
  },
  data() {
    return {
      textarea: '',
      ruleForm: {
        studentId: '',
        studentName: '',
        courseName: '',
        courseCollege: '',
        courseId: '',
        originScore: '',
        newScore: '',
        applyReason: '',
      },
      rules: {
        studentName: [
          {
            required: true,
            message: '请填写学生姓名',
            trigger: 'blur',
          },
        ],
        studentId: [
          {
            required: true,
            message: '请填写学生学号',
            trigger: 'blur',
          },
        ],
        courseName: [
          {
            required: true,
            message: '请填写课程编号',
            trigger: 'blur',
          },
        ],
        courseCollege: [
          {
            required: true,
            message: '请填写开课院系',
            trigger: 'blur',
          },
        ],
        courseId: [
          {
            required: true,
            message: '请填写课程编号',
            trigger: 'blur',
          },
        ],
        originScore: [
          {
            required: true,
            message: '请填写学生原成绩',
            trigger: 'blur',
          },
        ],
        newScore: [
          {
            required: true,
            message: '请填写学生课程新成绩',
            trigger: 'blur',
          },
        ],
        applyReason: [
          {
            required: true,
            message: '请填写申请理由',
            trigger: 'blur',
          },
        ],
      },
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (!valid) {
          console.log('error submit!!')
          return false
        } else {
          //alert(this.ruleForm.applyType);
          const self = this;
          self.axios({
            method: 'post',
            url: '/scoreRevise_Apply/',
            data: qs.stringify({
              'studentId': this.ruleForm.studentId,
              'studentName': this.ruleForm.studentName,
              'courseName': this.ruleForm.courseName,
              'courseCollege': this.ruleForm.courseCollege,
              'courseId': this.ruleForm.courseId,
              'originScore': this.ruleForm.originScore,
              'newScore': this.ruleForm.newScore,
              'applyReason': this.ruleForm.applyReason,

            }),
            headers: {
              'X-CSRFToken': this.getCookie('csrftoken')
            },
          }).then(res => {

            var obj1 = JSON.parse(res.data);
            //TODO: yes or no
            if (obj1.result===0) {
              alert("提交申请成功!");
            } else if (obj1.result===-1) {
              alert("申请信息填写有误，请核实后重新提交!")
            } else if (obj1.result===-2) {
              alert("您没有修改该课程成绩的权限!")
            }
          })
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
  },
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
  opacity: 1;
  z-index: -1;
}

.bg_white {
  margin: 4% auto 0 15%;
  padding: 20px 0 70px 60px;
  width: 65%;
  min-height: 540px;
  background-color: rgba(255, 255, 255, 1);
  box-shadow: rgb(204 204 204) 0 1px 6px;
  box-sizing: border-box;
  transition: opacity 0.2s ease-in 0s;
  display: flex;
  flex-direction: row;
  -webkit-box-align: stretch;
  align-items: stretch;
  opacity: 0.7;
  position: fixed;
  z-index: 0;
}
.form {
  /*border: solid;*/
  position: fixed;
  width: 50%;
  margin-left: 26%;
  margin-top: 6%;
  z-index: 1;
}

.head {
  margin-left: 26%;
  font-family: 幼圆,serif;
  font-size: 28px;
  z-index: 1;
}
</style>