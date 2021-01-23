import Vue from 'vue'
import Router from 'vue-router'
import Cookie from 'vue-cookies'
import Home from './Top'
import map from './components/BaseMap'
import VenueDetails from "@/components/VenueDetails";
import DayCheckins from "@/components/DayCheckins";
import Result from "@/components/Result";

Vue.use(Router)
Vue.use(Cookie)


const router = new Router(
{
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {
        isPublic: true
      }
    },
    {
      path: '/result',
      name: 'result',
      component: Result
    },
    {
      path: '/map',
      name: 'map',
      component: map
    },
    {
      path: '/venue/:venueId',
      name: 'venue',
      component: VenueDetails,
      props: true
    },
    {
      path: '/day/:day',
      name: 'day-checkins',
      component: DayCheckins,
      props: true
    },
    {
      path: '/auth',
      beforeEnter() {location.href = process.env.VUE_APP_HOST + '/auth'},
      meta: {
        isPublic: true
      }
    },
    {
      name: 'notfound',
      path: '*',
      redirect: '/'
    }
  ]
})

router.beforeEach((to, from, next) => {
  const sessionId = Vue.$cookies.get('sessionId');
  if (to.matched.some(record => !record.meta.isPublic) && sessionId) {
    next({ path: '/'});
  } else {
    next();
  }
});


export default router;


// Router.beforeEach((to, from, next) => {
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
  // if (store.state.isLoggedIn) {
  //   next()
  // }
  // else {
  //   next('/login')
  // }
// })
