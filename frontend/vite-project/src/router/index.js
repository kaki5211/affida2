// router/index.js
import Home from '../views/Home.vue'
import About from '../views/About.vue'
// import NotFoundComponent from '../views/NotFoundComponent.vue'

// import { computed } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
// import { useStore } from 'vuex';
// import store from '../store';




const routes= []










routes.push(
  
    { path: '/home', name: 'Home', component: Home },
    { path: '/about', name: 'About', component: About },


//   { path: '/:pathMatch(.*)*', name: 'App_none', component: NotFoundComponent },
);


// function sleep(ms) {
//   return new Promise(resolve => setTimeout(resolve, ms));
// }

// async function doSomething() {
//   console.log('処理を開始します');
//   await sleep(10000); // 3秒待機
//   console.log('処理を終了しました');
// }


// import smoothscroll from 'smoothscroll-polyfill';


// const scrollBehavior = async (to, from, savedPosition) => {

//   if (savedPosition) {
//     return savedPosition;
//   }

//   return { x: 0, y: 0 };
// };



const router = createRouter({
  history: createWebHistory(),
  routes,

});

// router.beforeEach((to, from, next) => {
//   if (to.name === 'Books_Contents') {
//     // /books/:params にアクセスした場合、リダイレクトして /books/:params/:params2 に遷移する
//     const params = to.params.params;
//     const params2 = '1'; // params2 の値を指定
//     next({ name: 'Books_Contents_Pages', params: { params, params2 } });
//   } else {
//     next();
//   }
// });











export default router;

