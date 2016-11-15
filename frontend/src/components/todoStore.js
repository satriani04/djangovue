import Vue from 'vue'
import {todoapi, createTodoUrl} from './../api'
const state = {
  todoList: []
}

const mutations = {
  SET_TODO_LIST (state, todoList) {
    state.todoList = todoList
  },
  ADD_TODO (state, newTodo) {
    state.todoList.push(newTodo)
  }
}

const actions = {
  setTodoList: ({commit}) => {
    Vue.http.get(todoapi).then((res) => {
      commit('SET_TODO_LIST', res.body)
      return res.body
    })
  },
  addTodo: ({commit}, newTodo) => {
    Vue.http.post(createTodoUrl, newTodo).then((res) => {
      if (res.status === 201) {
        commit('ADD_TODO', newTodo)
      }
    })
  }
}

export default {
  state, mutations, actions
}
