import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';

// 创建axios实例
const service = axios.create({
    // axios中请求配置有baseURL选项，表示请求URL公共部分
    baseURL: 'http://localhost:8001',
    // 超时
    timeout: 10000,
});
Vue.prototype.$axios = service; // 给vue的原型添加一个公有的axios，各个组件都能直接用this.$axios，而不需要再引用


new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
