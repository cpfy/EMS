<template>
  <div class="bg"></div>
  <div style="height: 111px;">
    <Student_Nav active-index2="3-3"></Student_Nav>
  </div>
  <div style="position: absolute;text-align: center">
    <el-table
        :data="examSchedule.slice(index1,index2)"
        :row-class-name="tableRowClassName"
        height="78vh"
        class="table"
        cell-style="height:60px;;text-align: center"
        header-cell-style="height:75px;text-align: center;font-size:20px"

    >
      <el-table-column prop="num" label="序号" width="120px"/>
      <el-table-column prop="courseId" label="课程编号"/>
      <el-table-column prop="courseName" label="课程名称"/>
      <el-table-column prop="courseCategory" label="课程类别"/>
      <el-table-column prop="courseCollege" label="开课院系"/>
      <el-table-column prop="courseTeacher" label="任课教师"/>
      <el-table-column prop="time" label="考试时间"/>
      <el-table-column prop="location" label="考试地点"/>
    </el-table>
  </div>

  <div style="right: 10vw;bottom: 3vh;position: absolute">
    <el-pagination background layout="prev, pager, next" :total="this.examSchedule.length"
                   v-model:current-page="newPage"
                   page-size=9
                   pager-count=3
                   @current-change="change_page(newPage)">
    </el-pagination>
  </div>
</template>

<script>
import Student_Nav from "../../components/Student_Nav";
import qs from "qs";

export default {
  name: "Student_ExamSchedule",
  components: {
    Student_Nav
  },
  mounted() {
    const self = this;
    self.axios({
      method: 'post',
      url: 'http://localhost:8000/site/info/getExamSchedule/',
      data: qs.stringify({}),
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {
      for (let i = 0; i < res.data.resultList.length; i++) {
        let obj = {};
        obj.num = i;
        obj.courseId = res.data.resultList[i].courseId;
        obj.courseName = res.data.resultList[i].courseName;
        obj.courseCategory = res.data.resultList[i].courseCategory;
        obj.courseCollege = res.data.resultList[i].courseCollege;
        obj.courseTeacher = res.data.resultList[i].courseTeacher;
        obj.time = res.data.resultList[i].time;
        obj.location = res.data.resultList[i].location;
        this.examSchedule.splice(this.examSchedule.length - 1, 0, obj);
      }
    })
  },
  data() {
    return {
      newPage: 1,
      index1: 0,
      index2: 9,
      examSchedule: [
        {
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          time: 'everyDay',
          location: 'nmb nmb',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        },
        {
          num: 1,
          courseId: '#sadl',
          courseName: 'fuckyou',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'van',
          time: 'everyDay',
          location: 'nmb A 101',
        }

      ],

    }
  },
  methods: {
    getCookie(name) {
      var value = ';' + document.cookie;
      var parts = value.split('; ' + name + '=');
      if (parts.length === 2) return parts.pop().split(';').shift();
    },
    change_page(newPage) {
      this.index1 = (newPage - 1) * 9;
      this.index2 = this.index1 + 9;
      console.log(this.index1);
      console.log(this.index2);
    },
    tableRowClassName({ row, rowIndex }) {
      if (row.selected === true) {
        return 'success-row'
      }
      return ''
    },
  }
}
</script>

<style scoped>
.bg {
  background: url("../../assets/homePage/bg_home.png");
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  background-size: 100% 100%;
}

.table {
  margin-left: 5vw;
  margin-top: 7vh;
  width: 90%;
  opacity: 0.7;
  position: fixed;

}

</style>