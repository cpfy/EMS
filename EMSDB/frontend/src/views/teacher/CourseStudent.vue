<template>
  <div class="bg"></div>
  <div style="height: 111px;">
    <Teacher_Nav active-index2="2-3"></Teacher_Nav>
  </div>

  <div  style="position: absolute;top: 20.5vh;opacity: 0.7;left: 6vw">
    <el-select @change="renew" v-model="id" placeholder="选择课程">
      <el-option
          v-for="item in courseInfo"
          :key="item.courseId"
          :label="item.courseName"
          :value="item.courseId"
      >
      </el-option>
    </el-select>
  </div>

  <div>
      <el-table
          :data="studentInfo.slice(index1,index2)"
          :row-class-name="tableRowClassName"
          height="73.5vh"
          class="table"
          cell-style="height:52px;text-align: center"
          header-cell-style="height:75px;text-align: center;font-size:20px"
      >

      <el-table-column prop="num" label='序号'/>
      <el-table-column prop='studentName' label="学生姓名"/>
      <el-table-column prop='studentId' label="学号"/>
      <el-table-column prop='class' label="班级"/>
      <el-table-column prop='grade' label="年纪"/>
      <el-table-column prop='college' label="学院"/>
      <el-table-column prop='email' label="邮箱"/>
    </el-table>

  </div>

  <div style="zoom:96%;right: 5vw;bottom: 0.6vh;position: absolute;opacity: 0.8;">
    <el-pagination background layout="prev, pager, next" :total="this.studentInfo.length"
                   v-model:current-page="newPage"
                   page-size=9
                   pager-count=3
                   @current-change="change_page(newPage)">
    </el-pagination>
  </div>

</template>

<script>
import Teacher_Nav from "../../components/Teacher_Nav";
import qs from "qs";

export default {
  mounted() {
    const self = this;
    self.axios({
      method: 'post',
      url: 'http://localhost:8000/site/t/getCourse/',
      data: qs.stringify({
      }),
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {

      this.courseInfo.splice(0, this.courseInfo.length);
      for (let i = 0; i < res.data.courseInfo.length; i++) {
        let obj = {};
        obj.courseId = res.data.courseInfo[i].courseId;
        obj.courseName = res.data.courseInfo[i].courseName;
        this.courseInfo.splice(this.courseInfo.length, 0, obj);
      }
    })
  },
  name: "CourseStudent",
  components: {
    Teacher_Nav
  }, data() {

    return {
      id: '',
      date: '',
      newPage: 1,
      index1: 0,
      index2: 10,
      courseInfo: [
        {
          courseId: '#23012',
          courseName: 'compile'
        },
        {
          courseId: '#88997',
          courseName: 'database'
        },
        {
          courseId: '#887',
          courseName: 'database'
        },
        {
          courseId: '#897',
          courseName: 'database'
        },
        {
          courseId: '#8997',
          courseName: 'database'
        },
        {
          courseId: '#8899',
          courseName: 'database'
        }
      ],
      /*studentInfo: [
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        },
        {
          num: 1,
          studentId: '30',
          studentName: 'sb',
          class: '3',
          grade: '19',
          college: 'computer',
          email: '11@qq.com'
        },
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        },
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        },
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        },
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        },
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        },
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        },
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        },
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        },
        {
          num: 0,
          studentId: '333',
          studentName: '22',
          class: '3',
          grade: '19',
          college: 'sea',
          email: '666@qq.com'
        }
      ],*/
      studentInfo: [
        {
          num: '--',
          studentId: '--',
          studentName: '--',
          class: '--',
          grade: '--',
          college: '--',
          email: '--'
        },
      ]
    }
  },
  methods: {
    getCookie(name) {
      var value = ';' + document.cookie;
      var parts = value.split('; ' + name + '=');
      if (parts.length === 2) return parts.pop().split(';').shift();
    },
    change_page(newPage) {
      this.index1 = (newPage - 1) * 10;
      this.index2 = this.index1 + 10;
      console.log(this.index1);
      console.log(this.index2);
    },
    renew() {
      const self = this;
      self.axios({
        method: 'post',
        url: 'http://localhost:8000/site/t/getStudentInfo/',
        data: {
          'courseId': this.id,
        },
        headers: {
          'X-CSRFToken': this.getCookie('csrftoken')
        },
      }).then(res => {
       this.studentInfo.splice(0, this.studentInfo.length);
      for (let i = 0; i < res.data.studentInfo.length; i++) {
        let obj = {};
        obj.num = i;
        obj.studentId = res.data.studentInfo[i].studentId;
        obj.studentName = res.data.studentInfo[i].studentName;
        obj.class = res.data.studentInfo[i].class;
        obj.grade = res.data.studentInfo[i].grade;
        obj.college = res.data.studentInfo[i].college;
        obj.email = res.data.studentInfo[i].email;
        this.studentInfo.splice(this.studentInfo.length, 0, obj);
      }

        //TODO: splice?
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
  margin-top: 12vh;
  width: 90%;
  opacity: 0.7;
  position: fixed;

}

</style>