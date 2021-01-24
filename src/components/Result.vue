<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="8">
        <p class="text-sm-h5 text-md-h4">
          ジャンル別
        </p>
      </v-col>
      <v-col cols="12">
        <result-genre/>
      </v-col>
      <v-col cols="12">
        <div class="text-h3 text-sm-h3 text-md-h3 text-lg-h2 text-xl-h2 text-center white--text">
          Swarm Analyzer
        </div>
      </v-col>
      <v-col cols="12">
        <div class="text-h5 text-center white--text">
          Swarm のチェックインを地図にプロットするだけ
        </div>
      </v-col>

      <v-col>
        <div class="text-center">
          (作業中)
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ResultGenre from "@/components/ResultGenre";


export default {
  name: "result",
  components: {ResultGenre},
}
</script>

<style scoped>

</style>