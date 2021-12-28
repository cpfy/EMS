<template>
  <div class="bg">
  </div>
  <div v-if="this.$store.state.userType==='学生'" style="height: 111px;">
    <Student_Nav active-index2="7-2"></Student_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='教师'" style="height: 111px;">
    <Teacher_Nav active-index2="6-2"></Teacher_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='管理员'" style="height: 111px;">
    <Admin_Nav active-index2="5-2"></Admin_Nav>
  </div>
  <div class="bg_white" ></div>
  <div class="mainBody" style="position:absolute;left: 10%; margin-top: 6%">
    <el-form
        ref="ruleForm"
        :model="ruleForm"
        :rules="rules"
        label-width="120px"
        class="demo-ruleForm"
        style="zoom: 120%"
    >
      <el-form-item label="学号" prop="studentId">
        <el-input placeholder=studentId disabled v-model="ruleForm.studentId"></el-input>
      </el-form-item>
      <el-form-item label="用户名" prop="name">
        <el-input placeholder=name disabled v-model="ruleForm.name"></el-input>
      </el-form-item>
      <el-form-item label="原密码" prop="oldPassword">
        <el-input show-password v-model="ruleForm.oldPassword"></el-input>
      </el-form-item>
      <el-form-item label="新密码" prop="newPassword">
        <el-input show-password v-model="ruleForm.newPassword"></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="confirmPassword">
        <el-input show-password v-model="ruleForm.confirmPassword"></el-input>
      </el-form-item>
    </el-form>

    <div style="display: flex;justify-content: space-between; margin-left: 150px;margin-right: 10px">
      <el-button style="zoom:130%" round @click="reset('ruleForm')">重置</el-button>
      <el-button style="zoom:130%" type="primary" round @click="onSubmit('ruleForm')">确认修改</el-button>
    </div>

  </div>
</template>

<script>
import Admin_Nav from "../components/Admin_Nav";
import Teacher_Nav from "../components/Teacher_Nav";
import Student_Nav from "../components/Student_Nav";
import qs from "qs";
export default {
  name: "Admin_PasswordChange",
  //TODO: mounted
  mounted() {
    const self = this;
    self.axios({
      method: 'post',
      url: '/mounted/',
      //TODO
      data: {
      },
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {
      var obj1 = JSON.parse(res.data);
      this.$store.state.studentId = obj1.studentId;
      this.$store.state.userType = obj1.userType;
      this.$store.state.userName = obj1.userName;

    })
  },
  data() {
    return {
      ruleForm: {
        studentId: this.$store.state.studentId,
        name: this.$store.state.userName,
        oldPassword: '',
        newPassword: '',
        confirmPassword: ''
      },
      rules: {
        oldPassword: [
          {
            required: true,
            message: '请输入原密码',
            trigger: 'blur'
          }
        ],
        newPassword: [
          {
            required: true,
            message: "请输入新密码",
            trigger: 'blur'
          },
          {
            min: 6,
            max: 18,
            message: '密码长度必须在6到18个字符之间',
            trigger: 'blur',
          }
        ],
        confirmPassword: [
          {
            required: true,
            message: "请输入新密码",
            trigger: 'blur'
          },
          {
            min: 6,
            max: 18,
            message: '密码长度必须在6到18个字符之间',
            trigger: 'blur',
          }
        ]
      },
    }

  },
  methods: {
    onSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (!valid) {
          console.log('error submit!!')
          return false
        } else {
          if (this.ruleForm.newPassword !== this.ruleForm.confirmPassword) {
            alert("两次输入密码不一样");
          } else {
            if (this.ruleForm.oldPassword === 'true') {
              //alert('OK');
              //TODO: to delete
            }
            const self = this;
            self.axios({
              method: 'post',
              url: 'http://localhost:8000/site/passwordChange/',
              data: qs.stringify({
                'oldPassword': this.ruleForm.oldPassword,
                'newPassword': this.ruleForm.newPassword
              }),
              headers: {
                'X-CSRFToken': this.getCookie('csrftoken')
              },
            }).then(res => {
              var obj1 = JSON.parse(res.data);
              //TODO: yes or no
              if (obj1.result===true) {
                alert("修改密码成功");
              }
            })

          }
        }
      })

    },
    getCookie(name) {
      var value = ';' + document.cookie;
      var parts = value.split('; ' + name + '=');
      if (parts.length === 2) return parts.pop().split(';').shift();
    },
    reset(formName) {
      this.$refs[formName].resetFields()
    }
  },

  components: {
    Admin_Nav,
    Teacher_Nav,
    Student_Nav
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
  opacity: 1;
}
.bg_white {
  margin: 4% auto 0 20%;
  padding: 20px 0 70px 60px;
  width: 53%;
  min-height: 540px;
  background-color: rgba(255, 255, 255, 1);
  box-shadow: rgb(204 204 204) 0 1px 6px;
  box-sizing: border-box;
  transition: opacity 0.2s ease-in 0s;
  display: flex;
  flex-direction: row;
  -webkit-box-align: stretch;
  align-items: stretch;
  font-size: 14px;
  opacity: 0.7;
  position: fixed;
}
.mainBody {
  position: fixed;
  margin: 4% auto 0 20%;
  padding: 20px 0 70px 10px;
}
</style>