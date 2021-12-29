<template>
  <div>
    <div style="color: dimgrey;background-color: rgba(0,0,0,0);position: absolute;left: 1vw;top:21.8vh"> 请选择周数：</div>
    <el-select style="margin-left: 1vw;width: 5.5vw;position: absolute;background-color: lightsteelblue;opacity: 0.75" v-model="weekNum" placeholder="选择周数">
      <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
      >
      </el-option>
    </el-select>

    <el-table
        :data="totalData[weekNum-1]"
        border
        ref="filterTable"
        style="width: 80%; margin-top: 20px;margin-left: 8vw;opacity: 0.8"
        header-cell-style="height:10vh;background-color:lightsteelblue;color:white;text-align:center;font-size:20px;font-weight:inherit;opacity:0.9"
        cell-style="height:11vh;width:6vw;text-align:center;font-size:16px"
    >

      <el-table-column class-name="rowClass" prop="time" :label=' "第" + this.weekNum + "周"'
                       column-key="time"

                       :filter-method="filterHandler"
      />
      <el-table-column prop="Monday" label="周一"/>
      <el-table-column prop="Tuesday" label="周二"/>
      <el-table-column prop="Wednesday" label="周三"/>
      <el-table-column prop="Thursday" label="周四"/>
      <el-table-column prop="Friday" label="周五"/>
      <el-table-column prop="Saturday" label="周六"/>
      <el-table-column prop="Sunday" label="周日"/>
    </el-table>
  </div>

</template>

<script>
export default {
  mounted() {
    console.log(this.totalData)
  },
  name: "Schedule",
  props: {
    totalData: {
      type: Array,
      default: [
        [
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
        ],
        [
          {
            time: '1,2节',
            Monday: '编译技术 锌小子 (一)215',
            Tuesday: 'asdasdasdasd',
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
            Wednesday: 'sadasdasdas',
            Thursday: '4',
            Friday: '5',
            Saturday: '6',
            Sunday: '7'
          },
          {
            time: '5,6节',
            Monday: 'asdasdasdas',
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
        [
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
        ],
      ]
    }
  },
  data() {
    return {
      tableData: this.totalData[0],
      // tableData: [],
      options: [
        {
          value: 1,
          label: '第1周',
        },
        {
          value: 2,
          label: '第2周',
        },
        {
          value: 3,
          label: '第3周',
        },
        {
          value: 4,
          label: '第4周',
        },
        {
          value: 5,
          label: '第5周',
        },
        {
          value: 6,
          label: '第6周',
        },
        {
          value: 7,
          label: '第7周',
        },
        {
          value: 8,
          label: '第8周',
        },
        {
          value: 9,
          label: '第9周',
        },
        {
          value: 10,
          label: '第10周',
        },
        {
          value: 11,
          label: '第11周',
        },
        {
          value: 12,
          label: '第12周',
        },
        {
          value: 13,
          label: '第13周',
        },
        {
          value: 14,
          label: '第14周',
        },
        {
          value: 15,
          label: '第15周',
        },
        {
          value: 16,
          label: '第16周',
        }
      ],
      weekNum: 1,
    }
  },
  methods: {
    /*update() {
      this.tableData.splice(0, this.tableData.length)
      if (this.weekNum-1 > this.totalData.length) return
      for (let i = 0; i < this.totalData[this.weekNum-1].length; i++) {
        this.tableData.splice(i, 0, this.totalData[this.weekNum-1][i]);
      }
    }*/
  }
}
</script>

<style>
.rowClass {
  background-color: lightsteelblue;
  /*background-color: mediumslateblue;*/
  color: white;
  font-size: 22px;
  text-align: center;
  font-weight: inherit;
  opacity: 0.9;

}
</style>