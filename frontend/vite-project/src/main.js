import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import router from './router'
import store from './store';
import { createMetaManager } from 'vue-meta'

// Vuetify
// import 'vuetify/styles'
import { createVuetify } from 'vuetify'
// import * as components from 'vuetify/components'
// import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
//   components,
//   directives,
})



createApp(App)
.use(store)
.use(router)
.use(createMetaManager())
.use(vuetify)
.mount('#app')
