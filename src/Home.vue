<template>
  <v-main class="bg">
    <v-container>
      <v-row justify="center" align-content="center" style="height: 450px">
        <v-spacer />
        <v-col cols="12">
          <div class="text-h3 text-sm-h3 text-md-h3 text-lg-h2 text-xl-h2 text-center">
            Swarm Mapper
          </div>
        </v-col>
        <v-col cols="12">
          <div class="text-h5 text-center">
            Swarm のチェックインを地図にプロットするだけ
          </div>
        </v-col>

        <v-col cols="12">
          <div class="text-center">
            <router-link to="/map">
              <v-btn elevation="2" color="orange" class="white--text">
                Authenticate with Foursquare
              </v-btn>
            </router-link>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
export default {
  name: "Home"
}
</script>

<style scoped>
  .bg {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background-size: cover;
    background-image: url("");
  }
  a {
    text-decoration: none;
  }
</style>