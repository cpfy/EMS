import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'

// 配置请求的根路径
axios.defaults.baseURL = 'http://127.0.0.1:8000/'

// 挂载到vue
// Vue.prototype.$http = axios

createApp(App).use(store).use(router).use(ElementPlus).use(VueAxios,axios).mount('#app')

