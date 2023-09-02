import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import router from './router'
import store from './store';

// import vuetify from './plugins/vuetify'
// import { createMetaManager } from 'vue-meta'



createApp(App)
.use(store)
.use(router)
// .use(vuetify)
.mount('#app')