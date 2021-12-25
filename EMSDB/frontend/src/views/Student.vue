
<template>
  <div class="Head">
    <h1>教务管理系统-学生端</h1>
  </div>
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
      <template #title><img style="height: 30px;margin-right: 5px" src="../assets/courseSelect.png" alt="image failed">学生选课</template>
      <el-menu-item index="2-1">课程选择</el-menu-item>
      <el-menu-item index="2-2">退选课程</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="3">
      <template #title><img style="height: 28px; margin-right: 8px;" src="../assets/information.png" alt="image failed">信息查询</template>
      <el-menu-item index="3-1">推荐课表查询</el-menu-item>
      <el-menu-item index="3-2">个人课表</el-menu-item>
      <el-menu-item index="3-3">考表查询</el-menu-item>
      <el-menu-item index="3-4">空教室查询</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="4">
      <template #title><img style="height: 25px; margin-right: 8px" src="../assets/apply.png" alt="img failed"> 事务申请</template>
      <el-menu-item index="4-1">申请免听课程</el-menu-item>
      <el-menu-item index="4-2">申请免修课程</el-menu-item>
      <el-menu-item index="4-3">申请缓考</el-menu-item>
      <el-menu-item index="4-4">其他申请</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="5">
      <template #title><img style="height: 26px; margin-right: 8px" src="../assets/message.png" alt="img failed"> 消息反馈</template>
      <el-menu-item index="5-1">系统通知</el-menu-item>
      <el-menu-item index="5-2">教师反馈</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="6"><img style="height: 28px;margin-right: 10px;" src="../assets/teachingEva.png" alt="img failed"> 教学评价</el-menu-item>
    <el-sub-menu index="7">
      <template #title><img style="height: 28px;margin-right: 5px;" src="../assets/person.png" alt="img failed"> 个人中心</template>
      <el-menu-item index="7-1">个人信息</el-menu-item>
      <el-menu-item index="7-2">修改密码</el-menu-item>
      <el-menu-item index="7-3">退出登录</el-menu-item>
    </el-sub-menu>
  </el-menu>




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
.Head {

}





/*

.tab_item {
  height: 50px;
}

.el-dropdown {
  vertical-align: top;
}
.el-dropdown + .el-dropdown {
  margin-left: 15px;
}
.el-icon-arrow-down {
  font-size: 12px;
}

.tab-box {
  box-shadow: 0 0 5px #ccc;
  width: 100%;
  height: 50px;
  background: #0084ff;
  border-radius: 2px;
  display: flex;
  position: relative;
  z-index: 99;
}

.tab-box span {
  display: block;
  flex-grow: 1;
  line-height: 50px;
  font-weight: bold;
  cursor: pointer;
  position: relative;
  transition: 0.5s ease;
  user-select: none;
  color: white;
  border-bottom: 3px solid transparent;
}

.tab-box span .dot {
  display: inline-block;
  width: 30px;
  height: 10px;
  -webkit-filter: url("#goo");
  filter: url("#goo");
  position: absolute;
  background: #0084ff;
  left: calc(50% - 15px);
  top: 1px;
}

.tab-box span .dot::after {
  content: "";
  position: absolute;
  left: calc(50% - 6px);
  width: 12px;
  height: 12px;
  display: block;
  background: #0084ff;
  border-radius: 50%;
}

.active {
  height: 20%;
  text-shadow: 0 0 10px white;
  border-bottom: 3px solid white !important;
}

.active .dot::after {
  animation: gooey 1s both 1 ease;
}

@keyframes gooey {
  50% {
    transform: translateY(-30px) scaleX(0.8);
  }
}

.tab-box span:hover {
  text-shadow: 0 0 10px white;
}

.tab-box span:nth-of-type(1):hover + * + * + * + * + .bar-box .bar {
  left: 0;
}

.tab-box span:nth-of-type(2):hover + * + * + * + .bar-box .bar {
  left: 20%;
}

.tab-box span:nth-of-type(3):hover + * + * + .bar-box .bar {
  left: 40%;
}

.tab-box span:nth-of-type(4):hover + * + .bar-box .bar {
  left: 60%;
}

.tab-box span:nth-of-type(5):hover + .bar-box .bar {
  left: 80%;
}

.bar-box {
  width: 100%;
  height: 100%;
  border-radius: 2px;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}

.tab-box .bar {
  width: 20%;
  height: 3px;
  position: absolute;
  left: -20%;
  bottom: 0;
  background: white;
  transition: 0.5s ease;
  opacity: 0.9;
}
*/

</style>