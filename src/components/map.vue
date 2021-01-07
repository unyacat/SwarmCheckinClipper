<template>
  <div>
    <v-bottom-sheet v-model="sheet" class="floating-menu" scrollable>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            class="mx-2 floating-menu"
            fab
            dark
            large
            bottom
            right
            color="red"
            v-bind="attrs"
            v-on="on"
        >
          <v-icon dark>mdi-pencil</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-text style="height: 70%;">
          <v-list>
            <v-subheader>日付を選択</v-subheader>
            <v-list two-line>
              <template v-for="(checkin, index) in checkins">
<!--                <checkin-editor-->
<!--                    :checkin="checkin"-->
<!--                    :key="checkin.id"-->
<!--                    @deleteCheckin="deleteCheckin"-->
<!--                ></checkin-editor>-->
                <v-divider v-if="index + 1 < railroads.length" :key="index+10000"
                ></v-divider>
              </template>
            </v-list>
            <v-menu
                v-model="menu2"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                    v-model="startDate"
                    label="Picker without buttons"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                  v-model="startDate"
                  @input="menu2 = false"
              ></v-date-picker>
            </v-menu>
            <v-divider/>
            <v-subheader>保存する</v-subheader>
            <div class="add-button">
              <v-btn dark large color="green" @click="loadCheckins">
                <v-icon dark left>mdi-floppy</v-icon>
                読み込む
              </v-btn>
            </div>
            <div class="add-button">
              <v-btn dark large color="blue" @click="save">
                <v-icon dark left>mdi-floppy</v-icon>
                画像として保存
              </v-btn>
            </div>
          </v-list>
        </v-card-text>
      </v-card>
    </v-bottom-sheet>

    <l-map
        ref="basemap"
        id="mappreview"
        class="mapPane"
        :zoom="zoom"
        :center="center"
        :options="options"
    >
      <l-tile-layer
          :visible="true"
          url="https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png"
          attribution="Data <a href='https://www.openstreetmap.org/copyright'>© OpenStreetMap contributors</a>"
          layer-type="base"
      ></l-tile-layer>
      <!--      <l-tile-layer-->
      <!--        :visible="true"-->
      <!--        url="http://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png"-->
      <!--        layer-type="overlay"-->
      <!--      ></l-tile-layer>-->
            <l-circle
                v-for="checkin in checkins"
                :key="checkin.id"
                :lat-lng="checkin.latlng"
                :radius="100"
            >
              <l-popup :content="checkin.id"/>
            </l-circle>

    </l-map>

    <v-snackbar
        v-model="snackbar"
        timeout="3000"
    >
      {{ count }} 件のチェックインを読み込みました
    </v-snackbar>

  </div>
</template>

<script>
import L from "leaflet";
import {LMap, LTileLayer,
  LCircle,
   LPopup
} from "vue2-leaflet";

import "leaflet-easyprint";
// import CheckinEditor from "@/components/checkinEditor";
import moment from "moment";
export default {
  name: "basemap",
  components: {
    // CheckinEditor,
    LMap,
    LTileLayer,
    LCircle,
    LPopup
  },

  data() {
    return {
      center: [38, 135],
      zoom: 5,
      railroads: [],
      railways: [],
      sheet: false,
      uid: 1,
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
      dates: [],
      startDate: new Date().toISOString().substr(0, 10),
      menu2: false
    };
  },
  mounted() {
    this.$nextTick(function () {
      const vh = window.innerHeight * 0.01;
      document.documentElement.style.setProperty("--vh", `${vh}px`);
    });
  },
  created() {
    // TODO: withCredentials
    this.$axios.get("http://127.0.0.1/mock-allcheckins", { withCredentials: true }).then(res => {
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
      // res.data.checkins.items.forEach((item) => {
      //   L.circleMarker([item.venue.location.lat, item.venue.location.lng], {
      //   }).addTo(this.$refs.basemap.mapObject).bindPopup(item.id)
      // })
    });
  },
  methods: {
    save: function () {
      var p1080 = {
        width: 1920,
        height: 1080,
        className: "p1080class",
        tooltip: "1080p size"
      };

      const map = this.$refs.basemap.mapObject;
      const printPlugin = L.easyPrint({
        exportOnly: true,
        sizeModes: [p1080],
        hidden: true,
        tileLayer: L.tileLayer(
            "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
        ),
        tileWait: 500
      }).addTo(map);
      printPlugin.printMap("p1080class", "MyManualPrint");
    },
    deleteCheckin: function (toDeleteId) {
      const toDeleteIdx = this.checkins.findIndex(
          checkin => checkin.id === toDeleteId
      );
      this.checkins.splice(toDeleteIdx, 1);
    },
    loadCheckins: function () {
      console.log(moment(this.startDate).unix())
      console.log(moment(this.startDate).add(1, 'days').unix())
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

.floating-menu {
  z-index: 999;
  position: absolute;
  right: 1%;
  top: calc((var(--vh, 1vh) * 100) - 110px);
}

.add-button {
  z-index: 999;
  position: relative;
  display: inline-block;
  top: 50%;
  left: 50%;
  transform: translateX(-50%);
  margin-top: 20px;
  margin-bottom: 20px;
}

.easyPrintHolder .p1080class {
  background-image: url(data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTguMS4xLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDQ0NC44MzMgNDQ0LjgzMyIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNDQ0LjgzMyA0NDQuODMzOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgd2lkdGg9IjUxMnB4IiBoZWlnaHQ9IjUxMnB4Ij4KPGc+Cgk8Zz4KCQk8cGF0aCBkPSJNNTUuMjUsNDQ0LjgzM2gzMzQuMzMzYzkuMzUsMCwxNy03LjY1LDE3LTE3VjEzOS4xMTdjMC00LjgxNy0xLjk4My05LjM1LTUuMzgzLTEyLjQ2N0wyNjkuNzMzLDQuNTMzICAgIEMyNjYuNjE3LDEuNywyNjIuMzY3LDAsMjU4LjExNywwSDU1LjI1Yy05LjM1LDAtMTcsNy42NS0xNywxN3Y0MTAuODMzQzM4LjI1LDQzNy4xODMsNDUuOSw0NDQuODMzLDU1LjI1LDQ0NC44MzN6ICAgICBNMzcyLjU4MywxNDYuNDgzdjAuODVIMjU2LjQxN3YtMTA4LjhMMzcyLjU4MywxNDYuNDgzeiBNNzIuMjUsMzRoMTUwLjE2N3YxMzAuMzMzYzAsOS4zNSw3LjY1LDE3LDE3LDE3aDEzMy4xNjd2MjI5LjVINzIuMjVWMzR6ICAgICIgZmlsbD0iIzAwMDAwMCIvPgoJPC9nPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+Cjwvc3ZnPgo=);
}
</style>
