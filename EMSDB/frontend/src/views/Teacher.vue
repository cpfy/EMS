<template>

  <div class="Head">
    <h1>教务管理系统-教师端</h1>
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
          <template #title><img style="height: 28px;margin-right: 8px;" src="../assets/courseManage.png" alt="image failed">
            课程管理
          </template>
          <el-menu-item index="2-1">开设课程</el-menu-item>
          <el-menu-item index="2-2">修改课程信息</el-menu-item>
          <el-menu-item index="2-3">查看选课学生</el-menu-item>
          <el-menu-item index="2-4">学生成绩录入</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title><img style="height: 28px; margin-right: 8px;" src="../assets/information.png" alt="image failed">
            信息查询
          </template>
          <el-menu-item index="3-1">教学任务查询</el-menu-item>
          <el-menu-item index="3-2">空教室查询</el-menu-item>
          <el-menu-item index="3-3">教学课表</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="4">
          <template #title><img style="height: 25px; margin-right: 8px" src="../assets/apply.png" alt="img failed"> 事务申请
          </template>
          <el-menu-item index="4-1">申请请假</el-menu-item>
          <el-menu-item index="4-2">申请修改成绩</el-menu-item>
          <el-menu-item index="4-3">其他申请</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="5">
          <template #title><img style="height: 26px; margin-right: 8px" src="../assets/message.png" alt="img failed"> 消息反馈</template>
          <el-menu-item index="5-1">系统通知</el-menu-item>
          <el-menu-item index="5-2">学生申请</el-menu-item>
        </el-sub-menu>

        <el-sub-menu index="6">
          <template #title><img style="height: 28px;margin-right: 5px;" src="../assets/person.png" alt="img failed"> 个人中心
          </template>
          <el-menu-item index="6-1">个人信息</el-menu-item>
          <el-menu-item index="6-2">修改密码</el-menu-item>
          <el-menu-item index="6-2">退出登录</el-menu-item>
        </el-sub-menu>
    </el-menu>
  </div>

</template>

<script>
import {defineComponent, ref} from 'vue'

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