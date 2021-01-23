

<script>
import {Doughnut} from 'vue-chartjs'


export default {
  name: "ResultGenreCircle",
  extends: Doughnut,
  data() {
    return {
      sample: {
        // 凡例とツールチップに表示するラベル
        labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        // 表示するデータ
        datasets: [
          {
            data: [10, 15, 6, 22, 11, 49, 32],
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
    this.renderChart(this.sample, this.options)
  }
}
</script>

<style scoped>

</style>