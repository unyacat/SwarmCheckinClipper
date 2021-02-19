<script>
import {Doughnut, mixins} from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  name: "ResultGenreCircle",
  mixins: [reactiveProp],
  extends: Doughnut,
  props: ['options'],
  mounted() {
    this.renderChart(this.chartData, this.options)
  }
}
</script>

<style scoped>

</style>