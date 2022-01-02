<template>
  <div class="bg">
  </div>
  <div v-if="this.$store.state.userType==='学生'" style="height: 111px;">
    <Student_Nav active-index2="7-1"></Student_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='教师'" style="height: 111px;">
    <Teacher_Nav active-index2="6-1"></Teacher_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='管理员'" style="height: 111px;">
    <Admin_Nav active-index2="5-1"></Admin_Nav>
  </div>

  <div style="height: 60px">
  </div>

  <div class="main_body"></div>
    <div class="left_part">
      <div v-if="this.$store.state.userType==='管理员'" class="icon admin-icon">
        <img class="thumb" src="../assets/personalInfo/admin.png" alt="img failed">
      </div>
      <div v-else-if="this.$store.state.userType==='教师'" class="icon teacher-icon">
        <img class="thumb" src="../assets/personalInfo/teacher.png" alt="img failed">
      </div>
      <div v-else class="icon student-icon">
        <img class="thumb" src="../assets/personalInfo/student.png" alt="img failed">
      </div>
      <div class="tab">帐号信息</div>
    </div>
    <div class="right_part">
      <div class="row textForm userName">
        <span class="label">用户名</span>
        <span style="width: 40%;" class="value">
						<el-input size="small" type="input" :placeholder="this.userName" v-model="newUserName"/>
					</span>
        <span>
          <el-button type="primary" @click="changeUserName" round size="small">修改</el-button>
        </span>
      </div>
      <div v-if="this.$store.state.userType!=='管理员'" class="row textForm realName">
        <span class="label">姓名</span>
        <span style="width: 5%;"></span>
        <span class="value gray">{{ this.realName }}</span>
      </div>
      <div v-if="this.$store.state.userType!=='管理员'" class="row textForm id">
        <span v-if="this.$store.state.userType==='学生'" class="label">学号</span>
        <span v-if="this.$store.state.userType==='教师'" class="label">教工号</span>

        <span style="width: 5%;"></span>
        <span class="value gray">{{ this.id }}</span>
      </div>
      <div v-if="this.$store.state.userType==='学生'" class="row textForm grade">
        <span class="label">年级</span>
        <span style="width: 5%;"></span>
        <span class="value gray">{{ this.grade }}</span>
      </div>
      <div v-if="this.$store.state.userType==='学生'" class="row textForm class">
        <span class="label">班级</span>
        <span style="width: 5%;"></span>
        <span class="value gray">{{ this.classNum }}</span>
      </div>
      <div v-if="this.$store.state.userType==='教师'" class="row textForm age">
        <span class="label">年龄</span>
        <span style="width: 5%;"></span>
        <span class="value gray">{{ this.age }}</span>
      </div>
      <div v-if="this.$store.state.userType==='教师'" class="row textForm phone">
        <span class="label">联系电话</span>
        <span style="width: 5%;"></span>
        <span class="value gray">{{ this.phone }}</span>
      </div>
      <div v-if="this.$store.state.userType!=='管理员'" class="row textForm college">
        <span class="label">学院</span>
        <span style="width: 5%;"></span>
        <span class="value gray">{{ this.college }}</span>
      </div>
      <div v-if="this.$store.state.userType==='学生'" class="row textForm creditGot">
        <span class="label">已修学分</span>
        <span style="width: 5%;"></span>
        <span class="value gray">{{ this.creditGot }}</span>
      </div>
      <div v-if="this.$store.state.userType==='学生'" class="row textForm creditNeed">
        <span class="label">所需学分</span>
        <span style="width: 5%;"></span>
        <span class="value gray">{{ this.creditNeed }}</span>
      </div>
      <div class="row textForm email">
        <span class="label">邮箱</span>
        <span style="width: 40%" class="value">
						<el-input size="small" type="text" :placeholder="this.email" v-model="this.newEmail"/>
					</span>
        <span>
          <el-button type="primary" @click="changeEmail" round size="small">修改</el-button>
        </span>
      </div>


    </div>


</template>

<script>
import Admin_Nav from "../components/Admin_Nav";
import Teacher_Nav from "../components/Teacher_Nav";
import Student_Nav from "../components/Student_Nav";
import axios from "axios";

