<template>
  <div class="bg">
  </div>
  <div style="height: 111px;">
    <Teacher_Nav active-index2='4-1'></Teacher_Nav>
  </div>
  <div class="bg_white"></div>
  <div class="form">
    <p class="head">教师请假申请</p>
    <div style="height: 25px"></div>
    <el-form
        ref="ruleForm"
        :model="ruleForm"
        :rules="rules"
        class="demo-ruleForm"
        label-position="left"
        label-width="20%"
    >

      <div style="width: 75%;">
        <el-form-item label="申请理由:" prop="applyReason">
          <el-input v-model="ruleForm.applyReason" placeholder="具体原因">
            <template #prepend>
              <el-select v-model="ruleForm.reasonSelect" placeholder="类型" style="width: 110px">
                <el-option label="事假" value="事假"></el-option>
                <el-option label="病假" value="病假"></el-option>
                <el-option label="其他" value="其他"></el-option>
              </el-select>
            </template>
          </el-input>
        </el-form-item>
      </div>

      <div style="width: 75%;">
        <el-form-item label="请假时间" required>
          <el-col :span="11">
            <el-form-item prop="beginDate">
              <el-date-picker
                  v-model="ruleForm.beginDate"
                  type="date"
                  placeholder="起始日期"
                  style="width: 100%"
              ></el-date-picker>
            </el-form-item>
          </el-col>
          <el-col class="line" :span="2">-</el-col>
          <el-col :span="11">
            <el-form-item prop="endDate">
              <el-date-picker
                  v-model="ruleForm.endDate"
                  type="date"
                  placeholder="结束日期"
                  style="width: 100%"
              ></el-date-picker>
            </el-form-item>
          </el-col>
        </el-form-item>
      </div>

      <el-form-item label="需要其他老师代课" @click="needSubstitute" prop="substitute">
        <el-switch v-model="ruleForm.substitute"></el-switch>
      </el-form-item>

      <div v-if="this.ruleForm.substitute===true">
        <div style="width: 35%">
          <el-form-item label-width="42%" label="代课教师姓名:" prop="subTeacherName" required>
            <el-input v-model="ruleForm.subTeacherName" placeholder="姓名"></el-input>
          </el-form-item>
        </div>
        <div style="width: 35%">
          <el-form-item label-width="41%" label="代课教师教工号:" prop="subTeacherId" required>
            <el-input v-model="ruleForm.subTeacherId" placeholder="教工号"></el-input>
          </el-form-item>
        </div>
        <div style="width: 35%">
          <el-form-item label-width="42%" label="代课教师院系:" prop="subTeacherCollege" required>
            <el-input v-model="ruleForm.subTeacherCollege" placeholder="院系"></el-input>
          </el-form-item>
        </div>
      </div>
      <div v-else>
        <el-form-item label="需要其他时间补课" prop="supplement">
          <el-switch v-model="ruleForm.supplement"></el-switch>
        </el-form-item>
        <div v-if="this.ruleForm.supplement===true">
          <div style="width: 35%">
            <el-form-item label-width="42%" label="补课时间:" prop="supplementDate" required>
              <el-date-picker
                  v-model="ruleForm.supplementDate"
                  type="date"
                  placeholder="请选择补课时间"
                  style="width: 100%"
              ></el-date-picker>
            </el-form-item>
          </div>
          <div style="width: 35%">
            <el-form-item label-width="42%" label="补课地点:" prop="supplementPos" required>
              <el-input v-model="ruleForm.supplementPos" placeholder="补课地点"></el-input>
            </el-form-item>
          </div>
        </div>
      </div>

      <div style="height: 25px"></div>

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
import Teacher_Nav from "../../components/Teacher_Nav";
import qs from "qs";

export default {
  name: "Leave_Apply",
  components: {
    Teacher_Nav
  },
  data() {
    const checkSubstitute = (rule, value, callback) => {
      if (this.ruleForm.substitute === true && value === '') {
        return callback(new Error('请输入代课教师信息'))
      }
    }
    const checkSupplement = (rule, value, callback) => {
      if (this.ruleForm.supplement === true && value === '') {
        return callback(new Error('请输入补课日期/地点'))
      }
    }
    const checkDate = (rule, value, callback) => {
      if (this.ruleForm.beginDate > value ) {
        return callback(new Error('结束日期不得晚于起始日期'))
      }
    }
    return {
      textarea: '',
      select: '',

      ruleForm: {
        reasonSelect: '',
        applyReason: '',
        beginDate: '',
        endDate: '',
        supplement: false,
        substitute: false,
        subTeacherName: '',
        subTeacherId: '',
        subTeacherCollege: '',

        supplementDate: '',
        supplementPos: '',

      },
      rules: {
        reasonSelect: [
          {
            required: true,
            message: '请选择请假类型',
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
        beginDate: [
          {
            type: 'date',
            required: true,
            message: '请选择起始日期',
            trigger: 'change',
          },
        ],
        endDate: [
          {
            type: 'date',
            required: true,
            message: '请选择结束日期',
            trigger: 'change',
          },
          {
            validator: checkDate, trigger: 'change'
          }
        ],
        subTeacherName: [{validator: checkSubstitute, trigger: 'blur'}],
        subTeacherId: [{validator: checkSubstitute, trigger: 'blur'}],
        subTeacherCollege: [{validator: checkSubstitute, trigger: 'blur'}],
        supplementDate: [{validator: checkSupplement, trigger: 'blur'}],
        supplementPos: [{validator: checkSupplement, trigger: 'blur'}],
      },
    }
  },
  methods: {
    submitForm(formName) {
      alert(this.ruleForm.beginDate)
      this.$refs[formName].validate((valid) => {
        if (!valid) {
          console.log('error submit!!')
          return false
        } else {
          //alert(this.ruleForm.applyType);
          const self = this;
          self.axios({
            method: 'post',
            url: '/leave_Apply/',
            data: qs.stringify({
              'reasonSelect': this.ruleForm.reasonSelect,
              'applyReason': this.ruleForm.applyReason,
              'beginDate': this.ruleForm.beginDate,
              'endDate': this.ruleForm.endDate,
              'supplement': this.ruleForm.supplement,
              'substitute': this.ruleForm.substitute,
              'subTeacherName': this.ruleForm.subTeacherName,
              'subTeacherId': this.ruleForm.subTeacherId,
              'subTeacherCollege': this.ruleForm.subTeacherCollege,
              'supplementDate': this.ruleForm.supplementDate,
              'supplementPos': this.ruleForm.supplementPos,

            }),
            headers: {
              'X-CSRFToken': this.getCookie('csrftoken')
            },
          }).then(res => {

            var obj1 = JSON.parse(res.data);
            //TODO: yes or no
            if (obj1.result === 0) {
              alert("提交申请成功!");
            } else if (obj1.result === -1) {
              alert("代课教师信息有误，请核实后重新提交!")
            }
          })
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
    needSubstitute() {
      this.ruleForm.supplement = false;
    }
  },

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
  z-index: -1;
}

.bg_white {
  margin: 4% auto 0 15%;
  padding: 20px 0 70px 60px;
  width: 65%;
  height: 635px;
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
  font-size: 28px;
  z-index: 1;
}
</style>