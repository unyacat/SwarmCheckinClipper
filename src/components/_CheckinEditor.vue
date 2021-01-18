<template>
  <v-list-item>
    <v-row class="my-n3">

<!--      <v-col cols="12" class="text&#45;&#45;secondary">-->
<!--        <v-row no-gutters style="width: 100%">-->
<!--          <v-col cols="12" md="5" lg="5" xl="5">-->
<!--            路線: {{ checkin.venue.name || "名前" }}-->
<!--          </v-col>-->
<!--          <v-col cols="6" md="3" lg="3" xl="3">-->
<!--            始点: {{ checkin.venue.location.lat || "未指定" }}-->
<!--          </v-col>-->
<!--          <v-col cols="6" md="3" lg="3" xl="3">-->
<!--            終点: {{ checkin.venue.location.lng || "未指定" }}-->
<!--          </v-col>-->
<!--        </v-row>-->
<!--      </v-col>-->
    </v-row>
    <v-row justify="end">
      <v-btn color="error" class="mr-4" @click="deleteCheckinEmit">
        <v-icon class="pr-6" dark right>mdi-delete</v-icon>
        削除
      </v-btn>
    </v-row>
  </v-list-item>
</template>

<script>
export default {
  name: "checkinEditor",
  props: ["checkin"],
  data: () => ({}),
  created: function () {
  },
  methods: {
    deleteCheckinEmit: function () {
      this.$emit("deleteCheckin", this.checkin.id);
    },
  }
};
</script>

<style scoped></style>
