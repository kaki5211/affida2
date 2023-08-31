import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'


import { createStore } from 'vuex';
import axios from 'axios';

import { createVuetify } from 'vuetify';
import { aliases, mdi } from 'vuetify/iconsets/mdi-svg';

// import vuetify from './plugins/vuetify'

import { loadFonts } from './plugins/webfontloader'

import store from './store';

import { createMetaManager } from 'vue-meta'

import VSkeletonLoader from 'v-skeleton-loader';

// import VueVideoPlayer from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'


// const app = createApp(App)

// app.use(plugin)
// app.mixin(createMeta())
// store.fetchDataAndInitializeStore(store);

loadFonts();


// const vuetify = createVuetify({
//     icons: {
//         defaultSet: 'mdi',
//         aliases,
//         sets: {
//             mdi,
//         },
//     },
//  });












createApp(App)
.use(store)
.use(router)
.use(createMetaManager())
.use(vuetify)
.use(VueVideoPlayer)
.component('v-skeleton-loader', VSkeletonLoader)
// .use(createMetaManager())


.mount('#app');

