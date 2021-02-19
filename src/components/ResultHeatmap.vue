<template>
  <div>
    <calendar-heatmap
        cols="12" md="8" lg="8" xl="8"
        v-if="count"
        :values="count"
        :end-date="endDate"
        tooltip-unit="checkins"
        :locale="locale"
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
      count: null,
      locale: {
        months: ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
        days: ['日', '月', '火', '水', '木', '金', '土']
      }
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