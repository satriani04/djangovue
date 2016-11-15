<template>
  <div class="container">
    <add-todo class="todo-form"></add-todo>
    <todolist v-for="todo in todoStore.todoList" :todo="todo"></todolist>
  </div>
</template>

<script>
import AddTodo from './AddTodo'
import Todolist from './Todolist'
import {mapState} from 'vuex'
export default {
  components: {
    Todolist, AddTodo
  },
  computed: {
    ...mapState({
      todoStore: state => state.todoStore
    })
  },
  created () {
    this.$store.dispatch('setTodoList')
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