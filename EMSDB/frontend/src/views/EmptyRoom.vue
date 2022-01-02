<template>
  <div class="bg">
  </div>
  <div v-if="this.$store.state.userType==='学生'" style="height: 111px;">
    <Student_Nav active-index2="3-4"></Student_Nav>
  </div>
  <div v-else-if="this.$store.state.userType==='教师'" style="height: 111px;">
    <Teacher_Nav active-index2="3-2"></Teacher_Nav>
  </div>

  <div style="position: absolute;top: 20.5vh;opacity: 0.7;left: 8.5vw">
    <el-date-picker
        @change="renew"
        v-model="date"
        type="date"
        placeholder="选择要查询的日期"
        style="width: 75%"
    ></el-date-picker>
  </div>

  <div>
    <el-table
        :data="roomInfo.slice(index1,index2)"
        border
        ref="filterTable"
        style="width: 80%; margin-top: 12vh;margin-left: 8vw;opacity: 0.75;"

        header-cell-style="height:7.5vh;background-color:lightsteelblue;color:white;text-align:center;font-size:20px;font-weight:inherit;opacity:0.9"
        cell-style="height:6.8vh;width:6vw;text-align:center;font-size:16px"
    >

      <el-table-column class-name="rowClass" prop="room" label='教室'
                       column-key="time" width="150px"
      />
      <el-table-column class-name="cel" prop='c[0]' label="1节"/>
      <el-table-column prop='c[1]' label="2节"/>
      <el-table-column prop='c[2]' label="3节"/>
      <el-table-column prop='c[3]' label="4节"/>
      <el-table-column prop='c[4]' label="5节"/>
      <el-table-column prop='c[5]' label="6节"/>
      <el-table-column prop='c[6]' label="7节"/>
      <el-table-column prop='c[7]' label="8节"/>
      <el-table-column prop='c[8]' label="9节"/>
      <el-table-column prop='c[9]' label="10节"/>
      <el-table-column prop='c[10]' label="11节"/>
      <el-table-column prop='c[11]' label="12节"/>
    </el-table>

  </div>

  <div style="right: 12vw;bottom: 1vh;position: absolute;opacity: 0.8;">
    <el-pagination background layout="prev, pager, next" :total="this.roomInfo.length"
                   v-model:current-page="newPage"
                   page-size=9
                   pager-count=3
                   @current-change="change_page(newPage)">
    </el-pagination>
  </div>

</template>

<script>
import Student_Nav from "../components/Student_Nav";
import Teacher_Nav from "../components/Teacher_Nav";
import qs from "qs";
export default {
  name: "EmptyRoom",
  components: {
    Student_Nav,
    Teacher_Nav
  },
  data() {

    return {
      date: '',
      newPage: 1,
      index1: 0,
      index2: 9,
      roomInfo: [
        {
          room :'nmb A 101',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb B 201',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb B 201',
          c :  ['空闲','空闲','空闲','占用','空闲','占用','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb B 309',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb B 201',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb B 201',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb B 201',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb B 201',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb B 201',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb C 201',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        },
        {
          room :'nmb B 201',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        }
        ,
        {
          room :'nmb B 201',
          c :  ['空闲','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲','占用','空闲','空闲'],
        }
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
      this.index1 = (newPage - 1) * 9;
      this.index2 = this.index1 + 9;
      console.log(this.index1);
      console.log(this.index2);
    },
    renew() {
      const self = this;
      self.axios({
        method: 'post',
        url: 'http://localhost:8000/site/info/getEmptyRoom/',
        data: qs.stringify({
          'date' : this.date,
        }),
        headers: {
          'X-CSRFToken': this.getCookie('csrftoken')
        },
      }).then(res => {

        console.log(res)
      this.roomInfo.splice(0, this.roomInfo.length);
      for (let i = 0; i < res.data.roomInfo.length; i++) {
        let obj = {};
        obj.room = res.data.roomInfo[i].room;
        obj.Monday = res.data.roomInfo[i].Monday;
        obj.Tuesday = res.data.roomInfo[i].Tuesday;
        obj.Wednesday = res.data.roomInfo[i].Wednesday;
        obj.Thursday = res.data.roomInfo[i].Thursday;
        obj.Friday = res.data.roomInfo[i].Friday;
        obj.Saturday = res.data.roomInfo[i].Saturday;
        obj.Sunday = res.data.roomInfo[i].Sunday;
        this.roomInfo.splice(this.roomInfo.length, 0, obj);
      }

        this.roomInfo = res.data.roomInfo;
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

</style>