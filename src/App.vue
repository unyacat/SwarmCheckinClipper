<template>
  <v-app>
    <v-main>
<!--      <Map />-->
<!--      <Result />-->
      <Home />
    </v-main>
  </v-app>
</template>

<script>
import Home from './Home'

export default {
  name: 'App',

  components: {
    Home
    // Map,
  },

  data: () => ({
    //
  }),
};
</script>
