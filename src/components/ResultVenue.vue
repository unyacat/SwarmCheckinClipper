<template>
  <v-row justify="center">
    <v-col cols="4">
      <v-list-item two-line>
        <v-list-item-avatar>
          <v-img src="@/assets/medal_0001_01.png"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title> 〇〇駅 </v-list-item-title>
          <v-list-item-subtitle> 125 チェックイン</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-list-item two-line>
        <v-list-item-avatar>
          <v-img src="@/assets/medal_0001_02.png"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title> □□ビル </v-list-item-title>
          <v-list-item-subtitle> 8 チェックイン</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-list-item two-line>
        <v-list-item-avatar>
          <v-img src="@/assets/medal_0001_03.png"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title> ねこ </v-list-item-title>
          <v-list-item-subtitle> 2 チェックイン</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-col>
  </v-row>
</template>

<script>

export default {
  name: "ResultGenre",
  data() {
    return {
    }
  },
  mounted() {
  }
}
</script>

<style scoped>

</style>