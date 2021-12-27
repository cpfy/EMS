<template>
  <div class="bg">
  </div>
  <div v-if="this.$store.state.userType==='学生'" style="height: 111px;">
    <Student_Nav active-index2="4-3"></Student_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='教师'" style="height: 111px;">
    <Teacher_Nav active-index2="4-3"></Teacher_Nav>
  </div>
  <div class="bg_white"></div>
  <div class="form">
    <p class="head">其他事务申请</p>
    <div style="height: 30px"></div>
    <el-form
        ref="ruleForm"
        :model="ruleForm"
        :rules="rules"
        class="demo-ruleForm"
        label-position="left"
        label-width="20%"
    >

      <div style="width: 75%;">
        <el-form-item label-width="16%" label="申请事项:" prop="applyItem">
          <el-input type="textarea" :rows="3" v-model="ruleForm.applyItem"></el-input>
        </el-form-item>
      </div>
      <div style="height: 15px"></div>
      <div style="width: 75%;">
        <el-form-item label-width="16%" label="申请理由:" prop="applyReason">
          <el-input type="textarea" :rows="3" v-model="ruleForm.applyReason"></el-input>
        </el-form-item>
      </div>
      <div style="height: 100px; width: 85%">
        <p style="font-family: 等线,serif;color: #2154FA ">
          注：在申请事项需要填写必要的信息。
          <br/>
          例如：若学生需要申请补填到容量已满的课程中，则需要写出课程的编号、名称、院系、任课教师等必要的课程信息；
          若教师需要申请重新录入成绩等操作，同样需要给出课程的编号、名称、院系等必要信息。
        </p>
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
import Teacher_Nav from "../components/Teacher_Nav";

export default {
  name: "OtherApply",

  components: {
    Student_Nav,
    Teacher_Nav
  },
  data() {
    return {
      textarea: '',
      ruleForm: {
        applyReason: '',
        applyItem: ''
      },
      rules: {
        applyItem: [
          {
            required: true,
            message: '请填写要申请的事项',
            trigger: 'blur',
          }
        ],
        applyReason: [
          {
            required: true,
            message: '请填写申请理由',
            trigger: 'blur',
          }
        ]
      }
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
            url: '/other_Apply/',
            data: {
              'applyItem': this.ruleForm.applyItem,
              'applyReason': this.ruleForm.applyReason,

            },
            /*headers: {
              'X-CSRFToken': this.getCookie('csrftoken')
            },*/
          })/*.then(res => {
            //TODO; need to delete?
          })*/
          alert('申请提交成功');
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
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
  z-index: -1;
}

.bg_white {
  margin: 4% auto 0 22%;
  padding: 20px 0 70px 60px;
  width: 52%;
  height: 540px;
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
  margin-top: 4.5%;
  z-index: 1;
}

.head {
  margin-left: 30%;
  font-family: 幼圆, serif;
  font-size: 35px;
  z-index: 1;
}
</style>