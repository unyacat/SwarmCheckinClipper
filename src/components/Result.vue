<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="8">
        <div class="text-center text-sm-h5 text-md-h4">
          チェックイン数
        </div>
      </v-col>

      <v-col cols="12" md="8" lg="8" xl="8">
        <div class="text-center text-h2 text-sm-h2">
          <AnimatedNumber number="7777"/>
        </div>
      </v-col>

      <v-col cols="12">
        <p class="text-center text-sm-h5 text-md-h4">
          ジャンル別
        </p>
        <result-genre />
      </v-col>
      <v-col cols="12" md="8" lg="6" xl="6">
        <p class="text-center text-sm-h5 text-md-h4">
          チェックイン回数
        </p>
        <result-venue />
      </v-col>
      <v-col cols="12" md="8" lg="8" xl="8">
        <p class="text-center text-sm-h5 text-md-h4">
          チェックインヒートマップ
        </p>
      </v-col>
      <v-col cols="12" md="8" lg="8" xl="8">
        <result-heatmap />
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
import ResultGenre from "@/components/ResultGenre";
import AnimatedNumber from "@/components/AnimatedNumber";
import ResultVenue from "@/components/ResultVenue";
import ResultHeatmap from "@/components/ResultHeatmap";


export default {
  name: "result",
  components: {ResultHeatmap, ResultVenue, AnimatedNumber, ResultGenre},
}
</script>

<style scoped>

</style>