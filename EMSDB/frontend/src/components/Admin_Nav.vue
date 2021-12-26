<template>
  <div style="z-index: 2;height: 22%" class="background">
    <div class="Head">
      <img style="zoom: 0.22;margin-top: 0.8%;" src="../assets/head.png" alt="img failed">
    </div>

    <div style="position: fixed;top: -20px;right: 0">
      <img src="../assets/plane.gif" alt="gif failed">
    </div>

    <div style="margin-top: 45px ;" class="Nav">
      <el-menu
          :default-active="activeIndex2"
          class="el-menu-demo"
          mode="horizontal"
          background-color="#98a8d0"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="handleSelect"
          style="opacity: 0.9"
      >
        <el-menu-item style="font-size: 18px" index="1">主页</el-menu-item>
        <el-sub-menu index="2">
          <template #title><img style="height: 28px;margin-right: 8px;" src="../assets/homePage/accountManage.png"
                                alt="image failed">
            账号管理
          </template>
          <el-menu-item index="2-1">学生账号管理</el-menu-item>
          <el-menu-item index="2-2">教师账号管理</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title><img style="height: 25px; margin-right: 10px;" src="../assets/homePage/infManage.png"
                                alt="image failed">
            信息管理
          </template>
          <el-menu-item index="3-1">课程信息管理</el-menu-item>
          <el-menu-item index="3-2">教室信息管理</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="4">
          <template #title><img style="height: 26px; margin-right: 8px" src="../assets/homePage/message.png"
                                alt="img failed">
            消息反馈
          </template>
          <el-menu-item index="4-1">发布通知</el-menu-item>
          <el-menu-item index="4-2">教师申请</el-menu-item>
          <el-menu-item index="4-3">学生申请</el-menu-item>
        </el-sub-menu>

        <el-sub-menu index="5">
          <template #title><img style="height: 28px;margin-right: 5px;" src="../assets/homePage/person.png"
                                alt="img failed">
            个人中心
          </template>
          <el-menu-item index="5-1">个人信息</el-menu-item>
          <el-menu-item index="5-2">修改密码</el-menu-item>
          <el-menu-item index="5-3">退出登录</el-menu-item>
        </el-sub-menu>
      </el-menu>
    </div>

    <el-dialog
        v-model="dialogVisible"
        title="提示"
        width="30%"
    >
      <span>您确定要退出吗？</span>
      <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="confirmLogout">确定</el-button>
        <el-button @click="dialogVisible = false">取消</el-button>
      </span>
      </template>
    </el-dialog>


  </div>

</template>

<script>

export default {
  name: "admin",
  props: {
    activeIndex2: {
      type: String,
      default: '1',
    }
  },
  data() {
    return {
      dialogVisible: false,
    }
  },
  methods: {
    handleSelect(index, indexPath) {
      this.$store.state.userType = '管理员'
      if (index === '5-3') {
        this.dialogVisible = true
      } else if (index==='5-2') {
        this.$router.push('/passwordChange')
      } else if (index==='5-1') {
        this.$router.push('/personalInfo')
      }else if (index==='1') {
        this.$router.push('/admin')
      }
      //alert(index)
    },
    confirmLogout() {
      this.$router.push('/')
      this.dialogVisible = false
    },
  }
}
</script>

<style scoped>

html, body {
  margin: 0;
  padding: 0;
}

.background {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  background-size: 100% 100%;
}

.Head {
  margin-left: 32%;
  height: 60px;
  width: 100%;
}

.Nav {
  top: 60px;
}


</style>