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
        cell-style="height:60px;text-align: center"
        header-cell-style="height:75px;text-align: center;font-size:20px"
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
      <el-table-column width="80%" prop="credit" label="学分"/>
      <el-table-column prop="time" label="上课时间"/>
      <el-table-column prop="capacity" label="剩余/容量"/>
    </el-table>

  </div>

  <div style="right: 10vw;bottom: 3vh;position: absolute">
    <el-pagination background layout="prev, pager, next" :total="this.courseInfos.length"
                   v-model:current-page="newPage"
                   :page-size=9
                   pager-count=3
                   @current-change="change_page(newPage)">
    </el-pagination>
  </div>

  <div style="position: absolute;left: 6vw;top: 22.8vh;z-index: 56"><p style="color: dimgrey;">隐藏冲突课程</p></div>

  <div style="position: absolute;left: 12vw;top: 24.5vh;z-index: 56">

    <el-switch @change="renew" active-text="Y" inactive-text="N" inline-prompt v-model="filter"
               active-color="#13ce66"></el-switch>
  </div>


</template>

<script>
import Student_Nav from "../../components/Student_Nav";
import qs from "qs";

export default {
  name: "Student_CourseSelect",
  components: {
    Student_Nav
  },
  mounted() {
    console.log("courseSelect " + document.cookie)
    const self = this;
    console.log("filter " + this.filter)
    self.axios({
      method: 'post',
      url: 'http://localhost:8000/site/course/getCourse/',
      data: qs.stringify({'filter': this.filter}),

      withCredentials: true,
      headers: {
        //'Content-Type': 'application/json',
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {

      console.log(res)
      this.courseInfos.splice(0, this.courseInfos.length)
      for (let i = 0; i < res.data.resultList.length; i++) {
        let obj = {};
        obj.num = i+1;
        obj.courseId = res.data.resultList[i].courseId;
        obj.courseName = res.data.resultList[i].courseName;
        obj.courseCategory = res.data.resultList[i].courseCategory;
        obj.courseCollege = res.data.resultList[i].courseCollege;
        obj.courseTeacher = res.data.resultList[i].courseTeacher;
        obj.credit = res.data.resultList[i].credit;
        obj.time = res.data.resultList[i].time;
        obj.capacity = res.data.resultList[i].capacity;
        obj.selected = res.data.resultList[i].selected;
        this.courseInfos.splice(this.courseInfos.length - 1, 0, obj);
      }
    })
  },
  data() {
    return {
      filter: true,
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

    }
  },
  methods: {
    renew() {
      const self = this;
      self.axios({
        method: 'post',
        url: 'http://localhost:8000/site/course/getCourse/',
        data: qs.stringify({
          'filter': this.filter
        }),
        headers: {
          'X-CSRFToken': this.getCookie('csrftoken')
        },
      }).then(res => {
        console.log(res)
        this.courseInfos.splice(0, this.courseInfos.length)
        for (let i = 0; i < res.data.resultList.length; i++) {
          let obj = {};
          obj.num = i+1;
          obj.courseId = res.data.resultList[i].courseId;
          obj.courseName = res.data.resultList[i].courseName;
          obj.courseCategory = res.data.resultList[i].courseCategory;
          obj.courseCollege = res.data.resultList[i].courseCollege;
          obj.courseTeacher = res.data.resultList[i].courseTeacher;
          obj.credit = res.data.resultList[i].credit;
          obj.time = res.data.resultList[i].time;
          obj.capacity = res.data.resultList[i].capacity;
          obj.selected = res.data.resultList[i].selected;
          this.courseInfos.splice(this.courseInfos.length - 1, 0, obj);
        }
      })
    },
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
    tableRowClassName({row, rowIndex}) {
      if (row.selected === true) {
        return 'success-row'
      }
      return ''
    },
    select(index, row) {
      const self = this;
      self.axios({
        method: 'post',
        url: 'http://localhost:8000/site/course/selectCourse/',
        data: qs.stringify({
          'courseId': row.courseId,
        }),
        headers: {
          'X-CSRFToken': this.getCookie('csrftoken')
        },
      }).then(res => {
        if (res.data.result === true) {
          this.courseInfos[index + (this.newPage - 1) * 9].selected = true;
          this.$message({
            type: 'success',
            message: '选课成功'
          })
        } else {
          this.$message({
            type: 'error',
            message: res.data.info,
          })
        }

      })

    }
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

.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-lighter);
}
</style>