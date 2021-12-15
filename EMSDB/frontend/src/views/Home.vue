<template>

  <!--  image-->
  <div class="mainBuilding" style=" ">
    <img src="../assets/mainBuilding.png" style="position: absolute;left: 0;top:20px;height: 100vh;width: 100%"
         alt="no image">
  </div>

  <div class="sign blur" style=" position: absolute;top:0;right: 0;width: 500px;">
  </div>

  <div class="sign " style="position: absolute;top:0;right: 0;width: 500px;">


    <div class="login" style="position:absolute; top:25%;width: 500px; ">
      <h1 style="font-family: font1,serif">用户登录</h1>
      <input type="text" style="zoom: 150%;background-color: rgba(158,207,240,40%);" class="class_user qxs-icon" placeholder="用户名" v-model="userName">
      <input type="text" style="zoom: 150%;background-color: rgba(158,207,240,40%);" class="class_password qxs-icon" placeholder="密码" v-model="password">
      <br/>
      <div>
        <el-radio-group v-model="userType">
          <el-radio :label="1" style="zoom:120%">学生登录</el-radio>
          <el-radio :label="2" style="zoom:120%">教师登录</el-radio>
          <el-radio :label="3" style="zoom:120%">管理员登录</el-radio>
        </el-radio-group>
      </div>

      <el-button class="login_btn" type="primary" round>注册</el-button>
      <el-button class="login_btn" @click.native="login" type="primary" round :loading="isBtnLoading">登录</el-button>
    </div>

  </div>
</template>


<script>

export default {
  data() {
    return {
      userName: '',
      password: '',
      userType: '',
      isBtnLoading: false
    };
  },
  methods: {
    login() {
      if (!this.userName && !this.password) {
        this.$message.error('请输入用户名与密码');
      } else if (!this.userName) {
        this.$message.error('请输入用户名');
      } else if (!this.password) {
        this.$message.error('请输入密码');
      } else {
        if (!this.userType) {
          this.$message.error('请选择登录方式');
        } else {
          this.$router.push("/about");
          self.axios({
            method: 'post',
            url: '/login/',
            data: {
              'userName': this.userName,
              'password': this.password,
              'userType': this.userType
            },
            headers: {
              'X-CSRFToken': this.getCookie('csrftoken')
            },
          }).then(res => {
            var obj1 = JSON.parse(res.data);

          })
        }
      }

    }
  },
  getCookie(name) {
    var value = '; ' + document.cookie;
    var parts = value.split('; ' + name + '=');
    if (parts.length === 2) return parts.pop().split(';').shift();
  },
}

</script>


<style>
@import "../font-style/font.css";
.sign {
  font-size: 22px;
  color: #333333;
  margin: 0;
  list-style: none;
  height: auto;
  overflow: hidden;
  width: 320px;
  position: relative;
  padding: 25px 25px 120px;
  min-height: calc(100% - 145px);
}

.blur {
  position: absolute;
  object-fit: cover;
  -webkit-filter: blur(10px);
  background-color: rgba(255,255,255,0.8);
}

.class_user {
  background: url("../assets/user.png") no-repeat 2px 7px;
  background-size: 28px;
}

.class_password {
  background: url("../assets/lock.png") no-repeat 2px 7px;
  background-size: 26px;
}

.qxs-icon {
  height: 40px;
  width: 70%;
  margin-bottom: 5px;
  padding-left: 10%;
  border: 0;
  border-bottom: solid 1px lavender;
}

.login_btn {
  margin-left: 5%;
  width: 40%;
  font-size: 16px;
  background: -webkit-linear-gradient(left, #000099, #2154FA); /* Safari 5.1 - 6.0 */
  background: -o-linear-gradient(right, #000099, #2154FA); /* Opera 11.1 - 12.0 */
  background: -moz-linear-gradient(right, #000099, #2154FA); /* Firefox 3.6 - 15 */
  background: linear-gradient(to right, #000099, #2154FA); /* 标准的语法 */
  filter: brightness(1.4);
}

.outer_label {
  margin-top: 5%;
  position: relative;
  left: 0;
  top: 0;
  width: 100%;
  height: 220px;
  text-align: center;
  filter: brightness(1.4);
}

.inner_label {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  margin: auto;
  height: 50px;
}

</style>