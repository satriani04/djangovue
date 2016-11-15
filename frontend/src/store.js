import Vue from 'vue'
import Vuex from 'vuex'
import todoStore from './components/todoStore'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    todoStore
  },
  debug: true
})
