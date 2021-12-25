<template>
  <div class="Head">
    <h1>教务管理系统-管理员</h1>
  </div>
  <div>
    <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        @select="handleSelect"
    >
      <el-menu-item style="font-size: 18px" index="1">主页</el-menu-item>
      <el-sub-menu index="2">
        <template #title><img style="height: 28px;margin-right: 8px;" src="../assets/accountManage.png" alt="image failed">
          账号管理
        </template>
        <el-menu-item index="2-1">学生账号管理</el-menu-item>
        <el-menu-item index="2-2">教师账号管理</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="3">
        <template #title><img style="height: 25px; margin-right: 10px;" src="../assets/infManage.png" alt="image failed">
          信息管理
        </template>
        <el-menu-item index="3-1">课程信息管理</el-menu-item>
        <el-menu-item index="3-2">教室信息管理</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="4">
        <template #title><img style="height: 26px; margin-right: 8px" src="../assets/message.png" alt="img failed"> 消息反馈</template>
        <el-menu-item index="4-1">发布通知</el-menu-item>
        <el-menu-item index="4-2">教师申请</el-menu-item>
        <el-menu-item index="4-3">学生申请</el-menu-item>
      </el-sub-menu>

      <el-sub-menu index="5">
        <template #title><img style="height: 28px;margin-right: 5px;" src="../assets/person.png" alt="img failed"> 个人中心
        </template>
        <el-menu-item index="5-1">个人信息</el-menu-item>
        <el-menu-item index="5-2">修改密码</el-menu-item>
        <el-menu-item index="5-3">退出登录</el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'

export default defineComponent({
  setup() {
    const activeIndex = ref('1')
    const activeIndex2 = ref('1')
    const handleSelect = (key, keyPath) => {
      console.log(key, keyPath)
    }
    return {
      activeIndex,
      activeIndex2,
      handleSelect,
    }
  },
})
</script>

<style scoped>

</style>