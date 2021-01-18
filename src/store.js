import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

const initialState = {
  checkins: []
}
// ストアの定義
const store = new Vuex.Store({
  // ステート、ミューテーションなどをここに記載 https://qiita.com/yoshi0518/items/6d08ee6b71e47d70e4bc#%E3%82%B9%E3%83%86%E3%83%BC%E3%83%88
  state: initialState,
  mutations: {
    setCheckins(state, payload) {
      state.checkins = payload.checkins
    }
  },
  plugins: [createPersistedState()]
})

// ストアをエクスポート
export default store