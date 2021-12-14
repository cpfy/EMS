<template>
  <div class="sign" id="sign1" title="FuckMe">

    <div class="login">
      <input type="text" style="" class="class_user qxs-icon" placeholder="用户名" v-model="userName">
      <input type="text" style="" class="class_password qxs-icon" placeholder="密码" v-model="password">
      <br/>
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
      isBtnLoading: false
    }
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
        this.$router.push("/");
        self.axios({
          method: 'post',
          url: '/login/',
          data: {
            'userName': this.userName,
            'password': this.password
          },
          headers: {
            'X-CSRFToken': this.getCookie('csrftoken')
          },
        }).then(res => {
          var obj1 = JSON.parse(res.data);

        })
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

.class_user {
  background: url("../assets/user.png") no-repeat 10px 6px;
  background-size: 26px 30px;
}

.class_password {
  background: url("../assets/lock.png") no-repeat 10px 6px;
  background-size: 26px 30px;
}

.qxs-icon {
  height: 40px;
  width: 50%;
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