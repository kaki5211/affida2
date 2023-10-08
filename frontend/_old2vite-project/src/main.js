// /**
//  * main.js
//  *
//  * Bootstraps Vuetify and other plugins then mounts the App`
//  */

// // Components
// import App from './App.vue'

// // Composables
// import { createApp } from 'vue'

// // Plugins
// import { registerPlugins } from '@/plugins'

// const app = createApp(App)

// registerPlugins(app)

// app.mount('#app')







// Components
import App from './App.vue'
import store from './store';

// Vuetify style
// import 'vuetify/styles'
// import 'vuetify/dist/vuetify.min.css' // VuetifyのCSSをインポート


// Composables
import { createApp } from 'vue'


// Plugins
import { registerPlugins } from '@/plugins'

const app = createApp(App)

registerPlugins(app)

app
.use(store)
.mount('#app')
