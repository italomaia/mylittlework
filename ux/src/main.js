import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

import '@/assets/stylesheets.css'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App)
})
