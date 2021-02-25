<template>
  <div>認証</div>
</template>

<script>
export default {
  name: "callback",
  created: function () {
    this.$axios
      .get(process.env.VUE_APP_HOST + "/api/token", {
        params: {
          code: this.$route.query.code
        },
      })
      .then((res) => {
        localStorage.access_token = res.data.access_token;
      })
      .then(
        this.$router.push('result')
      )
      .catch(() => {
        console.log("なにかがおかしいよ")
      });
  },
};
</script>

<style></style>
