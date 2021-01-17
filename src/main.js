import Vue from "vue";
import App from "./App.vue";
import axios from "axios";
// import store from './store';
import router from './router'

//ここから
import { Icon } from "leaflet";
import "leaflet/dist/leaflet.css";
import vuetify from "./plugins/vuetify";
//ここまで


import L from 'leaflet';
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});
// this part resolve an issue where the markers would not appear
delete Icon.Default.prototype._getIconUrl;

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;

if (window.location.hash === "#_=_"){
  history.replaceState
    ? history.replaceState(null, null, window.location.href.split("#")[0])
    : window.location.hash = "";
}


new Vue({
  vuetify,
  // store,
  router,
  render: h => h(App)
}).$mount("#app");
