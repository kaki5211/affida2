import { createApp } from 'vue'
import './style.css'
import myrouter from './router'
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';

// �y�[�W�R���|�[�l���g���C���|�[�g
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
app.use(router); // Vue�A�v���P�[�V������Vue Router��ǉ�

app.mount('#app');
