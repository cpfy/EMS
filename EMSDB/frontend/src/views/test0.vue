<template>
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
                style="margin-bottom: 10px; width: 85%"></el-input>
    </el-form-item>

  </el-form>

</template>

<script>
import {Timer} from '@element-plus/icons-vue'

export default {

  components: {
    Timer,
  },
  data() {
    return {
      temp2: {
        tempName: '',
        tempCategory: '',
        tempCollege: '',
        tempCapacity: '',
        tempCredit: '',
      },
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
    handleEdit(index, row) {
      alert(index)
      this.dialogVisible = true;
      console.log(index, row)
    },
    handleDelete(index, row) {
      this.tableData.splice(index, 1)
    },
    confirm(index, row) {
      if (this.tempName) {
        this.temp.name = this.tempName;
      } else {
        this.temp.name = row.name;
      }
      if (this.tempCollege) {
        this.temp.college = this.tempCollege;
      } else {
        this.temp.college = row.college;
      }
      if (this.tempCapacity) {
        this.temp.capacity = this.tempCapacity;
      } else {
        this.temp.capacity = row.capacity;
      }
      if (this.tempCategory) {
        this.temp.category = this.tempCategory;
      } else {
        this.temp.category = row.category;
      }
      if (this.tempCredit) {
        this.temp.credit = this.tempCredit;
      } else {
        this.temp.credit = row.credit;
      }

      this.tableData.splice(index, 1, this.temp);
      this.tempName = '';
      this.dialogVisible = false;
    },
    cancel() {
      this.tempName = '';
      this.tempCollege = '';
      this.tempCapacity = '';
      this.tempCategory = '';
      this.tempCredit = '';
      this.dialogVisible = false;
    }
  },
}
</script>