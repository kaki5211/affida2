import { createApp } from 'vue'
import './style.css'
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';

// ページコンポーネントをインポート
import Home from './views/Home.vue';
import About from './views/About.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About },
  ],
});

const app = createApp(App);
app.use(router); // VueアプリケーションにVue Routerを追加

app.mount('#app');
