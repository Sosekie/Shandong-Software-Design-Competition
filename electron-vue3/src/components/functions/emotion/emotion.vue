<template>
  <div>
    <div class="main">
      <div class="box">
        <!-- ? -->
        <div id="figure" class="figure"></div>
        <div class="details">
          <div class="h2">该主题词今日人民满意度为</div>
          <div class="rate">78%</div>
          <h3>满意</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import Vue from "vue";

export default {
  name: "emotion",
  components: {},
  mounted() {
    var myChart = echarts.init(document.getElementById("figure"));
    window.onresize = function () {
      myChart.resize({
        width: 80,
        height: 400,
      });
    };
    var option = {
      title: {
        text: "情绪趋势",
        x: "center",
        textStyle: {
          fontSize: 14,
        },
      },
      legend: {
        orient: "horizontal",
        x: "left",
        y: "top",
        data: ["正面舆情趋势", "负面舆情趋势"],
        textStyle: {
          fontSize: 14,
        },
      },
      grid: {
        top: "16%", // 等价于 y: '16%'
        left: "3%",
        right: "8%",
        bottom: "3%",
        containLabel: true,
      },
      tooltip: {
        trigger: "axis",
        textStyle: {
          fontSize: 24,
        },
      },
      toolbox: {
        feature: {
          saveAsImage: {}, //下载工具
        },
      },
      xAxis: {
        name: "日期",
        type: "category",
        axisLine: {
          lineStyle: {
            // 设置x轴颜色
            color: "#5e5498",
          },
        },
        data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
      },
      yAxis: {
        name: "",
        type: "value",
        min: 0,
        max: 2000, // 设置y轴刻度的最大值
        splitNumber: 5, // 设置y轴刻度间隔个数
        axisLine: {
          lineStyle: {
            color: "#5e5498",
          },
        },
      },
      series: [
        {
          name: "正面舆情趋势",
          data: [820, 932, 301, 1434, 1290, 1330, 1320],
          type: "line",
          // 设置小圆点消失
          // 注意：设置symbol: 'none'以后，拐点不存在了，设置拐点上显示数值无效
          symbol: "none",
          // 设置折线弧度，取值：0-1之间
          smooth: 0.5,
          color: "#55a55e",
        },

        {
          name: "负面舆情趋势",
          data: [620, 732, 941, 834, 1690, 1030, 920],
          type: "line",
          color: "#5e5498",
          // 设置折线上圆点大小
          symbolSize: 8,
          itemStyle: {
            normal: {
              // 拐点上显示数值
              label: {
                show: true,
              },
              borderColor: "red", // 拐点边框颜色
              lineStyle: {
                width: 5, // 设置线宽
                type: "dotted", //'dotted'虚线 'solid'实线
              },
            },
          },
        },
      ],
    };
    myChart.setOption(option);
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
/* 标题 */
/* 表格处? */
.box {
  position: relative;
  display: flex;
  width: 66.5rem;
  height: 11rem;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  display: inline-block;
}
.box .figure {
  position: relative;
  width: 66.5rem;
  height: 11rem;
  border: 0.2rem solid #f4f2ff;
  box-shadow: inset 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  padding: 1rem;
  box-shadow: 6px 6px 20px rgba(122, 122, 122, 0.212);
  transform: scale(1);
  transition: transform 500ms;
}
.box .details {
  position: absolute;
  top: 1rem;
  left: 1rem;
  right: 1rem;
  bottom: 1rem;
  margin: 0.5rem 10rem;
  background: #fffa;
  box-shadow: 0px 71px 134px rgba(94, 84, 152, 0.1),
    0px 35.9437px 58.4156px rgba(94, 84, 152, 0.0675),
    0px 14.2px 21.775px rgba(94, 84, 152, 0.05),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.0325);
  color: #797c8c;
  box-shadow: 6px 6px 20px rgba(122, 122, 122, 0.212);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transform: scale(1, 1);
  transition: transform 200ms;
}
.box:hover .details {
  transform: scale(0.5, 0);
}
.box .details .h2 {
  text-align: center;
  color: #5e5498;
  border-bottom: solid 0.01rem #dce3eb;
  font-size: 1.5rem;
  font-weight: 700;
  font-family: YaHei;
}
.box .details h3 {
  text-align: center;
  color: #6b738d;
  border-bottom: solid 0.1rem #5e5498;
  font-size: 1.2rem;
  font-weight: 700;
  font-family: YaHei;
}
.rate {
  padding: 0.25rem 1.25rem;
  margin: 0.25rem 0.25rem;
  background: #5e5498;
  box-shadow: 0px 11px 134px rgba(94, 84, 152, 0.5),
    0px 25.9437px 58.4156px rgba(94, 84, 152, 0.375),
    0px 4.2px 21.775px rgba(94, 84, 152, 0.2),
    0px 3.10625px 7.74687px rgba(94, 84, 152, 0.125);
  color: #f4f2ff;
  font-size: 1.2rem;
  font-weight: 900;
  font-family: YaHei;
  transition: all 500ms ease-in-out;
}
</style>