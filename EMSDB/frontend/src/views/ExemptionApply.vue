<template>
  <div class="bg">
  </div>
  <div v-if="this.$store.state.userType==='学生'" style="height: 111px;">
    <Student_Nav active-index2="7-2"></Student_Nav>
  </div>
  <div class="bg_white"></div>
  <div class="form">
    <p class="head">学生免听/免修申请</p>
    <el-form
        ref="ruleForm"
        :model="ruleForm"
        :rules="rules"
        class="demo-ruleForm"
        label-position="left"
        label-width="13%"
    >
      <el-form-item style="" label="申请类型：" prop="applyType">
        <el-radio-group v-model="ruleForm.applyType">
          <el-radio label="免修申请"></el-radio>
          <el-radio label="免听申请"></el-radio>
        </el-radio-group>
      </el-form-item>
      <div style="width: 75%;">
        <el-form-item label-width="16%" label="课程名称:" prop="courseName">
          <el-input v-model="ruleForm.courseName"></el-input>
        </el-form-item>
      </div>
      <div style="width: 75%;">
        <el-form-item label-width="16%" label="课程编号:" prop="courseId">
          <el-input v-model="ruleForm.courseId"></el-input>
        </el-form-item>
      </div>

      <div style="width: 70%;display: flex;justify-content: space-between">
        <el-form-item label-width="38%" label="开课院系:" prop="courseCollege">
          <el-input v-model="ruleForm.courseCollege"></el-input>
        </el-form-item>
        <span style="width: 10%"></span>
        <el-form-item label-width="40%" label="任课教师:" prop="teacher">
          <el-input v-model="ruleForm.teacher"></el-input>
        </el-form-item>
      </div>

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
import Student_Nav from "../components/Student_Nav";

export default {
  name: "exemptionApply",
  components: {
    Student_Nav
  },
  data() {
    return {
      ruleForm: {
        textarea: '',
        applyType: '',
        courseName: '',
        courseCollege: '',
        teacher: '',
        courseId: '',
        applyReason: '',
      },
      rules: {
        applyType: [
          {
            required: true,
            message: '请选择申请类型',
            trigger: 'change',
          },
        ],
        courseName: [
          {
            required: true,
            message: '请填写课程名称',
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
        courseCollege: [
          {
            required: true,
            message: '请填写开课院系',
            trigger: 'blur',
          },
        ],
        teacher: [
          {
            required: true,
            message: '请填写任课教师姓名',
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
          const self = this;
          self.axios({
            method: 'post',
            url: '/exemptionApply/',
            data: {
              'applyType': this.ruleForm.applyType,
              'courseName': this.ruleForm.courseName,
              'courseCollege': this.ruleForm.courseCollege,
              'teacher': this.ruleForm.teacher,
              'courseId': this.ruleForm.courseId,
              'applyReason': this.ruleForm.applyReason,
            },
            headers: {
              'X-CSRFToken': this.getCookie('csrftoken')
            },
          }).then(res => {
            var obj1 = JSON.parse(res.data);
            //TODO: yes or no
            if (obj1.result===true) {
              alert("提交申请成功");
            }
          })
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
  },
  getCookie(name) {
    var value = ';' + document.cookie;
    var parts = value.split('; ' + name + '=');
    if (parts.length === 2) return parts.pop().split(';').shift();
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
}

.form {
  /*border: solid;*/
  position: fixed;
  width: 50%;
  margin-left: 26%;
  margin-top: 6%;
}

.head {
  margin-left: 22%;
  font-family: 幼圆,serif;
  font-size: 25px;
}
</style>