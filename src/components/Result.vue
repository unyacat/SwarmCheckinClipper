<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="8">
        <div class="text-center text-sm-h5 text-md-h4">
          チェックイン数
        </div>
      </v-col>
      <v-col cols="8">
        <div class="text-center text-sm-h3 text-md-h2">
          <AnimatedNumber number="7777" />
        </div>
      </v-col>

      <v-col cols="8">
        <p class="text-center text-sm-h5 text-md-h4">
          ジャンル別
        </p>
      </v-col>
      <v-col cols="12">
        <result-genre />
      </v-col>
      <v-col cols="8">
        <p class="text-center text-sm-h5 text-md-h4">
          チェックイン回数
        </p>
      </v-col>
      <v-col cols="12">
        <result-venue />
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
import ResultGenre from "@/components/ResultGenre";
import AnimatedNumber from "@/components/AnimatedNumber";
import ResultVenue from "@/components/ResultVenue";


export default {
  name: "result",
  components: {ResultVenue, AnimatedNumber, ResultGenre},
}
</script>

<style scoped>

</style>