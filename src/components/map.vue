<template>
  <div>
    <l-map
        ref="basemap"
        id="mappreview"
        class="mapPane"
        :zoom="zoom"
        :center="center"
        :options="options"
        @update:zoom="zoomUpdated"
    >
      <l-tile-layer
          :visible="true"
          url="https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png"
          attribution="Data <a href='https://www.openstreetmap.org/copyright'>© OpenStreetMap contributors</a>"
          layer-type="base"
      ></l-tile-layer>
      <l-circle
          v-for="checkin in checkins"
          :key="checkin.id"
          :lat-lng="checkin.latlng"
          :radius="circle.radius"
          :color="circle.color"
          :fillColor="circle.fillColor"
          :fillOpacity="circle.fillOpacity"
      >
        <l-popup :content="checkin.id"/>
      </l-circle>

    </l-map>

    <v-dialog
        v-model="loading"
        persistent
        width="500"
        style="z-index: 999"
    >
      <v-card
          color="primary"
          dark
      >
        <v-card-text>
          全チェックインを読込中です...
          <v-progress-linear
              indeterminate
              color="white"
              class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-dialog
        v-model="dialog"
        persistent
        width="300"
        style="z-index: 999"
    >
      <v-card>
        <v-card-title class="headline">読み込みエラー</v-card-title>
        <v-card-text>何かがおかしいよ</v-card-text>
      </v-card>
    </v-dialog>


    <v-snackbar
        v-model="snackbar"
        timeout="3000"
    >
      {{ count }} 件のチェックインを読み込みました
    </v-snackbar>


  </div>
</template>

<script>
import {
  LMap,
  LTileLayer,
  LCircle,
  LPopup
} from "vue2-leaflet";

import "leaflet-easyprint";

export default {
  name: "basemap",
  components: {
    LMap,
    LTileLayer,
    LCircle,
    LPopup
  },

  data() {
    return {
      center: [38, 135],
      zoom: 5,
      options: {
        useCache: true,
        zoomControl: false,
        crossOrigin: true,
        preferCanvas: true,
        style: function style() {
          return {
            weight: 4,
            color: "#0000FF",
            fillOpacity: 0.3
          };
        }
      },
      checkins: [],
      snackbar: false,
      count: 0,
      loading: false,
      dialog: false,
      circle: {
        radius: 100,
        color: "orange",
        fillColor: "orange",
        fillOpacity: 1
      }
    };
  },
  mounted() {
    this.$nextTick(function () {
      const vh = window.innerHeight * 0.01;
      document.documentElement.style.setProperty("--vh", `${vh}px`);
      this.loading = true
    });
  },

  created() {
    this.$axios.get("http://127.0.0.1/mock-allcheckins", {withCredentials: true}).then(res => {
      this.snackbar = true
      this.count = res.data.checkins.count;
      res.data.checkins.items.forEach((item) => {
            this.checkins.push(
                {
                  "latlng": [item.venue.location.lat, item.venue.location.lng],
                  "id": item.id
                })
          }
      )
      this.checkins = Object.freeze(this.checkins)
    }).then(() => {
      this.loading = false
    }).catch(() => {
      console.log("エラー処理")
      this.loading = false
      this.dialog = true
    });
  },
  methods: {
    zoomUpdated(zoom) {
      const radius = [100, 100, 100, 100, 100, 100, 100, 100, 300, 300, 100, 100, 50, 50, 10, 10, 10, 10, 10]
      this.$set(this.circle, 'radius', radius[zoom - 1])
    }
  }
};
</script>

<style scoped>
.mapPane {
  height: calc(var(--vh, 1vh) * 100);
  margin: 0;
  text-align: left;
}

</style>
