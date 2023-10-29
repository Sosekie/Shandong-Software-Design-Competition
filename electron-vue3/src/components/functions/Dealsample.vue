<template>
  <div class="dig" id="message">
    <div class="mod">
      <!-- <router-link to="/Deal/"> -->
      <button class="mod1">诉求处理详情</button>
      <!-- </router-link> -->
      <img src="../../assets/line.png" alt="" />
      <!-- <router-link to="/Deal/deal2"> -->
      <button class="mod2" @click="toggle">自定义上传查询</button>
      <!-- </router-link> -->
    </div>
    <div class="contentDeal">
      <div class="messageBox" v-if="bol" @click="close">
        <div class="boardout" @click.stop="">
          <div class="board">
            <div class="word">单条查询</div>
            <input type="text" class="miaoshu" placeholder="诉求描述" />
            <img src="../../assets/linehori.png" alt="" />
            <div class="word">批量查询</div>
            <div class="func">
              <button>诉求导入</button>
              <div class="discrip">?导入格式说明</div>
            </div>
          </div>
          <div class="chaxun">查询</div>
        </div>
      </div>
      <div class="contentDeal1">
        <div class="dealleft">
          <div class="questionleft" v-for="(item, index) in items">
            <button onclick="clickTab(this)" @click="getIndex(index)">
              <div class="title">{{ item.title }}</div>
              <div class="bar">|</div>
              <div class="words">{{ item.text }}</div>
            </button>
          </div>
        </div>
        <div class="middle">
          <div class="up">
            <div>
              <div v-if="show === 1">
                {{ items[key].content }}
              </div>
            </div>
          </div>
          <div class="down">
            <div class="left">
              <iframe
                src="chartdeal.html"
                name="topFrame"
                scrolling="No"
                frameborder="0"
                class="topFrame"
                v-if="play"
              ></iframe>
            </div>
            <div class="right">
              <button @click="displayon">
                <img src="../../assets/point.png" alt="" />智能转办
              </button>
              <div class="title">处理建议</div>
              <div v-if="play">
                <div class="words">市文化和旅游局</div>
                <div class="words">市社会保障局</div>
                <div class="words">市人民政府办公厅</div>
              </div>
            </div>
          </div>
        </div>
        <div class="dealright">
          <div class="titleright">相似工单</div>
          <div>
            <div class="questionright" v-for="(item, index) in items2">
              <button onclick="clickTab(this)" @click="getIndex2(index)">
                <div class="title">{{ item.title }}</div>
                <div class="bar">|</div>
                <div class="words">{{ item.text }}</div>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script scoped>
// import Vue from "vue";

