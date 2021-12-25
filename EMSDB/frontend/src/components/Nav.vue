
<template>
  <div class="overall">
    <div class="tab-box">
<!--      <span-->
<!--          v-for="(i,index) in list"-->
<!--          :key="index"-->
<!--          :class="defaultIndex===index?'active':''"-->
<!--          @click="defaultIndex=index"-->
<!--      >-->
<!--        <div class="dot"></div>-->
<!--        {{list[index]}}-->
<!--      </span>-->

<!--      <div class="bar-box">-->
<!--        <div class="bar"></div>-->
<!--      </div>-->
      <div  v-for="(i,index) in list"
            :key="index"
            :class="defaultIndex===index?'active':''"
            @click="defaultIndex=index">
        <el-dropdown>
          <el-button type="primary">
            Dropdown List<el-icon class="el-icon--right"></el-icon>
          </el-button>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item>Action 1</el-dropdown-item>
              <el-dropdown-item>Action 2</el-dropdown-item>
              <el-dropdown-item>Action 3</el-dropdown-item>
              <el-dropdown-item>Action 4</el-dropdown-item>
              <el-dropdown-item>Action 5</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </div>
    <svg style="width: 0; height: 0;">
      <defs>
        <filter id="goo">
          <feGaussianBlur in="SourceGraphic" result="blur" stdDeviation="4" />
          <feColorMatrix
              in="blur"
              mode="matrix"
              values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7"
              result="goo"
          />
          <feBlend in2="goo" in="SourceGraphic" result="mix" />
        </filter>
      </defs>
    </svg>
  </div>




</template>

<script>
export default {
  name : 'Nav',
  props: {
    msg: {
      type: String
    }
  },
  data() {
    return {
      defaultIndex: 1,
      list:['A','B','C','D','E']
    };
  },
};
</script>

<style  scoped>

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

</style>