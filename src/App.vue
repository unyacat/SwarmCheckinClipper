<template>
  <v-app>
    <v-main>
<!--      <Map />-->
      <Result />
    </v-main>
  </v-app>
</template>

<script>
// import Map from "@/components/map";
import Result from "./components/result";

export default {
  name: 'App',

  components: {
    Result,
    // Map,
  },

  data: () => ({
    //
  }),
};
</script>
