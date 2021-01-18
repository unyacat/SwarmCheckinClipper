<template>
  <v-app>
    <v-main>
      <keep-alive include="basemap">
        <router-view />
      </keep-alive>
    </v-main>
  </v-app>
</template>

<script>
// import Home from './Home'

export default {
  name: 'App',

  components: {
    // Home
    // Map,
  },

  data: () => ({
    //
  }),
};
</script>
