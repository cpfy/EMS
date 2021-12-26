<template>
  <div>
    <div class="eKTRoO">
      <div class="jcJKRS">
        <div class="avatar">
          <img class="thumb"
               src="../assets/personalInfo/admin.png"  alt="img failed">
        </div>
        <div class="tab">帐号信息</div>
      </div>
      <div class="iLfUQv">
        <div class="row textForm userName">
          <span class="label">用户名</span>
          <span class="value">
						<input type="text" placeholder="用户昵称"  v-model="this.newname" >
					</span>
        </div>
        <div class="row textForm realName">
          <span class="label">姓名</span>
          <span class="value gray">未绑定</span>
          <span class="action">绑定</span>
        </div>
        <div class="row textForm studentId">
          <span class="label">学号</span>
          <span class="value gray">未绑定</span>
          <span class="action">绑定</span>
        </div>
        <div class="row textForm grade">
          <span class="label">年级</span>
          <span class="value gray">未绑定</span>
          <span class="action">绑定</span>
        </div>
        <div class="row textForm class">
          <span class="label">班级</span>
          <span class="value gray">未绑定</span>
          <span class="action">绑定</span>
        </div>
        <div class="row textForm college">
          <span class="label">学院</span>
          <span class="value gray">未绑定</span>
          <span class="action">绑定</span>
        </div>
        <div class="row textForm creditGot">
          <span class="label">已修学分</span>
          <span class="value gray">未绑定</span>
          <span class="action">绑定</span>
        </div>
        <div class="row textForm creditNeed">
          <span class="label">所需学分</span>
          <span class="value gray">未绑定</span>
          <span class="action">绑定</span>
        </div>
        <div class="row textForm email">
          <span class="label">邮箱</span>
          <span class="value gray">未绑定</span>
          <span class="action">绑定</span>
        </div>


      </div>
    </div>
  </div>

</template>

<script>
export default {
  data() {
    return {
      input: '',
      newname:this.$store.state.userName,
      newpwd:'',
      inputagain: '',
      inputname: '',
      direction: '文档制作',
      dirchange: 'false',
      namechange: 'false',
      username: '',
      birth: ''
    }
  },
  methods: {
    changepasswd(){
      const self=this
      self.axios({
        method:'post',
        data:{
          newpwd:this.newpwd,
        },
        url:'/Changepassword/',
        headers: {'X-CSRFToken': this.getCookie('csrftoken')},
      })
    },
    getCookie (name) {
      var value = '; ' + document.cookie
      var parts = value.split('; ' + name + '=')
      if (parts.length === 2) return parts.pop().split(';').shift()
    },
    changname(){
      const self=this
      self.axios({
        method:'post',
        data:{
          newname:this.newname,
        },
        url:'/changeName/',
        headers: {'X-CSRFToken': this.getCookie('csrftoken')},

      }).then(res=>{
        if(res.data===-1){
          alert('用户名重复')

        }else{
          this.$message({
            type:'success',
            message:'更新成功'
          })
          this.$store.state.userName =this.newname
        }
      })
    },
    chakan: function() {

      var tp = document.getElementById("passwd");
      if (tp.type==="password") {
        tp.type = "text";
      } else {
        tp.type = "password";
      }
    },

  },
  mounted: function() {
    let user = sessionStorage.getItem('user');
    if (user) {
      this.username = user;
    }
  },

}
</script>

<style>
.id {
  background: url(https://assets.shimonote.com/static/lizard-one/assets/id.2242e69b.svg) left center / 15px 15px no-repeat;
}

.offset {
  margin-left: 3px;
}

.accountType {
  background: url(https://assets.shimonote.com/static/lizard-one/assets/account_enterprise.9524422b.svg) left center / 15px no-repeat;
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


.studentId {
  background: url("https://assets.shimonote.com/static/lizard-one/assets/email.7749113a.svg") left center / 20px 20px no-repeat;
}

.grade {

  background: url("https://assets.shimonote.com/static/lizard-one/assets/email.7749113a.svg") left center / 20px 20px no-repeat;
}

.realName {

  background: url("https://assets.shimonote.com/static/lizard-one/assets/email.7749113a.svg") left center / 20px 20px no-repeat;
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
  background: url("https://assets.shimonote.com/static/lizard-one/assets/mobile.4cb34424.svg") left center / 20px 20px no-repeat;
}

.college {
  background: url("https://assets.shimonote.com/static/lizard-one/assets/mobile.4cb34424.svg") left center / 20px 20px no-repeat;
}

.creditGot {
  background: url("https://assets.shimonote.com/static/lizard-one/assets/mobile.4cb34424.svg") left center / 20px 20px no-repeat;
}

.creditNeed {
  background: url("https://assets.shimonote.com/static/lizard-one/assets/mobile.4cb34424.svg") left center / 20px 20px no-repeat;
}


.email {
  background: url("https://assets.shimonote.com/static/lizard-one/assets/email.7749113a.svg") left center / 20px 20px no-repeat;
}



.tab {
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  margin: 0px;
  padding: 0px;
  outline: none;
  text-align: center;
  margin-bottom: 12px;
  height: 20px;
  line-height: 20px;
  cursor: pointer;
  position: relative;
  color: rgb(51, 51, 51);
  font-weight: bold;
}

.iLfUQv {
  padding-left: 82px;
  display: flex;
  flex: 1 1 0%;
  flex-direction: column;
  -webkit-box-align: stretch;
  align-items: stretch;
  -webkit-box-pack: center;
  justify-content: center;
}




.label {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  margin: 0px;
  padding: 0px;
  outline: none;
  width: 96px;
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
  margin: 0;
  padding: 0;
  outline: none;
  color: rgb(0, 0, 0);
  width: 240px;
  margin-right: 20px;
}

.eKTRoO {
  margin: 0px auto 30px;
  padding: 130px 0px 70px 60px;
  width: 816px;
  min-height: 540px;
  background-color: rgb(255, 255, 255);
  box-shadow: rgb(204 204 204) 0px 1px 6px;
  box-sizing: border-box;
  transition: opacity 0.2s ease-in 0s;
  display: flex;
  flex-direction: row;
  -webkit-box-align: stretch;
  align-items: stretch;
  font-size: 14px;
}

.jcJKRS {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  margin: 0px;
  padding: 0px;
  outline: none;
  width: 156px;
  display: flex;
  flex-direction: column;
  -webkit-box-align: stretch;
  align-items: stretch;
  border-right: 1px solid rgb(232, 236, 241);
}

.avatar {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  margin: 0px;
  padding: 0px;
  outline: none;
  align-self: center;
  width: 58px;
  height: 58px;
  border-radius: 50%;
  position: relative;
  overflow: hidden;
  margin-bottom: 38px;
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

.hint {
  line-height: 1.15;
  text-size-adjust: 100%;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", Helvetica, Tahoma, Arial, "Microsoft YaHei", 微软雅黑, 黑体, Heiti, sans-serif, SimSun, 宋体, serif;
  font-size: 14px;
  margin: 0px;
  padding: 0px;
  outline: none;
  position: absolute;
  inset: 0px;
  width: 100%;
  height: 100%;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  display: none;
}


</style>