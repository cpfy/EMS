<template>
  <div class="bg"></div>
  <div style="height: 111px;">
    <Teacher_Nav active-index2="2-1"></Teacher_Nav>
  </div>

  <div class="table" style="position: absolute" v-bind:style="{zIndex: this.layer}">
    <el-table :data="courseInfo.slice(index1,index2)" style="width: 100%"
              height="78vh"
              cell-style="height:60px;text-align: center"
              header-cell-style="height:75px;text-align: center;font-size:20px"
    >
      <el-table-column label="序号" prop="num"></el-table-column>
      <el-table-column label="课程名称" prop="name"></el-table-column>
      <el-table-column label="课程容量" prop="capacity"></el-table-column>
      <el-table-column label="院系" prop="college"></el-table-column>
      <el-table-column label="课程类别" prop="category"></el-table-column>
      <el-table-column label="学分" prop="credit"></el-table-column>
      <el-table-column label="信息修改">

        <template #default="scope">
          <el-button type="primary" size="medium" @click="handleEdit(scope.$index, scope.row)"
          >修改
          </el-button
          >

          <el-dialog
              v-model="dialogVisible"
              title="修改课程信息"
              width="30%"
              :before-close="beforeClose"
          >
            <div>
              <el-form
                  :model=temp
              >
                <el-form-item label="修改课程名称">
                  <el-input placeholder="修改课程名称" v-model="temp.tempName"
                            style="margin-bottom: 10px; width: 85%"></el-input>
                </el-form-item>
                <el-form-item label="修改课程容量">
                  <el-input placeholder="修改课程容量" v-model="temp.tempCapacity"
                            style="margin-bottom: 10px; width: 85%"></el-input>
                </el-form-item>
                <el-form-item label="修改开课院系">
                  <el-input placeholder="修改开课院系" v-model="temp.tempCollege"
                            style="margin-bottom: 10px; width: 85%"></el-input>
                </el-form-item>
                <el-form-item label="修改课程类型">
                  <el-input placeholder="修改课程类型" v-model="temp.tempCategory"
                            style="margin-bottom: 10px; width: 85%"></el-input>
                </el-form-item>
                <el-form-item label="修改课程学分">
                  <el-input placeholder="修改课程学分" v-model="temp.tempCredit"
                            style="margin-bottom: 10px; width: 85%"></el-input>
                </el-form-item>
              </el-form>

            </div>
            <template #footer>
      <span class="dialog-footer">
        <el-button @click="cancel">Cancel</el-button>
        <el-button type="primary" @click="confirm"
        >Confirm</el-button
        >
      </span>
            </template>

          </el-dialog>

        </template>
      </el-table-column>
    </el-table>
  </div>
  <div style=" zoom: 90%;right: 8vw;bottom: 3vh;position: absolute">
    <el-pagination background layout="prev, pager, next" :total="this.courseInfo.length"
                   v-model:current-page="newPage"
                   :page-size=9
                   pager-count=3
                   @current-change="change_page(newPage)">
    </el-pagination>
  </div>
  <el-button style="position: absolute;left: 7vw;bottom: 3vh" size="small" type="success"
             @click="dialogVisible2 = true">添加新课程
  </el-button>

  <el-dialog
      v-model="dialogVisible2"
      title="添加课程"
      width="30%"
      :before-close="beforeClose"
  >

    <el-form
        :model="temp2"
        :rules="rules"
    >

      <el-form-item label="添加课程名称" prop="tempName">
        <el-input placeholder="课程名称" v-model="temp2.tempName"
                  style="margin-bottom: 10px; width: 85%"></el-input>
      </el-form-item>
      <el-form-item label="添加课程容量" prop="tempCapacity">
        <el-input placeholder="课程容量" v-model="temp2.tempCapacity"
                  v-model.number="numberValidateForm.age" autocomplete="off" type="num"
                  style="margin-bottom: 10px; width: 85%"></el-input>
      </el-form-item>
      <el-form-item label="添加开课院系" prop="tempCollege">
        <el-input placeholder="开课院系" v-model="temp2.tempCollege"
                  style="margin-bottom: 10px; width: 85%"></el-input>
      </el-form-item>
      <el-form-item label="添加课程类型" prop="tempCategory">
        <el-input placeholder="课程类型" v-model="temp2.tempCategory"
                  style="margin-bottom: 10px; width: 85%"></el-input>
      </el-form-item>
      <el-form-item label="添加课程学分" prop="tempCredit">
        <el-input placeholder="课程学分" v-model="temp2.tempCredit"
                  v-model.number="numberValidateForm.age" autocomplete="off" type="num"
                  style="margin-bottom: 10px; width: 85%"></el-input>
      </el-form-item>

    </el-form>

    <template #footer>
      <span class="dialog-footer">
        <el-button @click="cancel">Cancel</el-button>
        <el-button type="primary" @click="confirmAdd"
        >Confirm</el-button
        >
      </span>
    </template>
  </el-dialog>


</template>

<script>
import Teacher_Nav from "../../components/Teacher_Nav";
import qs from "qs";

