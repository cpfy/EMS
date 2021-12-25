<template>
  <div class="background">
    <div class="Head">
      <img src="../assets/head.png" alt="img failed">
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
          <template #title><img style="height: 30px;margin-right: 5px" src="../assets/homePage/courseSelect.png"
                                alt="image failed">学生选课
          </template>
          <el-menu-item index="2-1">课程选择</el-menu-item>
          <el-menu-item index="2-2">退选课程</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title><img style="height: 28px; margin-right: 8px;" src="../assets/homePage/information.png"
                                alt="image failed">信息查询
          </template>
          <el-menu-item index="3-1">推荐课表查询</el-menu-item>
          <el-menu-item index="3-2">个人课表</el-menu-item>
          <el-menu-item index="3-3">考表查询</el-menu-item>
          <el-menu-item index="3-4">空教室查询</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="4">
          <template #title><img style="height: 25px; margin-right: 8px" src="../assets/homePage/apply.png"
                                alt="img failed"> 事务申请
          </template>
          <el-menu-item @click="fuck()" index="4-1">申请免听课程</el-menu-item>
          <el-menu-item index="4-2">申请免修课程</el-menu-item>
          <el-menu-item index="4-3">申请缓考</el-menu-item>
          <el-menu-item index="4-4">其他申请</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="5">
          <template #title><img style="height: 26px; margin-right: 8px" src="../assets/homePage/message.png"
                                alt="img failed"> 消息反馈
          </template>
          <el-menu-item index="5-1">系统通知</el-menu-item>
          <el-menu-item index="5-2">教师反馈</el-menu-item>
        </el-sub-menu>
        <el-menu-item index="6"><img style="height: 28px;margin-right: 10px;" src="../assets/homePage/teachingEva.png"
                                     alt="img failed"> 教学评价
        </el-menu-item>
        <el-sub-menu index="7">
          <template #title><img style="height: 28px;margin-right: 5px;" src="../assets/homePage/person.png"
                                alt="img failed"> 个人中心
          </template>
          <el-menu-item index="7-1">个人信息</el-menu-item>
          <el-menu-item index="7-2">修改密码</el-menu-item>
          <el-menu-item index="7-3">退出登录</el-menu-item>
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
  name: "stu",
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
      if (index === '7-3') {
        this.dialogVisible = true
      } else if (index === '7-2') {
        this.$store.state.userType = 'student'
        this.$router.push('/passwordChange')
      }
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
  margin-left: 38%;
  height: 60px;
  width: 100%;
}

.Nav {
  top: 60px;
}


</style>