<template>
  <div>
    <md-toolbar>
      <md-button class="md-icon-button" @click="toggleLeftSidenav">
        <md-icon>menu</md-icon>
      </md-button>

      <h2 class="md-title" style="flex: 1">DjangoVue Todo Apps</h2>

      <md-button class="md-icon-button">
        <md-icon>favorite</md-icon>
      </md-button>
    </md-toolbar>
    <md-sidenav class="md-left" ref="leftSidenav" @open="open('Left')" @close="close('Left')">
      <md-toolbar class="md-large">
        <div class="md-toolbar-container">
          <h3 class="md-title">DjangoVue</h3>
        </div>
      </md-toolbar>
      <div class="sidebar-content">
        <p>this is simple project todo list apps with django as backend api and vue js as frontend</p>
        <b>Copyright &copy; by Winarto Saputro</b>
      </div>
    </md-sidenav>
  </div>  
</template>

<script>
import SideBar from './SideBar'
export default {
  components: {
    SideBar
  },
  methods: {
    toggleLeftSidenav () {
      this.$refs.leftSidenav.toggle()
    },
    open (ref) {
      console.log('Opened: ' + ref)
    },
    close (ref) {
      console.log('Closed: ' + ref)
    }
  }
}
</script>

<style lang="css" scoped>
.md-title {
  margin: auto;
}
.sidebar-content {
  padding: 0 5px;
}
</style>