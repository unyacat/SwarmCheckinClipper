<template>
  <div>
      <div class="venue-map">
        <VenueMap :latlng="latlng"/>
      </div>
      <v-container>
        <v-layout>
          <v-row>
            <v-col cols="12">
              <p class="text-sm-h4 text-md-h3">
                {{ name }}
              </p>
              <p class="text-sm-h5 text-md-h4">
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
            <td>
              <router-link :to="/day/ + unixToYMD(checkin.cCreatedAt)"
                           style="text-decoration: none; color: black">
                {{ unixToRealtime(checkin.cCreatedAt) }}
              </router-link>
            </td>
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
      this.category = res.data[0].vCategoryName
    })
  },
  methods: {
    unixToRealtime(unixtime) {
      return dayjs.unix(unixtime).format("YYYY/MM/DD HH:mm:ss")
    },
    unixToYMD(unixtime) {
      return dayjs.unix(unixtime).format("YYYYMMDD")
    }
  }
}
</script>

<style scoped>
.container {
  max-width: calc(min(1200px, 95%))
}

.venue-map {
  height: 300px;
  max-height: 35vh;
  width: 100%
}

</style>