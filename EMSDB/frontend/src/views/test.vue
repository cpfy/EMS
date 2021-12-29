<template>
  <div class="bg"></div>
  <div style="height: 111px">
    <Student_Nav active-index2="2-1"></Student_Nav>
  </div>

  <div class="demo-collapse;" style="position: absolute;width: 85vw;left:7vw;top:20vh">
    <el-collapse v-model="activeName" accordion>
      <el-collapse-item title="Consistency" name="1">
        <div>
          <el-table
              :data="studentInfos.slice(index1,index2)"
              :row-class-name="tableRowClassName"

              class="table"
              cell-style="height:30px;text-align: center"
              header-cell-style="height:75px;text-align: center;font-size:20px"
          >

            <el-table-column prop="num" label="序号" width="120px"/>
            <el-table-column prop="courseId" label="课程编号"/>
            <el-table-column prop="courseName" label="课程名称"/>
            <el-table-column prop="courseCategory" label="课程类别"/>
            <el-table-column prop="courseCollege" label="开课院系"/>
            <el-table-column prop="courseTeacher" label="任课教师"/>
            <el-table-column width="80%" prop="credit" label="学分"/>
            <el-table-column prop="time" label="上课时间"/>
            <el-table-column prop="capacity" label="剩余/容量"/>
          </el-table>
          <div style="right: 10vw;bottom: 1vh;position: fixed">
            <el-pagination background layout="prev, pager, next" :total="this.studentInfos.length"
                           v-model:current-page="newPage"
                           page-size=9
                           pager-count=3
                           @current-change="change_page(newPage)">
            </el-pagination>
          </div>
        </div>

      </el-collapse-item>

      <el-collapse-item title="Feedback" name="2">

        <div>
          <el-table
              :data="studentInfos.slice(index1,index2)"
              :row-class-name="tableRowClassName"
              class="table"
              cell-style="height:30px;text-align: center"
              header-cell-style="height:75px;text-align: center;font-size:20px"
          >
            <el-table-column prop="num" label="序号" width="120px"/>
            <el-table-column prop="courseId" label="课程编号"/>
            <el-table-column prop="courseName" label="课程名称"/>
            <el-table-column prop="courseCategory" label="课程类别"/>
            <el-table-column prop="courseCollege" label="开课院系"/>
            <el-table-column prop="courseTeacher" label="任课教师"/>
            <el-table-column width="80%" prop="credit" label="学分"/>
            <el-table-column prop="time" label="上课时间"/>
            <el-table-column prop="capacity" label="剩余/容量"/>
          </el-table>
        </div>
        <div style="right: 10vw;bottom: 1vh;position: fixed">
          <el-pagination background layout="prev, pager, next" :total="this.studentInfos.length"
                         v-model:current-page="newPage"
                         page-size=9
                         pager-count=3
                         @current-change="change_page(newPage)">
          </el-pagination>
        </div>
      </el-collapse-item>
      <el-collapse-item title="Efficiency" name="3">
        <div>
          <el-table
              :data="studentInfos.slice(index1,index2)"
              :row-class-name="tableRowClassName"
              class="table"
              cell-style="height:30px;text-align: center"
              header-cell-style="height:75px;text-align: center;font-size:20px"
          >
            <el-table-column prop="num" label="序号" width="120px"/>
            <el-table-column prop="courseId" label="课程编号"/>
            <el-table-column prop="courseName" label="课程名称"/>
            <el-table-column prop="courseCategory" label="课程类别"/>
            <el-table-column prop="courseCollege" label="开课院系"/>
            <el-table-column prop="courseTeacher" label="任课教师"/>
            <el-table-column width="80%" prop="credit" label="学分"/>
            <el-table-column prop="time" label="上课时间"/>
            <el-table-column prop="capacity" label="剩余/容量"/>
          </el-table>
        </div>
        <div style="right: 10vw;bottom: 0;position: fixed;zoom:80%">
          <el-pagination background layout="prev, pager, next" :total="this.studentInfos.length"
                         v-model:current-page="newPage"
                         page-size=9
                         pager-count=3
                         @current-change="change_page(newPage)">
          </el-pagination>
        </div>
      </el-collapse-item>

    </el-collapse>
  </div>


</template>

<script>
import Student_Nav from "../components/Student_Nav";

export default {
  components: {
    Student_Nav
  },
  data() {

    return {
      activeName: '',
      newPage: 1,
      index1: 0,
      index2: 9,
      itemNum: 9,
      studentInfos: [
        {
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          credit: 1.5,
          time: 'everyDay',
          capacity: '1/8',
          selected: true,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          credit: 1.5,
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        }

      ],
      courseInfos: [
           1,2,3,4
      ],

    }
  },
  methods: {
    change_page(newPage) {
      this.index1 = (newPage - 1) * this.itemNum;
      this.index2 = this.index1 + this.itemNum;
      console.log(this.index1);
      console.log(this.index2);
    },
  }
}
</script>

<style>
.el-table .warning-row {
  --el-table-tr-bg-color: var(--el-color-warning-lighter);
}

.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-lighter);
}
.bg {
  background: url("../assets/homePage/bg_home.png");
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  background-size: 100% 100%;
}

</style>