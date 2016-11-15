<template>
  <div>
    <md-list class="custom-list md-triple-line">
      <md-list-item>
          <md-avatar>
            <img src="https://placeimg.com/40/40/people/1" alt="People">
          </md-avatar>

          <div class="md-list-text-container">
            <span>{{ todo.task }}</span>
            <span>{{ todo.created }}</span>
            <p>{{ todo.desc }}</p>
          </div>

          <md-button class="md-icon-button md-list-action">
            <md-icon class="md-primary">{{ todo.completed ? 'done' : 'crop' }}</md-icon>
          </md-button>

          <md-divider class="md-inset"></md-divider>
      </md-list-item>
    </md-list>
  </div>
</template>

<script>
export default {
  props: ['todo']
}
</script>

<style lang="css" scoped>
</style>