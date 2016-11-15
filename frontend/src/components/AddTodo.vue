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
// import {mapState} from 'vuex'
export default {
  data () {
    return {
      task: '',
      desc: ''
    }
  },
  // computed: {
  //   ...mapState({
  //     todoStore: state => state.todoStore
  //   })
  // },
  methods: {
    saveTodos () {
      const postData = {
        task: this.task,
        desc: this.desc
      }
      this.$store.dispatch('addTodo', postData)
    }
  }
}
</script>

<style lang="css" scoped>
</style>