export default {
  name: "Deal",
  data() {
    return {
      bol: false,
      play: false,
      key: 0,
      content: false,
      show: 1,
      items: [
        {
          title: "民生问题",
          text: "疫情复工",
          content:
            "健身房，台球厅，饭店各行业都可以复工营业了，电影院在做好防疫的情况下，什么时间可以营业啊，咱这边有没有具体的计划啊，每天的亏损实在扛不住了",
        },
        {
          title: "民生问题",
          text: "家庭暴力",
          content:
            "我们家隔壁好像有人在家暴 但今天是我第一天搬过来 不知道是隔壁还是楼下？ 我能听到的东西撞墙的声音，能听到一个男人咬着牙说是不是没完了？不知道要不要报警？一方面不能确定是哪一家，另外一方面也没办法完全确定是存在暴力行为的@青岛公安 但是那个男人咬着牙恶狠狠说话的声音真的很可怕。这个声音大概十分钟就会出现一次，应该是从晚上11点左右就开始了，中间停了很长一段时间，现在又开始了。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "交通问题",
          text: "市南区交通堵塞严重",
          content:
            "王沙路修路好几段是单车道，等公交车的人还站在马路上，本来就一个车道，人一站在那不但堵车，等车的人还有危险，公交车到站一停后面的车都堵起来了，今天为了躲避马路上等车的那几个人（照片上画红圈的就是等公交车的人），前车突然急刹车，导致追尾堵车！王沙路修路工程要到7月份才结束，早高峰晚高峰更是因为公交车停车、乘客等车等原因堵的要命，相关部门能不能好好规划一下？@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "物价问题",
          text: "猪肉持续涨价",
          content:
            "今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。 今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "民生问题",
          text: "家庭暴力",
          content:
            "我们家隔壁好像有人在家暴 但今天是我第一天搬过来 不知道是隔壁还是楼下？ 我能听到的东西撞墙的声音，能听到一个男人咬着牙说是不是没完了？不知道要不要报警？一方面不能确定是哪一家，另外一方面也没办法完全确定是存在暴力行为的@青岛公安 但是那个男人咬着牙恶狠狠说话的声音真的很可怕。这个声音大概十分钟就会出现一次，应该是从晚上11点左右就开始了，中间停了很长一段时间，现在又开始了。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "交通问题",
          text: "市南区交通堵塞严重",
          content:
            "王沙路修路好几段是单车道，等公交车的人还站在马路上，本来就一个车道，人一站在那不但堵车，等车的人还有危险，公交车到站一停后面的车都堵起来了，今天为了躲避马路上等车的那几个人（照片上画红圈的就是等公交车的人），前车突然急刹车，导致追尾堵车！王沙路修路工程要到7月份才结束，早高峰晚高峰更是因为公交车停车、乘客等车等原因堵的要命，相关部门能不能好好规划一下？@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "物价问题",
          text: "猪肉持续涨价",
          content:
            "今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。 今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "民生问题",
          text: "家庭暴力",
          content:
            "我们家隔壁好像有人在家暴 但今天是我第一天搬过来 不知道是隔壁还是楼下？ 我能听到的东西撞墙的声音，能听到一个男人咬着牙说是不是没完了？不知道要不要报警？一方面不能确定是哪一家，另外一方面也没办法完全确定是存在暴力行为的@青岛公安 但是那个男人咬着牙恶狠狠说话的声音真的很可怕。这个声音大概十分钟就会出现一次，应该是从晚上11点左右就开始了，中间停了很长一段时间，现在又开始了。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "交通问题",
          text: "市南区交通堵塞严重",
          content:
            "王沙路修路好几段是单车道，等公交车的人还站在马路上，本来就一个车道，人一站在那不但堵车，等车的人还有危险，公交车到站一停后面的车都堵起来了，今天为了躲避马路上等车的那几个人（照片上画红圈的就是等公交车的人），前车突然急刹车，导致追尾堵车！王沙路修路工程要到7月份才结束，早高峰晚高峰更是因为公交车停车、乘客等车等原因堵的要命，相关部门能不能好好规划一下？@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "物价问题",
          text: "猪肉持续涨价",
          content:
            "今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。 今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "民生问题",
          text: "家庭暴力",
          content:
            "我们家隔壁好像有人在家暴 但今天是我第一天搬过来 不知道是隔壁还是楼下？ 我能听到的东西撞墙的声音，能听到一个男人咬着牙说是不是没完了？不知道要不要报警？一方面不能确定是哪一家，另外一方面也没办法完全确定是存在暴力行为的@青岛公安 但是那个男人咬着牙恶狠狠说话的声音真的很可怕。这个声音大概十分钟就会出现一次，应该是从晚上11点左右就开始了，中间停了很长一段时间，现在又开始了。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "交通问题",
          text: "市南区交通堵塞严重",
          content:
            "王沙路修路好几段是单车道，等公交车的人还站在马路上，本来就一个车道，人一站在那不但堵车，等车的人还有危险，公交车到站一停后面的车都堵起来了，今天为了躲避马路上等车的那几个人（照片上画红圈的就是等公交车的人），前车突然急刹车，导致追尾堵车！王沙路修路工程要到7月份才结束，早高峰晚高峰更是因为公交车停车、乘客等车等原因堵的要命，相关部门能不能好好规划一下？@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "物价问题",
          text: "猪肉持续涨价",
          content:
            "今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。 今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
      ],
      items2: [
        {
          title: "民生问题",
          text: "允许开业",
          content:
            "请问理发店何时能够开业，店内以做好消毒措施，保证严格落实疫情防控政策，希望可以尽早允许开业，我们要挣钱吃饭啊",
        },
        {
          title: "民生问题",
          text: "影院营业",
          content: "求问电影院什么时候能开业啊",
        },
        {
          title: "民生问题",
          text: "解除封控",
          content: "已经连续多日没有新增病例了，请问何时可以解除封控？",
        },
        {
          title: "民生问题",
          text: "家庭暴力",
          content:
            "我们家隔壁好像有人在家暴 但今天是我第一天搬过来 不知道是隔壁还是楼下？ 我能听到的东西撞墙的声音，能听到一个男人咬着牙说是不是没完了？不知道要不要报警？一方面不能确定是哪一家，另外一方面也没办法完全确定是存在暴力行为的@青岛公安 但是那个男人咬着牙恶狠狠说话的声音真的很可怕。这个声音大概十分钟就会出现一次，应该是从晚上11点左右就开始了，中间停了很长一段时间，现在又开始了。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "交通问题",
          text: "市南区交通堵塞严重",
          content:
            "王沙路修路好几段是单车道，等公交车的人还站在马路上，本来就一个车道，人一站在那不但堵车，等车的人还有危险，公交车到站一停后面的车都堵起来了，今天为了躲避马路上等车的那几个人（照片上画红圈的就是等公交车的人），前车突然急刹车，导致追尾堵车！王沙路修路工程要到7月份才结束，早高峰晚高峰更是因为公交车停车、乘客等车等原因堵的要命，相关部门能不能好好规划一下？@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "物价问题",
          text: "猪肉持续涨价",
          content:
            "今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。 今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "民生问题",
          text: "家庭暴力",
          content:
            "我们家隔壁好像有人在家暴 但今天是我第一天搬过来 不知道是隔壁还是楼下？ 我能听到的东西撞墙的声音，能听到一个男人咬着牙说是不是没完了？不知道要不要报警？一方面不能确定是哪一家，另外一方面也没办法完全确定是存在暴力行为的@青岛公安 但是那个男人咬着牙恶狠狠说话的声音真的很可怕。这个声音大概十分钟就会出现一次，应该是从晚上11点左右就开始了，中间停了很长一段时间，现在又开始了。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "交通问题",
          text: "市南区交通堵塞严重",
          content:
            "王沙路修路好几段是单车道，等公交车的人还站在马路上，本来就一个车道，人一站在那不但堵车，等车的人还有危险，公交车到站一停后面的车都堵起来了，今天为了躲避马路上等车的那几个人（照片上画红圈的就是等公交车的人），前车突然急刹车，导致追尾堵车！王沙路修路工程要到7月份才结束，早高峰晚高峰更是因为公交车停车、乘客等车等原因堵的要命，相关部门能不能好好规划一下？@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "物价问题",
          text: "猪肉持续涨价",
          content:
            "今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。 今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "民生问题",
          text: "家庭暴力",
          content:
            "我们家隔壁好像有人在家暴 但今天是我第一天搬过来 不知道是隔壁还是楼下？ 我能听到的东西撞墙的声音，能听到一个男人咬着牙说是不是没完了？不知道要不要报警？一方面不能确定是哪一家，另外一方面也没办法完全确定是存在暴力行为的@青岛公安 但是那个男人咬着牙恶狠狠说话的声音真的很可怕。这个声音大概十分钟就会出现一次，应该是从晚上11点左右就开始了，中间停了很长一段时间，现在又开始了。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "交通问题",
          text: "市南区交通堵塞严重",
          content:
            "王沙路修路好几段是单车道，等公交车的人还站在马路上，本来就一个车道，人一站在那不但堵车，等车的人还有危险，公交车到站一停后面的车都堵起来了，今天为了躲避马路上等车的那几个人（照片上画红圈的就是等公交车的人），前车突然急刹车，导致追尾堵车！王沙路修路工程要到7月份才结束，早高峰晚高峰更是因为公交车停车、乘客等车等原因堵的要命，相关部门能不能好好规划一下？@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "物价问题",
          text: "猪肉持续涨价",
          content:
            "今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。 今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "民生问题",
          text: "家庭暴力",
          content:
            "我们家隔壁好像有人在家暴 但今天是我第一天搬过来 不知道是隔壁还是楼下？ 我能听到的东西撞墙的声音，能听到一个男人咬着牙说是不是没完了？不知道要不要报警？一方面不能确定是哪一家，另外一方面也没办法完全确定是存在暴力行为的@青岛公安 但是那个男人咬着牙恶狠狠说话的声音真的很可怕。这个声音大概十分钟就会出现一次，应该是从晚上11点左右就开始了，中间停了很长一段时间，现在又开始了。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "交通问题",
          text: "市南区交通堵塞严重",
          content:
            "王沙路修路好几段是单车道，等公交车的人还站在马路上，本来就一个车道，人一站在那不但堵车，等车的人还有危险，公交车到站一停后面的车都堵起来了，今天为了躲避马路上等车的那几个人（照片上画红圈的就是等公交车的人），前车突然急刹车，导致追尾堵车！王沙路修路工程要到7月份才结束，早高峰晚高峰更是因为公交车停车、乘客等车等原因堵的要命，相关部门能不能好好规划一下？@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
        {
          title: "物价问题",
          text: "猪肉持续涨价",
          content:
            "今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。 今年小麦亩产又增收了 　2021年由于受雨灾影响，延津县小麦播期普遍滞后、播期拉长，晚播弱苗占比偏高。小麦长势好不好、产量稳不稳、增收有没有希望成为众多农户关心的问题。 随着气温逐渐回升，麦田已是一片青绿。农技人员正在观察苗情，种植户在洒药施肥，水肥药一体化设备也正在按照设定好的程序给麦田浇水，田间地头变得忙碌起来。李元智告诉记者，今年苗情看上去不错，产量和收入不会比去年差。@青岛交通管理监督 @青岛交警 @青岛新闻网民生在线 @青岛政务 @青岛交通广播FM897 @城阳交警",
        },
      ],
    };
  },
  methods: {
    toggle() {
      this.bol = !this.bol;
    },
    close() {
      this.bol = !this.bol;
    },
    displayon() {
      this.play = !this.play;
    },
    contentview() {
      this.content = !this.content;
    },
    getIndex(index) {
      this.key = index;
      // console.log(this.key);
      this.show = 1;
    },
  },
  components: {},
};
</script>

<style scoped>
.dig {
  width: 66.5rem;
  height: 36rem;
  /* border: 1px solid; */
  display: flex;
  flex-direction: column;
}
.mod {
  flex: 1.5rem;
  /* border: 1px solid; */
  height: 1.5rem;
  width: 66.5rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.mod img {
  height: 0.8rem;
  margin: 0 0.5rem;
}
.mod button {
  width: 10rem;
  height: 1.5rem;
  border: 0.1rem solid #778e9577;
  background-color: #778e9522;
  color: #0bedae;
  font-size: 1rem;
  font-weight: 100;
  font-family: YouYuan;
  transition: all 200ms ease-in-out;
}
.mod button:hover {
  background-color: #0bedae;
  color: #fff;
  font-weight: 500;
}
.mod el-button {
  width: 10rem;
  height: 1.5rem;
  border: 0.1rem solid #778e9577;
  background-color: #778e9522;
  color: #0bedae;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  font-weight: 100;
  font-family: YouYuan;
  transition: all 200ms ease-in-out;
}
.mod el-button:hover {
  background-color: #0bedae;
  color: #fff;
  font-weight: 500;
}

.contentDeal {
  flex: 34.5rem;
  margin-top: 1rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

.messageBox {
  width: 100%;
  height: 100%;
  margin: 2.5rem 0rem 0rem 3.5rem;
  position: fixed;
  left: 0;
  top: 0;
  background-color: #0006;
  z-index: 2;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  /* transition: all 200ms ease-in-out; */
}
.messageBox .boardout {
  width: 20rem;
  margin: 0rem 7rem 5rem 0rem;
  border-radius: 0.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.messageBox .boardout .board {
  padding: 1rem;
  margin: 0;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 1),
    rgba(250, 251, 252, 0.8)
  );
  border-radius: 0.2rem 0.2rem 0 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.messageBox .board .word {
  width: 20rem;
  font-weight: 900;
  color: #687684;
}
.messageBox .board img {
  width: 20rem;
  height: 0.05rem;
  margin-bottom: 0.5rem;
}
.messageBox .board input {
  width: 18rem;
  margin: 0.5rem;
  padding: 0.2rem;
  border: 0;
  border-radius: 0.2rem;
  background-color: #e3dada;
  outline: medium;
  font-size: 1rem;
  font-weight: 100;
  text-align: center;
  font-family: YouYuan;
  -webkit-app-region: no-drag;
}
.messageBox .func {
  width: 20rem;
  margin: 0.5rem 0.5rem 0rem 0.5rem;
  display: flex;
  flex-direction: row;
  align-items: baseline;
  justify-content: left;
}
.messageBox .func button {
  width: 5rem;
  height: 2rem;
  border: 0;
  border-radius: 0.2rem;
  background-color: #fff;
  filter: drop-shadow(1 1 0.01rem #000);
}
.messageBox .func .discrip {
  font-size: 0.6rem;
  font-weight: 900;
  color: #687684;
  filter: drop-shadow(1 1 0.01rem #000);
}
.messageBox .chaxun {
  padding: 0.5rem 1rem;
  margin: 0;
  width: 21rem;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 1),
    rgba(250, 251, 252, 1)
  );
  border-radius: 0 0 0.2rem 0.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 900;
}

.contentDeal1 {
  flex: 34.5rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  color: #687684;
  z-index: 1;
}
.dealleft {
  flex: 15rem;
  height: 33.5rem;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 0.3),
    rgba(250, 251, 252, 0.2)
  );
  border-radius: 0.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: scroll;
}
.questionleft button {
  margin-top: 0.5rem;
  width: 14rem;
  height: 3rem;
  color: #fff;
  border: 0;
  font-size: 1rem;
  font-weight: 100;
  text-align: center;
  font-family: YouYuan;
  text-shadow: 0.01rem 0.01rem 1px #fff;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 0.3),
    rgba(250, 251, 252, 0.2)
  );
  border-radius: 0.2rem;
  padding: 0.2rem 0.5rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  transition: all 100ms ease-in-out;
}
.questionleft button:focus {
  height: 3.5rem;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 1),
    rgba(250, 251, 252, 0.8)
  );
  color: #687684;
}
.questionleft .title {
  width: 5rem;
  font-size: 1rem;
  overflow: scroll;
}
.questionleft .bar {
  font-size: 1.5rem;
}
.questionleft .words {
  width: 10rem;
  height: 2.5rem;
  font-size: 0.8rem;
  overflow: scroll;
  display: flex;
  flex-direction: row;
  transition: all 200ms ease-in-out;
}
.questionleft:hover .words {
  height: 3rem;
}
.middle {
  flex: 40rem;
  height: 33.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.middle .up {
  height: 8.5rem;
  width: 36rem;
  color: #fff;
  /* text-shadow: 0.01rem 0.01rem 1px #fff; */
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 0.5),
    rgba(250, 251, 252, 0.4)
  );
  border-radius: 0.2rem;
  padding: 1rem;
  text-align: left;
  margin-bottom: 1rem;
  overflow: scroll;
  line-height: 1.5rem;
}
.middle .down {
  width: 38rem;
  height: 22rem;
  display: flex;
}
.middle .down .left {
  flex: 27rem;
  height: 22rem;
  /* width: 29rem; */
  margin-right: 1rem;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 0.3),
    rgba(250, 251, 252, 0.2)
  );
  border-radius: 0.2rem;
  border-radius: 0.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.middle .down .left iframe {
  width: 26rem;
  height: 21rem;
  padding: 0rem;
  margin: 0rem;
}
.middle .down .right {
  flex: 10rem;
  height: 22rem;
  /* width: 8rem; */
  /* border: 1px solid #000; */
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 0.3),
    rgba(250, 251, 252, 0.2)
  );
  border-radius: 0.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: scroll;
}
.middle .down .right button {
  width: 9rem;
  height: 3rem;
  margin-top: 1rem;
  border: 0;
  border-radius: 0.2rem;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 1),
    rgba(250, 251, 252, 1)
  );
  font-size: 1.2rem;
  font-weight: 100;
  text-align: center;
  font-family: YouYuan;
  color: #687684;
  text-shadow: 0.01rem 0.01rem 1px #687684;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  transition: all 200ms ease-in-out;
}
.middle .down .right button:hover {
  width: 9.5rem;
  height: 3.2rem;
}
.middle .down .right img {
  width: 1rem;
}
.middle .down .right .title {
  margin: 1rem;
  color: #fff;
  font-size: 1.2rem;
}
.middle .down .right .words {
  margin-bottom: 0.5rem;
  width: 8rem;
  height: 3rem;
  color: #fff;
  text-shadow: 0.01rem 0.01rem 1px #fff;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 0.3),
    rgba(250, 251, 252, 0.2)
  );
  border-radius: 0.2rem;
  padding: 0.2rem 0.5rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  transition: all 200ms ease-in-out;
}
.dealright {
  flex: 11.5rem;
  height: 33.5rem;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 0.3),
    rgba(250, 251, 252, 0.2)
  );
  border-radius: 0.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: scroll;
}
.dealright .titleright {
  margin: 1rem;
  color: #000;
}
.questionright button {
  margin-bottom: 0.5rem;
  width: 10.5rem;
  height: 3rem;
  color: #fff;
  border: 0;
  font-size: 1rem;
  font-weight: 100;
  text-align: center;
  font-family: YouYuan;
  text-shadow: 0.01rem 0.01rem 1px #fff;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 0.3),
    rgba(250, 251, 252, 0.2)
  );
  border-radius: 0.2rem;
  padding: 0.2rem 0.5rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  transition: all 200ms ease-in-out;
}
.questionright button:focus {
  height: 3.5rem;
  background: linear-gradient(
    to bottom,
    rgba(250, 251, 252, 1),
    rgba(250, 251, 252, 0.8)
  );
  color: #687684;
  border: 0;
}
.questionright .title {
  width: 4rem;
  font-size: 1rem;
  overflow: scroll;
}
.questionright .bar {
  font-size: 1.5rem;
}
.questionright .words {
  width: 11rem;
  height: 2.5rem;
  font-size: 0.8rem;
  overflow: scroll;
  display: flex;
  flex-direction: row;
  transition: all 200ms ease-in-out;
}
.questionright:hover .words {
  height: 3rem;
}
</style>