<template>
  <div class="bg"></div>
  <div style="height: 111px;">
    <Teacher_Nav active-index2="3-3"></Teacher_Nav>
  </div>
  <div style="width: 90vw;margin-left: 5vw;margin-top: 7vh;">
    <Schedule :total-data="scheduleData" ></Schedule>
  </div>
</template>

<script>
import Schedule from "../../components/Schedule";
import Teacher_Nav from "../../components/Teacher_Nav";
import qs from "qs";

export default {
  mounted() {
    const self = this;
    self.axios({
      method: 'get',
      url: 'http://localhost:8000/site/info/Teacher_Schedule/',
      data: qs.stringify({
      }),
      headers: {
        'X-CSRFToken': this.getCookie('csrftoken')
      },
    }).then(res => {
      console.log(res)
      this.scheduleData.splice(0, this.scheduleData.length);
      for (let i = 0; i < res.data.schedule.length; i++) {
        let obj = [];
        obj = res.data.schedule[i];
        // obj.num = i;
        // obj.time = res.data.schedule[i].time;
        // obj.Monday = res.data.schedule[i].Monday;
        // obj.Tuesday = res.data.schedule[i].Tuesday;
        // obj.Wednesday = res.data.schedule[i].Wednesday;
        // obj.Thursday = res.data.schedule[i].Thursday;
        // obj.Friday = res.data.schedule[i].Friday;
        // obj.Saturday = res.data.schedule[i].Saturday;
        // obj.Sunday = res.data.schedule[i].Sunday;
        this.scheduleData.splice(this.scheduleData.length, 0, obj);
      }
    })
  },
  name: "Teacher_Schedule",
  components: {
    Schedule,
    Teacher_Nav
  },
  data() {
    return {
      scheduleData:[ [
        {
          time: '1,2节',
          Monday: '编译技术 锌小子 (一)215',
          Tuesday: '',
          Wednesday: '3',
          Thursday: '4',
          Friday: '数据库系统原理 铑小子 新主楼M-101',
          Saturday: '6',
          Sunday: '7'
        },
        {
          time: '3,4节',
          Monday: '1',
          Tuesday: '2',
          Wednesday: '3',
          Thursday: '4',
          Friday: '5',
          Saturday: '6',
          Sunday: '7'
        },
        {
          time: '5,6节',
          Monday: '1',
          Tuesday: '2',
          Wednesday: '3',
          Thursday: '4',
          Friday: '5',
          Saturday: '6',
          Sunday: '7'
        },
        {
          time: '7,8节',
          Monday: '1',
          Tuesday: '2',
          Wednesday: '3',
          Thursday: '4',
          Friday: '5',
          Saturday: '6',
          Sunday: '7'
        },
        {
          time: '9,10节',
          Monday: '1',
          Tuesday: '2',
          Wednesday: '3',
          Thursday: '4',
          Friday: '5',
          Saturday: '6',
          Sunday: '7'
        },
        {
          time: '11,12节',
          Monday: '1',
          Tuesday: '2',
          Wednesday: '3',
          Thursday: '4',
          Friday: '5',
          Saturday: '6',
          Sunday: '7'
        },
      ],]
    }
  },
  methods: {
    getCookie(name) {
      var value = ';' + document.cookie;
      var parts = value.split('; ' + name + '=');
      if (parts.length === 2) return parts.pop().split(';').shift();
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
</style>