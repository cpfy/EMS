<template>

  <div class="bg"></div>
  <div style="height: 111px;">
    <Teacher_Nav active-index2="2-4"></Teacher_Nav>
  </div >
  <div style="position: absolute;bottom: 3vh;left: 18vw; z-index: 3;">
    <el-button
        size=""
        type="primary"
        @click="download"
    >下载模板
    </el-button>
  </div>
  <div style="position: absolute;top: 14vh;">
    <el-table
        :data="scoreInfos.slice(index1,index2)"
        :row-class-name="tableRowClassName"
        height="76vh"
        class="table"
        cell-style="height:50px;text-align: center"
        header-cell-style="height:75px;text-align: center;font-size:20px"
    >
      <el-table-column prop="num" label="序号" width="120px"/>
      <el-table-column prop="courseId" label="课程编号"/>
      <el-table-column prop="courseName" label="课程名"/>
      <el-table-column prop="scoreRecorded" label="录入状态"/>
      <el-table-column prop="" label="成绩录入">
        <template #default="scope">
          <div>

            <el-upload
                class="upload-demo"
                action="http://localhost:8000/site/t/getCourseOfScore/"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :on-success="handleSuccess"
                :limit="1"
                :auto-upload="true"
                :on-error="handleError"
            >

              <el-button size="small" type="primary" @click="submit(scope.$index,scope.row)">上传文件</el-button>

              <template #tip>
                <div class="el-upload__tip">
                  请按照模板上传文件
                </div>
              </template>
              <!--                <el-button size="small" disabled type="default">选择文件</el-button>-->


            </el-upload>
          </div>
        </template>
      </el-table-column>

    </el-table>
  </div>
  <div style="right: 18vw;bottom: 3vh;position: absolute;zoom: 1.1;">
    <el-pagination background layout="prev, pager, next" :total="this.scoreInfos.length"
                   v-model:current-page="newPage"
                   :page-size=6
                   pager-count=3
                   @current-change="change_page(newPage)">
    </el-pagination>
  </div>
</template>

<script>
import Teacher_Nav from "../components/Teacher_Nav";
import qs from "qs";

export default {
  name: "ScoreRecord", components: {
    Teacher_Nav
  },
  mounted() {
    const self = this;
    self.axios({
      method: 'post',
      url: 'http://localhost:8000/site/t/getCourseOfScore/',
      data: qs.stringify({}),
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {
      this.scoreInfos = res.data.scoreInfos;
    })
  },
  data() {
    return {
      newPage: 1,
      index1: 0,
      index2: 6,
      result: '',
      info:'',
      rowNum: '',
      scoreInfos: [

        {
          num: 0,
          courseId: '#22222',
          courseName: 'database22',
          scoreRecorded: '已录入',
        },{
          num: 0,
          courseId: '#22',
          courseName: 'database',
          scoreRecorded: '未录入',
        },{
          num: 0,
          courseId: '#22',
          courseName: 'database',
          scoreRecorded: '未录入',
        },{
          num: 0,
          courseId: '#22',
          courseName: 'database',
          scoreRecorded: '未录入',
        },
        {
          num: 0,
          courseId: '#22',
          courseName: 'database',
          scoreRecorded: '未录入',
        },
        {
          num: 0,
          courseId: '#22222',
          courseName: 'database22',
          scoreRecorded: '已录入',
        },
        {
          num: 0,
          courseId: '#22222',
          courseName: 'database22',
          scoreRecorded: '已录入',
        },
        {
          num: 0,
          courseId: '#22222',
          courseName: 'database22',
          scoreRecorded: '已录入',
        }
      ],
      fileList: [],
    }
  },
  methods: {
    download() {
      const a = document.createElement('a')
      a.setAttribute('download', "成绩模板")
      a.setAttribute('href', "./template.xlsx")
      a.click()
    },
    getCookie(name) {
      var value = ';' + document.cookie;
      var parts = value.split('; ' + name + '=');
      if (parts.length === 2) return parts.pop().split(';').shift();
    },
    change_page(newPage) {
      this.index1 = (newPage - 1) * 6;
      this.index2 = this.index1 + 6;
      console.log(this.index1);
      console.log(this.index2);
    },
    tableRowClassName({row, rowIndex}) {
      if (row.scoreRecorded === '已录入') {
        return 'success-row'
      }
      return 'success-row'
    },
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    },


    handleSuccess() {

      if (this.result === true) {
        this.$message({
          type: 'success',
          message: '上传成功',
        })
        this.scoreInfos[this.rowNum].scoreRecorded = '已录入'
      } else {
        this.$message({
          type: 'error',
          message: this.info,
        })
      }

    },


    submit(index, row) {

      const self = this;
      self.axios({
        method: 'post',
        url: 'http://localhost:8000/site/t/importGrade/',
        data: qs.stringify({
          'courseId': row.courseId,
        }),
        headers: {
          'X-CSRFToken': this.getCookie('csrftoken')
        },
      }) .then(res => {
        this.rowNum = index;
        this.result = res.data.result;
        this.info = res.data.info;
      })
    },


    handleError(err, file, fileList) {
      console.log(err);
      console.log(file)
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
  margin-left: 17vw;
  margin-top: 8vh;
  width: 65%;
  opacity: 0.8;
  position: fixed;

}

.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-lighter);
}
</style>