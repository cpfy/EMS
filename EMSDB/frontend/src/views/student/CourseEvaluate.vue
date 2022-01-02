<template>
  <div class="bg"></div>
  <div style="height: 111px;position: absolute">
    <Student_Nav active-index2="6"></Student_Nav>
  </div>
  <div style="position: absolute;top: 14vh;">
    <el-table
        :data="courseInfos.slice(index1,index2)"
        :row-class-name="tableRowClassName"
        height="78vh"
        class="table"
        cell-style="height:60px;text-align: center"
        header-cell-style="height:75px;text-align: center;font-size:20px"
    >
      <!--      <el-table-column align="center">
              <template #default="scope">
                <el-button size="medium"
                           type="primary"
                           @click="drop(scope.$index, scope.row)"
                >退选
                </el-button>
              </template>
            </el-table-column>-->
      <el-table-column prop="num" label="序号" width="120px"/>
      <el-table-column prop="courseName" label="课程名称"/>
      <el-table-column prop="courseTeacher" label="任课教师"/>
      <el-table-column prop="courseId" label="课程编号"/>
      <el-table-column prop="courseCategory" label="课程类别"/>
      <el-table-column width="80%" prop="credit" label="学分"/>
      <el-table-column prop="courseCollege" label="开课院系"/>
      <el-table-column prop="evaluated" label="评价状态"/>
      <el-table-column label="评价">
        <template #default="scope">
          <div v-if="scope.row.evaluated==='未评价'">
            <el-rate v-model="courseInfos[scope.$index+(this.newPage-1)*9].mark" allow-half/>
          </div>
          <div v-else>
            <el-rate v-model="courseInfos[scope.$index+(this.newPage-1)*9].mark" disabled/>
          </div>

          <!--          <el-dialog
                      v-model="dialogVisible"
                      title="提示"
                      width="30%"
                  >
                    <span>当前所选评分数为{{courseInfos[scope.$index].mark}}，是否继续</span>
                    <template #footer>
                <span class="dialog-footer">
                  <el-button type="primary" @click="confirmEvaluate">确定</el-button>
                  <el-button @click="cancel">取消</el-button>
                </span>
                    </template>
                  </el-dialog>-->
          <!--TODO: add a dialog-->
        </template>
      </el-table-column>


      <el-table-column label="确认评价">
        <template #default="scope">
          <div v-if="scope.row.evaluated === '未评价'">
            <el-button size="medium" type="primary" @click="confirm(scope.$index, scope.row)">确认</el-button>
          </div>

          <div v-else>
            <el-button size="medium" type="default" disabled @click="confirm(scope.$index, scope.row)">已评价</el-button>
          </div>
        </template>
      </el-table-column>

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
import Student_Nav from "../../components/Student_Nav";
import qs from "qs";

export default {
  name: "CourseEvaluate",
  components: {
    Student_Nav
  },
  mounted() {
    const self = this;
    self.axios({
      method: 'post',
      url: 'http://localhost:8000/site/eva/getEvaInfo/',
      data: qs.stringify({}),
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {
      this.courseInfos.splice(0,this.courseInfos.length)
      for (let i = 0; i < res.data.resultList.length; i++) {
        this.courseInfos.splice(0,this.courseInfos.length , obj);
        let obj = {};
        obj.num = i;
        obj.courseId = res.data.resultList[i].courseId;
        obj.courseName = res.data.resultList[i].courseName;
        obj.courseCategory = res.data.resultList[i].courseCategory;
        obj.courseCategory = res.data.resultList[i].courseCategory;
        obj.mark = res.data.resultList[i].mark;
        obj.credit = res.data.resultList[i].credit;
        obj.courseTeacher = res.data.resultList[i].courseTeacher;
        obj.evaluated = res.data.resultList[i].evaluated;
        this.courseInfos.splice(this.courseInfos.length, 0, obj);
      }
    })
  },
  data() {
    return {
      dialogVisible: false,
      newPage: 1,
      index1: 0,
      index2: 9,

      courseInfos: [
        {
          mark: 5,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '已评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
        },
        {
          mark: 0,
          num: 1,
          courseId: '#ssssssssssssss',
          courseName: 'fuckme',
          courseCategory: 'sex',
          credit: 1.5,
          courseCollege: 'sexCollege',
          courseTeacher: 'JohnCena',
          evaluated: '未评价',
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
    tableRowClassName({row, rowIndex}) {
      if (row.evaluated === '已评价') {
        return 'success-row'
      }
      return ''
    },
    confirm(index, row) {
      if (row.mark !== 0) {

        const self = this;
        self.axios({
          method: 'post',
          url: 'http://localhost:8000/site/eva/evaluateCourse/',
          data: qs.stringify({
            'courseId': row.courseId,
            'mark': row.mark,
          }),
          headers: {
            'X-CSRFToken': this.getCookie('csrftoken')
          },
        }).then(res => {
          if (res.data.result === true) {
            this.courseInfos[index + (this.newPage - 1) * 9].selected = true;
            this.$message({
              type: 'success',
              message: '评价成功',
            })
            row.evaluated = '已评价'
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