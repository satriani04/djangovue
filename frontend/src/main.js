import Vue from 'vue'
import VueResource from 'vue-resource'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'
import App from './App'

/* eslint-disable no-new */
Vue.use(VueResource)
Vue.use(VueMaterial)
Vue.material.theme.register('default', {
  primary: 'indigo',
  accent: 'pink'
})

new Vue({
  el: '#app',
  template: '<App/>',
  components: { App }
})
