import { createApp } from 'vue'
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import './style.css'
import App from './App.vue'
import router from './routes/router.ts'
  
// Iconos opcionales
import '@mdi/font/css/materialdesignicons.css'

const vuetify = createVuetify({
    components,
    directives,
  })

createApp(App)
.use(vuetify)
.use(router)
.mount('#app')