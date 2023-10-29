<template>
  <div class="echart" id="mychart" :style="myChartStyle"></div>
</template>
 
<script>
import * as echarts from "echarts";

export default {
  data() {
    return {
      xData: ["安全", "城市", "交通", "经济", "科教", "民生"], //横坐标
      yData: [12, 15, 7, 23, 6, 33], //数据
      myChartStyle: { float: "left", width: "29rem", height: "18rem" }, //图表样式
    };
  },
  mounted() {
    this.initEcharts();
  },
  methods: {
    initEcharts() {
      // 基本柱状图
      const option = {
        title: { text: "今日各类舆情情况" },
        xAxis: {
          data: ["安全", "城市", "交通", "经济", "科教", "民生"],
          axisLine: { show: false }, //不显示坐标轴
          axisTick: {
            show: false, //不显示坐标轴刻度线
          },
          axisLabel: {
            show: true,
            textStyle: {
              color: "#6b738d", //更改坐标轴文字颜色
              //   fontSize : 12      //更改坐标轴文字大小
            },
          },
        },

        yAxis: {},
        series: [
          {
            name: "销量",
            type: "bar",
            data: [12, 15, 7, 23, 6, 33],
            itemStyle: {
              color: function (params) {
                var colorarrays = [
                  "#7947f7",
                  "#fff2ec",
                  "#7947f7",
                  "#fff2ec",
                  "#7947f7",
                  "#fff2ec",
                ];
                return colorarrays[params.dataIndex];
              },
              barBorderRadius: [5, 5, 5, 5],
            },
          },
        ],
      };
      const myChart = echarts.init(document.getElementById("mychart"));
      myChart.setOption(option);
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        myChart.resize();
      });
    },
  },
};
</script>
<style scoped>
.echart {
  width: 29rem;
  height: 13rem;
  overflow: hidden;
}
</style>