export default {
  name: "personalInfo",
  components: {
    Student_Nav,
    Teacher_Nav,
    Admin_Nav
  },
  mounted() {
    const self = this;
    self.axios({
      method: 'post',
      url: 'http://localhost:8000/site/my/info/',
      data: {

      },
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {
      // var obj1 = JSON.parse(res.data);
      let obj1 = res.data
      console.log(obj1)
      this.$store.state.studentId = obj1.id;
      this.$store.state.userType = obj1.userType;
      this.$store.state.userName = obj1.userName;
      this.userName = this.$store.state.userName;
      this.realName = obj1.realName;
      this.id = obj1.id;
      this.grade = obj1.grade;
      this.classNum = obj1.classNum;
      this.college = obj1.college;
      this.creditGot = obj1.creditGot;
      this.creditNeed = obj1.creditNeed;
      this.email = obj1.email;
      this.age = obj1.age;
      this.phone = obj1.phone;
    })
  },
  data() {
    return {
      userName: this.$store.state.userName,
      realName: 'realName',
      id: 'id',
      grade: 'grade',
      classNum: 'classNum',
      college: 'college',
      creditGot: 'creditGot',
      creditNeed: 'creditNeed',
      email: 'email',
      age: 'age',
      phone: 'phone',
      newEmail: '',
      newUserName: '',


    }
  },
  methods: {

    getCookie(name) {
      var value = '; ' + document.cookie
      var parts = value.split('; ' + name + '=')
      if (parts.length === 2) return parts.pop().split(';').shift()
    },
    changeUserName() {
      const self = this
      self.axios({
        method: 'post',
        data: qs.stringify({
          'newUserName': this.newUserName,
        }),
        url: 'http://localhost:8000/site/changeUsername/',
        headers: {'X-CSRFToken': this.getCookie('csrftoken')},
      }).then(res => {
        if (res.result === false) {
          alert('用户名重复')
        } else {
          this.$message({
            type: 'success',
            message: '更新成功'
          })
          this.$store.state.userName = this.newUserName
        }
      })
    },
    changeEmail() {
      const self = this
      self.axios({
        method: 'post',
        data: qs.stringify({
          newEmail: this.newEmail,
        }),
        url: 'http://localhost:8000/site/changeEmail/',
        headers: {'X-CSRFToken': this.getCookie('csrftoken')},
      }).then(res => {
        if (res.result === false) {
          alert('修改失败，该邮箱已被绑定')
        } else {
          this.$message({
            type: 'success',
            message: '更新成功'
          })
        }
      })
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
  z-index: -100;
}

.id {
  background: url("../assets/personalInfo/id.png") left center / 20px 20px no-repeat;
}

.row {
  display: flex;
  flex-direction: row;
  -webkit-box-align: center;
  align-items: center;
  padding-left: 30px;
  margin-top: 30px;
  font-size: 14px;
}


.textForm {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-weight: bolder;
  outline: none;
  display: flex;
  flex-direction: row;
  -webkit-box-align: center;
  align-items: center;
  padding-left: 30px;
  margin-top: 30px;
  font-size: 14px;
}

.userName {

  background: url("https://assets.shimonote.com/static/lizard-one/assets/name.fd2c1f23.svg") left center / 20px 20px no-repeat;
}

.grade {
  background: url("../assets/personalInfo/grade.png") left center / 20px 20px no-repeat;
}

.realName {

  background: url("../assets/personalInfo/realName.png") left center / 20px 20px no-repeat;
}

.value {
  color: rgb(165, 165, 165);
  width: 240px;
  margin-right: 20px;
}

.gray {
  color: rgb(165, 165, 165);
}

.class {
  background: url("../assets/personalInfo/class.png") left center / 20px 20px no-repeat;
}

.age {
  background: url("../assets/personalInfo/age.png") left center / 17px 17px no-repeat;
}

.phone {
  background: url("../assets/personalInfo/phone.png") left center / 20px 20px no-repeat;
}

.college {
  background: url("../assets/personalInfo/college.png") left center / 20px 20px no-repeat;
}

.creditGot {
  background: url("../assets/personalInfo/creditGot.png") left center / 16px 16px no-repeat;
}

.creditNeed {
  background: url("../assets/personalInfo/creditNeed.png") left center / 20px 20px no-repeat;
}


.email {
  background: url("https://assets.shimonote.com/static/lizard-one/assets/email.7749113a.svg") left center / 20px 20px no-repeat;
}


.tab {
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  font-weight: bolder;
  padding: 0;
  outline: none;
  text-align: center;
  margin-bottom: 12px;
  height: 20px;
  line-height: 20px;
  cursor: pointer;
  position: relative;
  color: rgb(51, 51, 51);
}

.right_part {
  margin-top: 3%;
  margin-left: 36%;
  padding-left: 82px;
  display: flex;
  flex: 1 1 0;
  flex-direction: column;
  -webkit-box-align: stretch;
  align-items: stretch;
  -webkit-box-pack: center;
  justify-content: center;
  position: fixed;
}


.label {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  font-weight: bolder;
  margin: 0;
  padding: 0;
  outline: none;
  width: 75px;
  color: rgb(51, 51, 51);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.value {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  padding: 0;
  outline: none;
  color: rgb(0, 0, 0);
  width: 240px;
  margin-right: 30px;
}

.main_body {
  margin: 0 auto 0 20%;
  padding: 20px 0 70px 60px;
  width: 816px;
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

.left_part {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  margin: 0 0 0 25%;
  padding: 0;
  outline: none;
  width: 156px;
  display: flex;
  flex-direction: column;
  -webkit-box-align: stretch;
  align-items: stretch;
  border-right: 1px solid rgb(232, 236, 241);
  position: fixed;
  /*z-index: 2;*/

}

.icon {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  outline: none;
  align-self: center;
  border-radius: 50%;
  position: relative;
  overflow: hidden;
}

.admin-icon {
  padding-top: 0;
  margin-top: 80px;
  margin-left: 5px;
  width: 70px;
  height: 70px;
  margin-bottom: 15px;
}

.student-icon {

  padding-top: 0;
  margin-top: 110px;
  margin-left: 5px;
  width: 85px;
  height: 85px;
  margin-bottom: 10px;
}

.teacher-icon {
  padding-top: 0;
  margin-top: 110px;
  margin-left: 5px;
  width: 75px;
  height: 75px;
  margin-bottom: 15px;
}

.thumb {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  margin: 0;
  padding: 0;
  outline: none;
  border-style: none;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
}

</style>