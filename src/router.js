import Vue from 'vue'
import Router from 'vue-router'
import Home from './Home'
import map from './components/map'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/map',
      name: 'map',
      component: map
    }
  ]
})


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
