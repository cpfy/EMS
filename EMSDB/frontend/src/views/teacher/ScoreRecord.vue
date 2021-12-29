<template>
  <div class="bg"></div>
  <div style="height: 111px;">
    <Teacher_Nav active-index2="2-4"></Teacher_Nav>
  </div>
  <div style="position: absolute;top: 14vh;">
    <div>

    </div>
    <el-table
        :data="scoreInfos.slice(index1,index2)"
        :row-class-name="tableRowClassName"
        height="78vh"
        class="table"
        cell-style="height:50px;text-align: center"
        header-cell-style="height:75px;text-align: center;font-size:20px"
    >
      <el-table-column prop="num" label="序号" width="120px"/>
      <el-table-column prop="courseId" label="课程编号"/>
      <el-table-column prop="courseName" label="课程名"/>
      <el-table-column prop="recorded" label="录入状态"/>
      <el-table-column prop="" label="成绩录入">
        <template #default="scope">
          <div>
            <el-upload
                class="upload-demo"
                action="http://localhost:8000/site/login/"
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

      <!--
            <el-table-column label="确认录入">
              <template #default="scope">
                <div v-if="scope.row.recorded === '未录入'">
                  <el-button size="medium" type="success" @click="confirmUpload(scope.$index, scope.row)">确认上传</el-button>
                </div>

                <div v-else>
                  <el-button size="medium" type="default" disabled>已录入</el-button>
                </div>
              </template>
            </el-table-column>-->

    </el-table>
  </div>
</template>

<script>
import Teacher_Nav from "../../components/Teacher_Nav";
import qs from "qs";

export default {
  name: "ScoreRecord", components: {
    Teacher_Nav
  },
  data() {
    return {
      newPage: 1,
      index1: 0,
      index2: 9,
      scoreInfos: [
        {
          num: 0,
          courseId: '#22',
          courseName: 'database',
          recorded: '未录入',
        },
        {
          num: 0,
          courseId: '#22222',
          courseName: 'database22',
          recorded: '已录入',
        },
        {
          num: 0,
          courseId: '#22',
          courseName: 'database',
          recorded: '未录入',
        },
        {
          num: 0,
          courseId: '#22',
          courseName: 'database',
          recorded: '未录入',
        }
      ],
      fileList: [],
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
      if (row.recorded === '已录入') {
        return 'success-row'
      }
      return ''
    },
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    },
    handleSuccess(index,row) {
      this.$message({
        type: 'success',
        message: '评价成功',
      })
      /* const self = this;
       self.axios({
         method: 'post',
         url: '/scoreRecord/',
         data: qs.stringify({
           'courseId': row.courseId,
         }),
         headers: {
           'X-CSRFToken': this.getCookie('csrftoken')
         },
       }).then(res => {
         if (res.data.result === 'success') {
           this.scoreInfos[index + (this.newPage - 1) * 9].recorded = true;
           this.$message({
             type: 'success',
             message: '评价成功',
           })
           row.evaluated = '已评价'
         } else {
           this.$message({
             type: 'error',
             message: res.data.result,
           })
         }

       })*/
    },
    submit(index, row) {

    },
    handleError() {
      this.$message({
        type: 'success',
        message: '评价成功',
      })}
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