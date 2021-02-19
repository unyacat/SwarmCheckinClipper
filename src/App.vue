<template>
  <v-app>
    <v-app-bar
        color="#ffa633"
        style="z-index: 9999"
        absolute
        height="64px"
        app
    >
      <v-container class="py-0 fill-height">
        <router-link to="/result" style="text-decoration: none;">
          <v-toolbar-title class="white--text">Swarm Analyzer</v-toolbar-title>
        </router-link>
      </v-container>
    </v-app-bar>
    <v-main>
      <keep-alive include="basemap">
        <router-view/>
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
