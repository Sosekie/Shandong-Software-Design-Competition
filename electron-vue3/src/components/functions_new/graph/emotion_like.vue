<template>
    <div>
        <div class="main">
            <div class="box_gragh">
                <!-- ? -->
                <div id="figure" class="figure"></div>
                <div class="details">
                    <div class="h2">近十五天内平台动态平均情绪值</div>
                    <div class="rate">0.6457</div>
<!--                    <h3>满意</h3>-->
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
                    width: 60,
                    height: 10,
                });
            };
            var option = {
                title: {
                    text: "平均情绪值趋势",
                    x: "center",
                    textStyle: {
                        fontSize: 14,
                        color: "#1b2767",
                    },
                },
                legend: {
                    orient: "horizontal",
                    x: "left",
                    y: "top",
                    data: ["情绪值趋势"],
                    textStyle: {
                        fontSize: 14,
                        color: "#1b2767",
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
                            color: "#1b2767",
                        },
                    },
                    data: ["9月11日","9月12日","9月13日","9月14日","9月15日","9月16日","9月17日","9月18日","9月19日","9月20日","9月21日","9月22日","9月23日", "9月24日", "9月25日"],
                },
                yAxis: {
                    name: "",
                    type: "value",
                    min: 0,
                    max: 1, // 设置y轴刻度的最大值
                    splitNumber: 5, // 设置y轴刻度间隔个数
                    axisLine: {
                        lineStyle: {
                            color: "#1b2767",
                        },
                    },
                },
                series: [
                    // {
                    //     name: "情绪值趋势",
                    //     data: [0.6428,0.7236,0.6974,0.6732,0.6342,0.5243,0.7738,0.6457,0.5978,0.4987,0.5113,0.5576,0.6213,0.6345,0.5788],
                    //     // 注意：设置symbol: 'none'以后，拐点不存在了，设置拐点上显示数值无效
                    //     symbol: "none",
                    //     // 设置折线弧度，取值：0-1之间
                    //     smooth: 0.5,
                    //     color: "#55a55e",
                    // },

                    {
                        name: "情绪值趋势",
                        data: [0.6428,0.7236,0.6974,0.6732,0.6342,0.5243,0.7738,0.6457,0.5978,0.4987,0.5113,0.5576,0.6213,0.6345,0.5788],
                        type: "line",
                        color: "#1b2767",
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
    /** {*/
    /*    margin: 0;*/
    /*    padding: 0;*/
    /*    !*width: 100%;*!*/
    /*    !*height: %;*!*/
    /*    box-sizing: border-box;*/
    /*}*/
    /* 标题 */
    /* 表格处? */
    .box_gragh {
        position: relative;
        display: flex;
        width: 100%;
        height: 18rem;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }
    .box_gragh .figure {
        position: relative;
        width: 100%;
        height: 100%;
        /*border: 0.2rem solid #f4f2ff;*/

        /*padding: 1rem;*/

        transform: scale(1);
        transition: transform 500ms;
    }
    .box_gragh .details {
        position: absolute;
        width: 30%;
        height:15%;
        padding: 5%;
        background: #fff;
        color: #1b2767;
        box-shadow: 6px 6px 20px rgba(122, 122, 122, 0.212);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        transform: scale(1, 1);
        transition: transform 200ms;
    }
    .box_gragh:hover .details {
        transform: scale(0.5, 0);
    }
    .box_gragh .details .h2 {
        text-align: center;
        color: #1b2767;
        border-bottom: solid 0.01rem #1b2767aa;
        font-size: 1rem;
        font-weight: 700;
        font-family: YaHei;
        line-height: 1.5rem;
    }
    .box_gragh .details h3 {
        text-align: center;
        color: #1b2767;
        border-bottom: solid 0.1rem #5e5498;
        font-size: 1rem;
        font-weight: 700;
        font-family: YaHei;
    }
    .rate {
        padding: 0.25rem 1.25rem;
        margin: 0.25rem 0.25rem;
        background: #1b2767;
        box-shadow: 0px 11px 134px rgba(94, 84, 152, 0.5),
        0px 25.9437px 58.4156px rgba(94, 84, 152, 0.375),
        0px 4.2px 21.775px rgba(94, 84, 152, 0.2),
        0px 3.10625px 7.74687px rgba(94, 84, 152, 0.125);
        color: #f4f2ff;
        font-size: 1rem;
        font-weight: 900;
        font-family: YaHei;
        transition: all 500ms ease-in-out;
    }
</style>