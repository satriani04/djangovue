<template>
  <div class="container">
    <add-todo class="todo-form"></add-todo>
    <todolist v-for="todo in todos" :todo="todo"></todolist>
  </div>
</template>

<script>
import Vue from 'vue'
import AddTodo from './AddTodo'
import Todolist from './Todolist'
import {todoapi} from './../api'
export default {
  components: {
    Todolist, AddTodo
  },
  data () {
    return {
      todos: []
    }
  },
  created () {
    this.$http.get(todoapi).then((res) => {
      console.log(res)
      Vue.set(this, 'todos', res.body)
    })
  }
}
</script>

<style lang="css" scoped>
  .container{
    width: 70%;
    margin: auto;
  }
  .container .todo-form{
    margin-top: 10px;
    margin-bottom: 10px;
  }
</style>