<template>
  <v-app id="inspire">

    <v-app-bar
        app
        color="#ffa633"
    >
      <v-container class="py-0 fill-height">
        <v-toolbar-title class="white--text">Swarm Analyzer</v-toolbar-title>
      </v-container>
    </v-app-bar>


    <v-main>
      <v-container>
        <v-layout>
          <v-row>
            <v-col cols="12">
              <p class="text-h3">
                {{ this.formatDay }}
              </p>
            </v-col>
          </v-row>

        </v-layout>
        <v-timeline dense>
          <v-timeline-item
              class="mb-4"
              icon-color="grey lighten-2"
              v-for="checkin in checkins" :key="checkin.cId"
          >
            <v-row justify="space-between">
              <v-col cols="7">
                {{ checkin.vName }}
              </v-col>
              <v-col
                  class="text-right"
                  cols="5"
              >
                {{ unixtimeToHourMinutes(checkin.cCreatedAt) }}
              </v-col>
            </v-row>
          </v-timeline-item>
        </v-timeline>
      </v-container>
    </v-main>
  </v-app>
</template>


<script>
import dayjs from "dayjs";
export default {
  name: "PeriodCheckins",
  props: ['day'],
  data() {
    return {
      formatDay: "",
      checkins: []
    }
  },
  mounted() {
    this.formatDay = dayjs(this.day).format("YYYY年MM月DD日")
    this.$axios.get( process.env.VUE_APP_HOST + "/api/day/" + this.day, {withCredentials: true}).then((res) => {
      this.checkins = res.data
    }).catch(() => {
      console.log("なにかがおかしいよ")
    })
  },
  methods: {
    unixtimeToHourMinutes(unixtime) {
      return dayjs.unix(unixtime).format("HH:mm")
    }
  }
}
</script>

<style scoped>
.container {
  max-width: calc(min(1200px, 95%))
}
</style>