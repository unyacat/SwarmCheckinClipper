<template>
  <v-row>
    <v-col cols="4">
      <result-genre-circle :graph="graph" :options="options"/>
    </v-col>
    <v-col cols="8">
      <p> hogehoge </p>
    </v-col>
  </v-row>
</template>

<script>
import ResultGenreCircle from "@/ResultGenreCircle";
export default {
  name: "ResultGenre",
  components: {ResultGenreCircle},
  data() {
    return {
      graph: {
        // 凡例とツールチップに表示するラベル
        labels: [],
        // 表示するデータ
        datasets: [
          {
            data: [],
            backgroundColor: ['#ef5350', '#EC407A', '#AB47BC', '#7E57C2', '#5C6BC0', '#42A5F5', '#29B6F6', '#26C6DA',
              '#26A69A', '#66BB6A', '#9CCC65', '#D4E157', '#FFEE58', '#FFCA28', '#FFA726', '#FF7043'
            ]
          }
        ]
      },
      options: {
        legend: {
          display: false
        },
        responsive: true
      }
    }
  },
  mounted() {
    this.$axios.get(process.env.VUE_APP_HOST + "/api/rank/genre", {withCredentials: true}).then((res) => {
      res.data.forEach((genre) => {
            this.graph.labels.push(genre.vCategoryName)
            this.graph.datasets[0].data.push(genre.count)
          }
      )
    })
  }
}
</script>

<style scoped>

</style>