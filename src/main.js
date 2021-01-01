import Vue from "vue";
import App from "./App.vue";
import Login from './Home';
import axios from "axios";
import store from './store';
import Router from 'vue-router'
Vue.use(Router)

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

const router = new Router({
  routes: [
    {
      path: "/",
      component: App,
      beforeEnter: (to, from, next) => {
        next('/login');
      }
    },
    {
      path: "/login",
      name: "top",
      component: Login,
      beforeEnter: (to, from, next) => {
        next('/login');
      }
    },
  ],
  // routes: `ルーティング設定を記述 (略)`
})

router.beforeEach((to, from, next) => {
  // トークンが存在、かつログイン有効期限を過ぎてない場合、またはログイン画面の場合
  // if ((store.state.auth.login.token && store.state.auth.login.expire > (new Date()).getTime()) || to.matched.some(page => {
  //   // ログイン画面はリダイレクト対象外 (他にも404ページなどいくつか対象外にする必要があるかも)
  //   return (page.path === '/login')
  // })) {
  //   next()
  // } else {
  //   // ログイン画面に飛ばす。ログイン後に元の画面に戻れるよう、backuriパラメーターにリダイレクト前のURLを入れる
  //   next({path: '/login', query: {backuri: to.fullPath}})
  // }
  if (store.state.isLoggedIn) {
    next()
  }
  else {
    next('/login')
  }
})



new Vue({
  vuetify,
  store,
  render: h => h(App)
}).$mount("#app");
