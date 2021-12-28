<template>
  <div class="bg"></div>
  <div style="height: 111px">
    <Student_Nav active-index2="2-1"></Student_Nav>
  </div>
  
  <div style="position: absolute;">
    <el-table
        :data="courseInfos.slice(index1,index2)"
        :row-class-name="tableRowClassName"
        height="78vh"
        class="table"
        cell-style="height:60px"
        header-cell-style="height:75px"
    >
      <el-table-column align="center">
        <template #default="scope">
          <el-button v-if="scope.row.selected===false"
                     size="medium"
                     type="primary"
                     @click="select(scope.$index, scope.row)"
          >选课
          </el-button>
          <el-button v-else size="medium" type="default" disabled>
            已选
          </el-button>
        </template>
      </el-table-column>
      <el-table-column prop="num" label="序号" width="120px"/>
      <el-table-column prop="courseId" label="课程编号"/>
      <el-table-column prop="courseName" label="课程名称"/>
      <el-table-column prop="courseCategory" label="课程类别"/>
      <el-table-column prop="courseCollege" label="开课院系"/>
      <el-table-column prop="courseTeacher" label="任课教师"/>
      <el-table-column prop="time" label="上课时间"/>
      <el-table-column prop="capacity" label="剩余/容量"/>
    </el-table>

  </div>

  <div style="right: 10vw;bottom: 3vh;position: absolute">
    <el-pagination background layout="prev, pager, next" :total="this.courseInfos.length"
                   v-model:current-page="newPage"
                   page-size=9
                   pager-count=3
                   @current-change="change_page(newPage)">
    </el-pagination>
  </div>


</template>

<script>
import Student_Nav from "../components/Student_Nav";
import qs from "qs";

export default {
  name: "Student_CourseSelect",
  components: {
    Student_Nav
  },
  /*mounted() {
    const self = this;
    self.axios({
      method: 'post',
      url: '/getCourse/',
      data: qs.stringify({}),
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {
      for (let i = 0; i < res.data.resultList.length; i++) {
        let obj;
        obj.num = i;
        obj.courseId = res.data.resultList[i].courseId;
        obj.courseName = res.data.resultList[i].courseName;
        obj.courseCategory = res.data.resultList[i].courseCategory;
        obj.courseCollege = res.data.resultList[i].courseCollege;
        obj.courseTeacher = res.data.resultList[i].courseTeacher;
        obj.time = res.data.resultList[i].time;
        obj.capacity = res.data.resultList[i].capacity;
        obj.selected = res.data.resultList[i].selected;
        this.resultList.splice(res.data.resultList.length - 1, 0, obj);
      }
    })
  },*/
  data() {
    return {
      newPage: 1,
      index1: 0,
      index2: 9,
      courseInfos: [
        {
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
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
          time: 'everyDay',
          capacity: '0/0',
          selected: false,
        }

      ],
      obj: {
        name: ''
      }
    }
  },
  methods: {
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
    select(index, row) {

      const self = this;
      self.axios({
        method: 'post',
        url: '/selectCourse/',
        data: qs.stringify({
          courseId: row.courseId,
        }),
        headers: {
          'X-CSRFToken': this.getCookie('csrftoken')
        },
      }).then(res => {
        if (res.data.result === 'success') {
          this.courseInfos[index+(this.newPage-1)*9].selected = true;
          this.$message({
            type: 'success',
            message: '选课成功'
          })
        } else {
          this.$message({
            type: 'error',
            message: res.data.result,
          })
        }

      })

    }
  }
}
</script>

<style scoped>
.bg {
  background: url("../assets/homePage/bg_home.png");
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

.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-lighter);
}
</style>