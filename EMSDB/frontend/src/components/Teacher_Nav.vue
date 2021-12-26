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
          <template #title><img style="height: 28px;margin-right: 8px;" src="../assets/homePage/courseManage.png"
                                alt="image failed">
            课程管理
          </template>
          <el-menu-item index="2-1">开设课程</el-menu-item>
          <el-menu-item index="2-2">修改课程信息</el-menu-item>
          <el-menu-item index="2-3">查看选课学生</el-menu-item>
          <el-menu-item index="2-4">学生成绩录入</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title><img style="height: 28px; margin-right: 8px;" src="../assets/homePage/information.png"
                                alt="image failed">
            信息查询
          </template>
          <el-menu-item index="3-1">教学任务查询</el-menu-item>
          <el-menu-item index="3-2">空教室查询</el-menu-item>
          <el-menu-item index="3-3">教学课表</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="4">
          <template #title><img style="height: 25px; margin-right: 8px" src="../assets/homePage/apply.png" alt="img failed"> 事务申请
          </template>
          <el-menu-item index="4-1">申请请假</el-menu-item>
          <el-menu-item index="4-2">申请修改成绩</el-menu-item>
          <el-menu-item index="4-3">其他申请</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="5">
          <template #title><img style="height: 26px; margin-right: 8px" src="../assets/homePage/message.png" alt="img failed">
            消息反馈
          </template>
          <el-menu-item index="5-1">系统通知</el-menu-item>
          <el-menu-item index="5-2">处理学生申请</el-menu-item>
        </el-sub-menu>

        <el-sub-menu index="6">
          <template #title><img style="height: 28px;margin-right: 5px;" src="../assets/homePage/person.png" alt="img failed">
            个人中心
          </template>
          <el-menu-item index="6-1">个人信息</el-menu-item>
          <el-menu-item index="6-2">修改密码</el-menu-item>
          <el-menu-item index="6-3">退出登录</el-menu-item>
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
  name: "tea",
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
      this.$store.state.userType = '教师'
      if(index==='6-3') {
        this.dialogVisible = true
      } else if (index==='6-2') {
        this.$router.push('/passwordChange')
      }else if (index==='6-1') {
        this.$router.push('/personalInfo')
      }else if (index==='1') {
        this.$router.push('/teacher')
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
  left:0;
  top:0;
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