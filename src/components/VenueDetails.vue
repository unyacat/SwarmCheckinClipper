<template>
  <div>
    <v-app-bar
        app
        color="#ffa633"
    >
      <v-container class="py-0 fill-height">
        <v-toolbar-title class="white--text">Swarm Analyzer</v-toolbar-title>
      </v-container>
    </v-app-bar>


    <v-container>
      <div style="height: 300px; width: 100%">
        <VenueMap :latlng="latlng"/>
      </div>
      <v-layout>
        <v-row>
          <v-col cols="12">
            <p class="text-h3">
              {{ name }}
            </p>
            <p class="text-h5">
              {{ category }}
            </p>
          </v-col>
        </v-row>
      </v-layout>

      <v-simple-table>
        <thead>
        <tr>
          <th class="text-left">
            チェックイン日時
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="checkin in checkins" :key="checkin.cId">
          <td> {{ unixToRealtime(checkin.cCreatedAt) }}</td>
        </tr>
        </tbody>
      </v-simple-table>
    </v-container>
  </div>
</template>

<script>
// import AnimatedNumber from "./AnimatedNumber";
import dayjs from "dayjs";
import VenueMap from "@/components/VenueMap";

export default {
  name: "result",
  components: {VenueMap},
  // components: {AnimatedNumber},
  props: ['venueId'],
  data() {
    return {
      name: "",
      category: "",
      latlng: [135, 35],
      checkins: []
    }
  },
  mounted() {
    this.$axios.get(process.env.VUE_APP_HOST + "/api/venue/" + this.venueId, {withCredentials: true}).then((res) => {
      this.checkins = res.data
      this.latlng = [res.data[0].vLat, res.data[0].vLng]
      this.name = res.data[0].vName
      this.category = res.data[0].vCategoryNam
      console.log(this.latlng)
    })
  },
  methods: {
    unixToRealtime(unixtime) {
      return dayjs.unix(unixtime).format("YYYY/MM/DD HH:mm:ss")
    }
  }
}
</script>

<style scoped>
.container {
  max-width: calc(min(1200px, 95%))
}
</style>