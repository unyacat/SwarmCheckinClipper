<template>
  <v-row justify="center">
    <v-col cols="12" xs="8" sm="8">
      <div>
        <v-list-item two-line>
          <v-list-item-avatar>
            <v-img src="@/assets/medal_0001_01.png"></v-img>
          </v-list-item-avatar>
          <v-list-item-content >
            <v-list-item-title> {{ ranks[0].vName }} </v-list-item-title>
            <v-list-item-subtitle> {{ ranks[0].count }} チェックイン</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item two-line>
          <v-list-item-avatar>
            <v-img src="@/assets/medal_0001_02.png"></v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title> {{ ranks[1].vName }} </v-list-item-title>
            <v-list-item-subtitle> {{ ranks[0].count }} チェックイン</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item two-line>
          <v-list-item-avatar>
            <v-img src="@/assets/medal_0001_03.png"></v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title> {{ ranks[2].vName }} </v-list-item-title>
            <v-list-item-subtitle> {{ ranks[0].count }} チェックイン</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </div>
    </v-col>
  </v-row>
</template>

<script>

export default {
  name: "ResultGenre",
  data() {
    return {
      ranks: []
    }
  },
  mounted() {
    this.$axios.get(process.env.VUE_APP_HOST + "/api/rank/venue", {withCredentials: true}).then((res) => {
      this.ranks = res.data
      console.log(this.ranks)
    })
  }
}
</script>

<style scoped>

</style>