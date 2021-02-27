<template>
  <div>
    <v-btn class="ma-2" color="primary" dark @click="load"> 読み込む </v-btn>
  </div>
</template>

<script>
export default {
  name: "load-checkins",
  created: function () {
    if (localStorage.getItem("access_token") === null) {
      this.$router.push("/");
    }
  },
  methods: {
    load() {
      this.$axios
        .get(process.env.VUE_APP_HOST + "/api/load_checkins", {
          headers: {
            Authorization: "Bearer " + localStorage.access_token,
          },
        })
        .then(this.$router.push("result"));
    },
  },
};
</script>

<style></style>
