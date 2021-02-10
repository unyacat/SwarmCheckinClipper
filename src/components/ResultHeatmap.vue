<template>
  <div>
    <calendar-heatmap
        v-if="count"
        :values="count"
        :end-date="endDate"
        tooltip-unit="checkins"
        :range-color="['#ebedf0', '#ffbe8c', '#ff9a60', '#ff8426', '#ff4f00']"
    ></calendar-heatmap>
  </div>
</template>

<script>
import {CalendarHeatmap} from 'vue-calendar-heatmap'
import dayjs from 'dayjs';

export default {
  name: "ResultHeatmap",
  components: {
    CalendarHeatmap
  },
  data() {
    return {
      endDate: dayjs().format("YYYY-MM-DD"),
      count: null
    }
  },
  mounted() {
    this.$axios.get(process.env.VUE_APP_HOST + "/api/checkin-freq", {withCredentials: true}).then(res => {
      this.count = res.data
    })
  }
}
</script>

<style scoped>

</style>