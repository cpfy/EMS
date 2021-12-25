<template>
  <div class="bg">
  </div>
  <div v-if="this.$store.state.userType==='student'" style="height: 111px;">
    <Student_Nav active-index2="7-2"></Student_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='teacher'" style="height: 111px;">
    <Teacher_Nav active-index2="6-2"></Teacher_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='admin'" style="height: 111px;">
    <Admin_Nav active-index2="5-2"></Admin_Nav>
  </div>
  <div class="mainBody" style="position:absolute;left: 10%; margin-top: 6%">
    <el-form
        ref="ruleForm"
        :model="ruleForm"
        :rules="rules"
        label-width="120px"
        class="demo-ruleForm"
        style="zoom: 120%"
    >
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
      <el-button style="zoom:130%" @click="reset('ruleForm')">重置</el-button>
      <el-button style="zoom:130%" type="primary" @click="onSubmit('ruleForm')">确认修改</el-button>
    </div>

  </div>
</template>

<script>
import Admin_Nav from "../components/Admin_Nav";
import Teacher_Nav from "../components/Teacher_Nav";
import Student_Nav from "../components/Student_Nav";
export default {
  name: "Admin_PasswordChange",

  data() {
    return {
      ruleForm: {
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
              alert('OK');
              //TODO: to delete
            }
            const self = this;
            self.axios({
              method: 'post',
              url: '/admin/passwordChange',
              data: {
                'oldPassword': this.ruleForm.oldPassword,
                'newPassword': this.ruleForm.newPassword
              },
              headers: {
                'X-CSRFToken': this.getCookie('csrftoken')
              },
            }).then(res => {
              var obj1 = JSON.parse(res.data);
              //TODO: yes or no
            })

          }
        }
      })

    },
    reset(formName) {
      this.$refs[formName].resetFields()
    }
  },
  getCookie(name) {
    var value = ';' + document.cookie;
    var parts = value.split('; ' + name + '=');
    if (parts.length === 2) return parts.pop().split(';').shift();
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
  opacity: 0.4;
}
</style>