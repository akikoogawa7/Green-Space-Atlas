<template>
  <img alt="Green atlas logo" src="./assets/satellite.png" width='100'>
  <div id="app">@{{ user.username }}</div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      countries: 'list of countries',
      map: 'map',
      user: {
        username: 'akikoogawa7',
        firstName: 'Akiko',
        lastName: 'Ogawa',
        email: 'akiko.ogawaa@gmail.com',
        isAdmin: true
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
