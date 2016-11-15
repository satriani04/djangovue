<template>
  <div>
    <form novalidate @submit.prevent="saveTodos">
      <md-input-container>
        <label>Task</label>
        <md-input type="text" v-model="task"></md-input>
      </md-input-container>
      <md-input-container>
        <label>Textarea</label>
        <md-textarea v-model="desc"></md-textarea>
      </md-input-container>
      <md-button class="md-icon-button md-raised md-primary" type="submit">
        <md-icon>add todo</md-icon>
      </md-button>
    </form>
  </div>
</template>

<script>
import Vue from 'vue'
import {createTodoUrl} from './../api'
export default {
  data () {
    return {
      task: '',
      desc: ''
    }
  },
  methods: {
    saveTodos () {
      console.log('submitted')
      const postData = {
        task: this.task,
        desc: this.desc
      }
      Vue.http.post(createTodoUrl, postData).then((res) => {
        console.log(res)
      })
    }
  }
}
</script>

<style lang="css" scoped>
</style>