<template>
  <div class="bg">
  </div>
  <div style="height: 111px;">
    <Admin_Nav active-index2="4-1"></Admin_Nav>
  </div>
  <div class="bg_white"></div>
  <div class="form">
    <p class="head">通知发布</p>
    <div style="height: 30px"></div>
    <el-form
        ref="ruleForm"
        :model="ruleForm"
        :rules="rules"
        class="demo-ruleForm"
        label-position="left"
        label-width="20%"
    >

      <div style="width: 88%">
        <el-form-item label="请选择要通知的对象：" label-width="43%" style="zoom: 120%" prop="object">
          <el-checkbox-group v-model="ruleForm.object">
            <el-checkbox label="全体教师" name="obj"></el-checkbox>
            <el-checkbox label="全体同学" name="obj"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
      </div>

      <div style="height: 15px"></div>
      <div style="width: 88%;">
        <el-form-item style="zoom: 120%" label-width="22%" label="通知内容:" prop="content">
          <el-input type="textarea" :rows="3" v-model="ruleForm.content"></el-input>
        </el-form-item>
      </div>
      <div style="height: 15px"></div>


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
import Admin_Nav from "../components/Admin_Nav";
import qs from "qs";

export default {
  name: "Notice_Send",
  components: {
    Admin_Nav
  },
  data() {
    return {
      textarea: '',
      ruleForm: {
        content: '',
        object: [],
      },
      rules: {
        object: [
          {
            type: 'array',
            required: true,
            message: '请至少选择一项',
            trigger: 'change',
          },
        ],
        content: [
          {required: true, message: '请填写通知内容', trigger:'blur'}
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
            url: '/notice_Send/',
            //TODO:
            data: qs.stringify({
              'object': this.ruleForm.object,
              'content': this.ruleForm.content,
            }),
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
}

.bg_white {
  margin: 4% auto 0 30%;
  padding: 20px 0 70px 60px;
  width: 42%;
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
  width: 30%;
  margin-left: 37%;
  margin-top: 6%;
  z-index: 1;
}

.head {
  margin-left: 30%;
  font-family: 幼圆, serif;
  font-size: 35px;
  z-index: 1;
}
</style>