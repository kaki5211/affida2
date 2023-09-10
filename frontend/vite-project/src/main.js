import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import router from './router'
import store from './store';
// import metaManager from './meta'; // 外部のmeta.jsをインポート
// import VueMeta from "vue-meta";

// import vuetify from './plugins/vuetify'
import { createMetaManager } from 'vue-meta'



createApp(App)
.use(store)
.use(router)
.use(createMetaManager())
// .use(vuetify)
.mount('#app')