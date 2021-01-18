<template>
  <v-app id="inspire">

    <v-app-bar
        app
        color="#ffa633"
    >
      <v-container class="py-0 fill-height">
        <v-toolbar-title class="white--text"> Swarm Analyzer 2020</v-toolbar-title>
      </v-container>
    </v-app-bar>



    <v-main>
      <v-container>
        <v-row>
          <v-col cols="12">
            Years in Review
            <animated-number v-bind:number="2020" />
          </v-col>
          <v-col
              v-for="n in 24"
              :key="n"
              cols="4"
          >
            <v-card height="200"></v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>

      <v-footer
    dark
    padless
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title class="teal">
        <strong class="subheading">🐝 正しい行動を取り、外出を控えましょう</strong>

        <v-spacer></v-spacer>

      </v-card-title>

      <v-card-text class="py-2 white--text text-center">
        © 2020 unyacat.net
      </v-card-text>
    </v-card>
  </v-footer>
  </v-app>
</template>

<script>
import AnimatedNumber from "./AnimatedNumber";
export default {
  name: "result",
  components: {AnimatedNumber}
}
</script>

<style scoped>

</style>