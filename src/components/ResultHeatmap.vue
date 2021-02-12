<template>
  <div>
    <calendar-heatmap
        cols="12" md="8" lg="8" xl="8"
        v-if="count"
        :values="count"
        :end-date="endDate"
        tooltip-unit="checkins"
        :range-color="['#ebedf0', '#ffbe8c', '#ff9a60', '#ff8426', '#ff4f00']"
        @day-click="handleDayClick"
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
  },
  methods: {
    handleDayClick(day) {
      day = Math.floor(day.date.getTime())
      day = dayjs(day).format("YYYYMMDD")
      this.$router.push("/day/" + day)
    }
  }
}
</script>

<style scoped>

</style>