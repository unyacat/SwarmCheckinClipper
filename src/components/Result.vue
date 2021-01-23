<template>
 <v-container>
   <v-row>
     <v-spacer/>
     <v-col cols="4">
       <result-genre-circle />
     </v-col>
     <v-col cols="8">

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
import { Doughnut } from 'vue-chartjs'
import ResultGenreCircle from "@/ResultGenreCircle";


export default {
  name: "result",
  components: {ResultGenreCircle},
  extends: Doughnut,

}
</script>

<style scoped>

</style>