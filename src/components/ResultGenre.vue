<template>
  <v-row justify="center" align-content="center">
    <v-col cols="8" md="3" lg="2">
      <result-genre-circle v-if="chartData" :chart-data="chartData" :options="options"/>
    </v-col>
    <v-col cols="12" xs="8" sm="8" md="3" lg="3">
      <v-list-item two-line>
        <v-list-item-avatar>
          <v-img src="@/assets/medal_0001_01.png"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title> {{ chartData.labels[0] }} </v-list-item-title>
          <v-list-item-subtitle> {{ chartData.datasets[0].data[0] }} チェックイン</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-list-item two-line>
        <v-list-item-avatar>
          <v-img src="@/assets/medal_0001_02.png"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title> {{ chartData.labels[1] }} </v-list-item-title>
          <v-list-item-subtitle> {{ chartData.datasets[0].data[1] }} チェックイン</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-list-item two-line>
        <v-list-item-avatar>
          <v-img src="@/assets/medal_0001_03.png"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title> {{ chartData.labels[2] }} </v-list-item-title>
          <v-list-item-subtitle> {{ chartData.datasets[0].data[2] }} チェックイン</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-col>
  </v-row>
</template>

<script>
import ResultGenreCircle from "@/components/ResultGenreCircle";

export default {
  name: "ResultGenre",
  components: {ResultGenreCircle},
  data() {
    return {
      chartData: null,
      options: {
        legend: {
          display: false
        },
        responsive: true
      },
    }
  },
  mounted() {
    this.$axios.get(process.env.VUE_APP_HOST + "/api/rank/genre", {withCredentials: true}).then((res) => {
          const labels = res.data.map(genre => genre.vCategoryName)
          const counts = res.data.map(genre => genre.count)
          this.chartData = {
            // 凡例とツールチップに表示するラベル
            labels: labels,
            // 表示するデータ
            datasets: [
              {
                data: counts,
                backgroundColor: [
                  '#ef5350', '#EC407A', '#ab47bc', '#7E57C2',
                  '#5C6BC0', '#42A5F5', '#29B6F6', '#26C6DA',
                  '#26A69A', '#66BB6A', '#9CCC65', '#D4E157',
                  '#FFEE58', '#FFCA28', '#FFA726', '#FF7043'
                ]
              }
            ]
          }
        }
    )
  }
}
</script>

<style scoped>

</style>