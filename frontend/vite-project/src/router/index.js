// router/index.js
import App from '../views/App.vue'
// import Home from '../views/Home.vue'
import About from '../views/About.vue'
import ContantsList from '../views/ContantsList.vue'
import ContantsListDisplayVideo from '../views/ContantsListDisplayVideo.vue'
import ContantsListKyounuki from '../views/ContantsListKyounuki.vue'
import ContantsDetealVideo from '../views/ContantsDetealVideo.vue'
import ContantsListDisplayArticle from '../views/ContantsListDisplayArticle.vue'

// import NotFoundComponent from '../views/NotFoundComponent.vue'

// import { computed } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
// import { useStore } from 'vuex';
// import store from '../store';




const routes= []










routes.push(

    // { path: '/home', name: 'Home', component: Home },
    // { path: '/about', name: 'About', component: About },

    // { path: '/app', name: 'App', component: App },



    { path: '/', name: 'Home', component: App },
    { path: '/video',  name: 'Videos',  meta: { subcontents: 'video'}, component: ContantsListDisplayVideo, props: true},
    { path: '/video/list',  name: 'VideosList',  meta: { subcontents: 'video'}, component: ContantsList, props: true},
    { path: '/video/:param',  name: 'Video',  meta: { subcontents: 'video'}, component: ContantsDetealVideo, props: true},
    
    { path: '/kyounuki',  name: 'Kyounuki',  meta: { subcontents: 'kyounuki'}, component: ContantsListKyounuki, props: true},
    { path: '/performer',  name: 'Performers',  meta: { subcontents: 'performer'}, component: ContantsList, props: true},
    // { path: '/performer/:param',  name: 'Performer',  meta: { subcontents: 'performer'}, component: About, props: true},
    { path: '/tag',  name: 'Tags',  meta: { subcontents: 'tag'}, component: ContantsList,  props: true},
    // { path: '/tag/:param',  name: 'Tag',  meta: { subcontents: 'tag'}, component: About, props: true},
    { path: '/maker',  name: 'Makers',  meta: { subcontents: 'maker'}, component: ContantsList, props: true},
    // { path: '/maker/:param',  name: 'Maker',  meta: { subcontents: 'maker'}, component: About, props: true},
    // { path: '/label',  name: 'Labels',  meta: { subcontents: 'label'}, component: About, props: true},
    // { path: '/label/:param',  name: 'Label',  meta: { subcontents: 'label'}, component: About, props: true},
    // { path: '/series',  name: 'Seriess',  meta: { subcontents: 'series'}, component: About, props: true},
    // { path: '/series/:param',  name: 'Series',  meta: { subcontents: 'series'}, component: About, props: true},
    { path: '/article',  name: 'Articles',  meta: { subcontents: 'article'}, component: ContantsListDisplayArticle, props: true},
    { path: '/article/list',  name: 'ArticlesList',  meta: { subcontents: 'article'}, component: ContantsList, props: true},
    { path: '/article/:param/:param2/:param3/:param4',  name: 'Article',  meta: { subcontents: 'article'}, component: ContantsListDisplayArticle, props: true},


    

    



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


  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }

    return new Promise((resolve) => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
      // スクロールが完了したら解決する
      window.addEventListener('scroll', function handler() {
        window.removeEventListener('scroll', handler, true);
        resolve();
      }, true);
    });
  },

// ルートのトレーリングスラッシュを削除
strict: true,
// 末尾のスラッシュを削除するためのリダイレクトを有効化
trailingSlash: true


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

