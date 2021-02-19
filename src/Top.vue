<template>
  <v-img
      src="@/assets/timo-wielink-4Zk45jNyQS4-unsplash.jpg"
      gradient="to top, rgba(80,95,181,.33), rgba(25,32,72)"
      height="100vh"
  >
    <v-container>
      <v-row justify="center" align-content="center" style="height: 450px">
        <v-spacer/>
        <v-col cols="12">
          <div class="text-h3 text-sm-h3 text-md-h3 text-lg-h2 text-xl-h2 text-center white--text">
            Swarm Analyzer
          </div>
        </v-col>
        <v-col cols="12">
          <div class="text-h5 text-center white--text">
            Swarm のチェックインを地図にプロットするだけ
          </div>
        </v-col>

        <v-col cols="12">
          <div class="text-center">
            <router-link to="/auth">
              <v-btn elevation="2" color="orange" class="white--text">
                Authenticate with Foursquare
              </v-btn>
            </router-link>
          </div>
        </v-col>
        <v-col>
          <div class="text-center">
            (作業中)
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-img>
</template>

<script>
export default {
  name: "Home"
}
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>