export default {
  mounted() {
    const self = this;
    self.axios({
      method: 'get',
      url: 'http://localhost:8000/site/t/getCourseDetail/',
      data: qs.stringify({}),
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {
      console.log("setup course")
      console.log(res)
      this.courseInfo.splice(0,this.courseInfo.length)
      for (let i = 0; i < res.data.resultList.length; i++) {
        let obj = {};
        obj.num = i+1;
        obj.id = res.data.resultList[i].id;
        obj.name = res.data.resultList[i].name;
        obj.credit = res.data.resultList[i].credit;
        obj.college = res.data.resultList[i].college;
        obj.capacity = res.data.resultList[i].capacity;
        obj.category = res.data.resultList[i].category;
        this.courseInfo.splice(this.courseInfo.length, 0, obj);
      }

    })
  },
  name: "Teacher_SetupCourse",
  components: {
    Teacher_Nav
  }, data() {
    return {
      numberValidateForm: {
        num: '',
      },
      index: '',
      row: {},
      dialogVisible2: false,
      dialogVisible: false,
      newPage: 1,
      index1: 0,
      index2: 9,
      courseName: '',

      temp: {
        num : '',
        tempName: '',
        tempCategory: '',
        tempCollege: '',
        tempCapacity: '',
        tempCredit: '',
      },
      temp2: {
        num :'',
        tempName: '',
        tempCategory: '',
        tempCollege: '',
        tempCapacity: '',
        tempCredit: '',
      },

      layer: 0,
      courseInfo: [

      ],
      rules: {
        tempName: [
          {required: true, message: '请填写课程名称！', trigger: 'blur'}
        ],
        tempCapacity: [
          {required: true, message: '请填写课程容量！', trigger: 'blur'},
          {type: 'number', message: '容量必须是数字！', trigger: 'blur'}
        ],
        tempCredit: [
          {required: true, message: '请填写课程学分！', trigger: 'blur'},
          {type: 'number', message: '容量必须是数字！', trigger: 'blur'}
        ],
        tempCategory: [
          {required: true, message: '请填写课程类别！', trigger: 'blur'}
        ],
        tempCollege: [
          {required: true, message: '请填写开课学院！', trigger: 'blur'}
        ],
      }
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
    beforeClose() {
      this.temp = {}
      this.temp2 = {}
      this.layer = 0;
      this.dialogVisible = false;
      this.dialogVisible2 = false;
    },
    handleEdit(index, row) {
      this.index = index;
      this.row = row;
      this.layer = 4;
      this.dialogVisible = true;
      console.log(index, row)
    },
    handleDelete(index, row) {
      this.courseInfo.splice(index, 1)
    },
    confirm() {
      let obj = {};
      if (this.temp.tempName) {
        obj.name = this.temp.tempName;
      } else {
        obj.name = this.row.name;
      }
      if (this.temp.tempCollege) {
        obj.college = this.temp.tempCollege;
      } else {
        obj.college = this.row.college;
      }
      if (this.temp.tempCapacity) {
        obj.capacity = this.temp.tempCapacity;
      } else {
        obj.capacity = this.row.capacity;
      }
      if (this.temp.tempCategory) {
        obj.category = this.temp.tempCategory;
      } else {
        obj.category = this.row.category;
      }
      if (this.temp.tempCredit) {
        obj.credit = this.temp.tempCredit;
      } else {
        obj.credit = this.row.credit;
      }
      // alert(obj.credit)
      const self = this;
      self.axios({
        method: 'post',
        url: 'http://localhost:8000/site/t/changeCourseInfo/',
        data: qs.stringify({
          'name': obj.name,
          'college': obj.college,
          'capacity': obj.capacity,
          'category': obj.category,
          'credit': obj.credit,
        }),
        headers: {
          'X-CSRFToken': this.getCookie('csrftoken')
        },
      }).then(res => {
        if (res.data.result === true) {
          this.courseInfo.splice(this.index + (this.newPage - 1) * 9, 1, obj);
          this.$message({
            type: 'success',
            message: '修改成功'
          })
        } else {
          this.$message({
            type: 'error',
            message: res.data.info,
          })
        }

      })

      this.temp = {};
      this.dialogVisible = false;
      this.layer = 0;

    },
    cancel() {

      this.layer = 0;
      this.temp2 = {}
      this.temp = {}
      this.dialogVisible = false;
      this.dialogVisible2 = false;

    },
    confirmAdd() {
      let obj = {
        credit: this.temp2.tempCredit,
        name: this.temp2.tempName,
        capacity: this.temp2.tempCapacity,
        college: this.temp2.tempCollege,
        category: this.temp2.tempCategory,
      }
      const self = this;
      self.axios({
        method: 'post',
        url: 'http://localhost:8000/site/t/addCourse/',
        data: qs.stringify({
          'name': obj.name,
          'college': obj.college,
          'capacity': obj.capacity,
          'category': obj.category,
          'credit': obj.credit,
        }),
        headers: {
          'X-CSRFToken': this.getCookie('csrftoken')
        },
      }).then(res => {
        if (res.data.result === true) {
          this.courseInfo.splice(this.courseInfo.length, 0, obj);
          this.$message({
            type: 'success',
            message: '添加成功'
          })
        } else {
          this.$message({
            type: 'error',
            message: res.data.info,
          })
        }

      })

      this.temp2 = {}
      this.dialogVisible2 = false;
    }
  },
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
  opacity: 0.8;
  position: fixed;

}

</style>