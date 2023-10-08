// Composables
import { createRouter, createWebHistory } from 'vue-router'

// router/index.js
import App from '../views/App.vue'
// import Home from '../views/Home.vue'
import About from '../views/About.vue'
// import ContantsListVideo from '../views/ContantsListVideo.vue'
// import ContantsListKyounuki from '../views/ContantsListKyounuki.vue'

// import NotFoundComponent from '../views/NotFoundComponent.vue'

// import { computed } from 'vue';
// import { createRouter, createWebHistory } from 'vue-router';
// import { useStore } from 'vuex';
// import store from '../store';








const routes = [
  
    // path: '/',
    // component: () => import('@/layouts/default/Default.vue'),
    // children: [
      // {
      //   path: '',
      //   name: 'Home',
      //   component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      // },


      { path: '/', name: 'Home', component: App },
      { path: '/video',  name: 'Videos',  meta: { subcontents: 'video'}, component: About, props: true},
      { path: '/video/:param',  name: 'Video',  meta: { subcontents: 'video'}, component: About, props: true},
      { path: '/kyounuki',  name: 'Kyounuki',  meta: { subcontents: 'kyounuki'}, component: About, props: true},
      { path: '/performer',  name: 'Performers',  meta: { subcontents: 'performer'}, component: About, props: true},
      { path: '/performer/:param',  name: 'Performer',  meta: { subcontents: 'performer'}, component: About, props: true},
      { path: '/tag',  name: 'Tags',  meta: { subcontents: 'tag'}, component: About,  props: true},
    //   { path: '/tag/:param',  name: 'Tag',  meta: { subcontents: 'tag'}, component: About, props: true},
      { path: '/maker',  name: 'Makers',  meta: { subcontents: 'maker'}, component: About, props: true},
    //   { path: '/maker/:param',  name: 'Maker',  meta: { subcontents: 'maker'}, component: About, props: true},
      { path: '/label',  name: 'Labels',  meta: { subcontents: 'label'}, component: About, props: true},
    //   { path: '/label/:param',  name: 'Label',  meta: { subcontents: 'label'}, component: About, props: true},
      // { path: '/series',  name: 'Seriess',  meta: { subcontents: 'series'}, component: About, props: true},
      // { path: '/series/:param',  name: 'Series',  meta: { subcontents: 'series'}, component: About, props: true},




    // ],
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router



