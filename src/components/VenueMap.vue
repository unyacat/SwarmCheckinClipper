<template>
  <l-map
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
        :lat-lng="latlng"
        :radius="circle.radius"
        :color="circle.color"
        :fillColor="circle.fillColor"
        :fillOpacity="circle.fillOpacity"
    />
  </l-map>
</template>

<script>
import {LMap, LTileLayer, LCircle} from "vue2-leaflet";

export default {
  name: "VenueMap",
  components: {
    LMap,
    LTileLayer,
    LCircle
  },
  props: ['latlng'],
  mounted() {
    console.log(this.latlng)
  },
  data() {
    return {
      zoom: 15,
      circle: {
        radius: 30,
        color: "orange",
        fillColor: "orange",
        fillOpacity: 1
      },
      options: {
        useCache: true,
        zoomControl: false,
        crossOrigin: true,
        preferCanvas: true,
      }
    }
  }
}
</script>

<style scoped>

</style>