<template>
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
</template>

<script>
import dayjs from "dayjs";

export default {
  name: "VenueCard",
  props: {
    checkin: {
      type: Object,
      required: true
    }
  },
  methods: {
    lastCheckinTime(unixtime) {
      return dayjs.unix(unixtime).format("YYYY/MM/DD HH:mm:ss")
    }
  }
}
</script>

<style scoped>
.popup {
  width: 500px;
}
</style>