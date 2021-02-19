<template>
  <div>
    <div class="venue-map">
      <l-map
          v-if="latlng"
          :zoom="zoom"
          :center="latlng"
          :options="options"
      >
        <l-tile-layer
            :visible="true"
            url="	https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="Data <a href='https://www.openstreetmap.org/copyright'>© OpenStreetMap contributors</a>"
            layer-type="base"
        ></l-tile-layer>
        <l-circle
            v-for="checkin in checkins"
            :key="checkin.cCreatedAt"
            :lat-lng="[checkin.vLat, checkin.vLng]"
            :radius="circle.radius"
            :color="circle.color"
            :fillColor="circle.fillColor"
            :fillOpacity="circle.fillOpacity"
        />
      </l-map>
    </div>
    <v-container>
      <v-layout>
        <v-row>
          <v-col cols="12">
            <p class="text-h4 text-sm-h3">
              {{ formatDay }}
            </p>
          </v-col>
        </v-row>

      </v-layout>
      <v-timeline dense>
        <v-timeline-item
            class="mb-6"
            icon-color="grey lighten-2"
            v-for="checkin in checkins" :key="checkin.cId"
        >
          <template v-slot:icon>
            <v-avatar>
              <img :src="checkin.vCategoryIcon">
            </v-avatar>
          </template>
          <v-row justify="space-between">
            <v-col cols="10">
              <router-link :to="/venue/ + checkin.vId"
                           style="text-decoration: none; color: black">

                <div class="text-h6">
                  {{ checkin.vName }}
                </div>
                <div v-if="checkin.cShout">
                  「{{ checkin.cShout }}」
                </div>
              </router-link>
            </v-col>
            <v-col class="text-right" cols="1">
              {{ unixtimeToHourMinutes(checkin.cCreatedAt) }}
            </v-col>
            <v-col
                cols="1"
            >
              <a :href=" 'https://www.swarmapp.com/checkin/' + checkin.cId " style="text-decoration: none; color: black"
                 target="_blank" rel="noopener">
                <v-icon>
                  mdi-arrow-top-right
                </v-icon>
              </a>
            </v-col>
          </v-row>
        </v-timeline-item>
      </v-timeline>
    </v-container>
  </div>
</template>


<script>
import dayjs from "dayjs";
import {LCircle, LMap, LTileLayer} from "vue2-leaflet";

export default {
  name: "DayCheckins",
  props: ['day'],
  components: {
    LMap,
    LTileLayer,
    LCircle
  },
  data() {
    return {
      formatDay: "",
      checkins: [],
      latlng: [38, 135],
      circle: {
        radius: 100,
        color: "orange",
        fillColor: "orange",
        fillOpacity: 1
      },
      options: {
        useCache: true,
        zoomControl: false,
        crossOrigin: true,
        preferCanvas: true,
      },
      zoom: 12
    }
  },
  mounted() {
    this.formatDay = dayjs(this.day).format("YYYY年MM月DD日")
    this.$axios.get(process.env.VUE_APP_HOST + "/api/day/" + this.day, {withCredentials: true}).then((res) => {
      this.checkins = res.data
      this.latlng = [res.data[0].vLat, res.data[0].vLng]
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

.venue-map {
  height: 400px;
  max-height: 35vh;
  width: 100%
}


</style>