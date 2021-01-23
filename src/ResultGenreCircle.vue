<script>
import {Doughnut, mixins} from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  name: "ResultGenreCircle",
  mixins: [reactiveProp],
  extends: Doughnut,
  props: ['graph', 'options'],
  mounted() {
    this.renderChart(this.graph, this.options)
  }
}
</script>

<style scoped>

</style>