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
          url="https://cyberjapandata.gsi.go.jp/xyz/blank/{z}/{x}/{y}.png"
          attribution="Data <a href='https://www.openstreetmap.org/copyright'>© OpenStreetMap contributors</a>"
          layer-type="base"
      ></l-tile-layer>
      <l-circle
          v-for="checkin in checkins"
          :key="checkin.venue.id"
          :lat-lng="checkin.venue.location.latlng"
          :radius="circle.radius"
          :color="circle.color"
          :fillColor="circle.fillColor"
          :fillOpacity="circle.fillOpacity"
      >
        <l-popup>
          <v-card elevation="0" class="popup">
            <v-list-item dense>
              <v-list-item-avatar>
                <v-img :src="checkin.venue.categories.icon"></v-img>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-card-title v-text="checkin.venue.name"/>
                <v-card-subtitle v-text="checkin.venue.categories.name"/>
              </v-list-item-content>
            </v-list-item>
            <v-list-item dense>
              <v-list-item-title>最終チェックイン</v-list-item-title>
              <v-list-item-subtitle class="text-right"
                                    v-text="lastCheckinTime(checkin.createdAt[0])"></v-list-item-subtitle>
            </v-list-item>
            <v-list-item dense>
              <v-list-item-title>チェックイン回数</v-list-item-title>
              <v-list-item-subtitle class="text-right"> {{ checkin.createdAt.length }} 回</v-list-item-subtitle>
            </v-list-item>
          </v-card>
        </l-popup>

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

// import L from "leaflet"
import "leaflet-easyprint";
import dayjs from "dayjs";

// import popupCard from "@/components/popupCard";

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
    this.$axios.get(process.env.VUE_APP_HOST + "/checkins", {withCredentials: true}).then(res => {
      this.snackbar = true
      this.count = res.data.checkins.count;
      // this.checkins = res.data.checkins.items;
      // this.checkins = Object.freeze(res.data.checkins.items)
      this.checkins = this.deepFreeze(res.data.checkins.items)
    }).then(() => {
      // this.checkins.forEach((checkin) => {
      //       L.circle(checkin.venue.location.latlng, 500).addTo(this.$refs.basemap.mapObject).bindPopup(
      //           checkin.venue.name
      //       )
      //     }
      // )
      this.loading = false
    }).catch(() => {
      console.log("エラー処理")
      this.loading = false
      this.dialog = true
    });
  },
  methods: {
    deepFreeze(obj) {
      Object.keys(obj).forEach(prop => {
        if (typeof obj[prop] === 'object' && !Object.isFrozen(obj[prop])) this.deepFreeze(obj[prop]);
      });
      return Object.freeze(obj);
    },
    zoomUpdated(zoom) {
      console.log(zoom)
      // return 0
      // const radius = [100, 100, 100, 100, 100, 100, 100, 100, 300, 300, 100, 100, 50, 50, 10, 10, 10, 10, 10]
      // this.$set(this.circle, 'radius', radius[zoom - 1])
    },
    lastCheckinTime(unixtime) {
      return dayjs.unix(unixtime).format("YYYY/MM/DD HH:mm:ss")
    }
  }
}
</script>


<style>
.leaflet-popup-content-wrapper {
  border-radius: 5px !important;
}

.leaflet-popup-content {
  margin: 0 0 !important;
}
</style>


<style scoped>
.mapPane {
  height: calc(1vh * 100);
  margin: 0;
  text-align: left;
}

.popup {
  width: 500px;
}

</style>


