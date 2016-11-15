<template>
  <div id="app" v-md-theme="'default'">
    <toolbar></toolbar>
    <maincontent></maincontent>
  </div>
</template>

<script>
import Toolbar from './components/Toolbar'
import Maincontent from './components/Maincontent'
export default {
  name: 'app',
  components: {
    Toolbar, Maincontent
  }
}
</script>

<style>
#app {
  text-align: center;
}
</style>
