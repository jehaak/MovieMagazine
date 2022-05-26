//*****************************************
// 받아오는 로직 만들기
// 받아온 정보에서 local_id나 id 밸류값 안겹치게 수정
//****************************************8

import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

// import _ from 'lodash'
// import accounts from './accounts'

export default {
  // namespaced: true,
  state: {
    recentMovies: [],
    hotMovies: [],
    directorSearchResult: [],
    actorSearchResult: [],
    movieSearchResult: [],
    perfectDirectorResult: [],
    perfectActorResult: [],
    perfectMovieResult: [],
    keyword: '',
    isEnter: '',
    choicedGenres: [],
    actorprofile: [],
    directorprofile: [],
    moviedetail: [],
  },

  getters: {
    recentMovies: state => state.recentMovies,
    hotMovies: state => state.hotMovies,
    directorSearchResult: state => state.directorSearchResult,
    actorSearchResult: state => state.actorSearchResult,
    movieSearchResult: state => state.movieSearchResult,
    perfectDirectorResult: state => state.perfectDirectorResult,
    perfectActorResult: state => state.perfectActorResult,
    perfectMovieResult: state => state.perfectMovieResult,
    keyword: state => state.keyword,
    isEnter: state => state.isEnter,
    choicedGenres: state => state.genre,
    actorprofile: state => state.actorprofile,
    directorprofile: state => state.directorprofile,
    moviedetail: state => state.moviedetail,
  },

  mutations: {
    SET_HOME_VIEW: function (state, data) {
      // console.log(data)
      state.recentMovies = data.recent_movie
      state.hotMovies = data.hot_movie
      // router.push({ name: 'home' })
    },
    SET_SEARCH_RESULT: function (state, result) {
      console.log(result)
      state.directorSearchResult = result.director
      state.actorSearchResult = result.actor
      state.movieSearchResult = result.movie
      state.perfectDirectorResult = result.perfect.director
      state.perfectActorResult = result.perfect.actor
      state.perfectMovieResult = result.perfect.movie
    },
    SET_KEYWORD: (state, keyword) => state.keyword = keyword,
    SET_IS_ENTER: (state, isEnter) => state.isEnter = isEnter,
    SET_CHOICED_GENRES: (state, genre) => state.genre = genre,
    SET_HOT_MOVIE: (state, hot) => state.hotMovies = hot,
    SET_ACTORPROFILE_VIEW: (state, actorprofile) => state.actorprofile = actorprofile,
    SET_DIRECTORPROFILE_VIEW: (state, directorprofile) => state.directorprofile = directorprofile,
    SET_MOVIEDETAIL_VIEW: (state, moviedetail) => state.moviedetail = moviedetail,
  },

  actions: {
    setHotMovie({commit}, hot) {commit('SET_HOT_MOVIE'), hot},
    
    fetchHomeView({ getters, commit }) {
      if (getters.isLoggedIn){
        axios({
          url: drf.movies.home(),
          method: 'get',
          headers: getters.authHeader
        })
          .then(res => {
            // console.log(res.data)
            commit('SET_HOME_VIEW', res.data)
            console.log('홈데이터로드')
          })
          .catch(err => {
            console.error(err.response.data)
          })
      } else {
        axios({
          url: drf.movies.home(),
          method: 'get',
        })
          .then(res => {
            // console.log(res.data)
            commit('SET_HOME_VIEW', res.data)
          })
          .catch(err => {
            console.error(err.response.data)
          })        
      }
    },

    setSearchResult({commit}, resKey) {
      commit('SET_SEARCH_RESULT', resKey.res)
      commit('SET_KEYWORD', resKey.key)
      commit('SET_IS_ENTER', resKey.isEnter)  
    },

    fetchSearchResult({commit, getters}, key) {
      // 로그인해서 요청 보낼 때
      if (getters.isLoggedIn){
        axios({
          url: drf.searche.search(),
          method: 'post',
          data: {keyword: key},
          headers: getters.authHeader
        })
          .then(res => {
            commit('SET_SEARCH_RESULT', res.data)
            commit('SET_KEYWORD', key)
          })
          .catch(err => {
            console.error(err.response.data)
          })
          // .finally(() => { 
          //   router.push({ name: 'searchResult', params: { keyword: key } }) 
            // console.log(`key= ${key}`)
          // })
      } else {
        // 비로그인 에서 요청 보낼 떄
        axios({
          url: drf.searche.search(),
          method: 'post',
          data: {keyword: key},
        })
          .then(res => {
            commit('SET_SEARCH_RESULT', res.data)
            commit('SET_KEYWORD', key)
          })
          .catch(err => {
            console.error(err.response.data)
          })
          // .finally(() => { 
          //   router.push({ name: 'searchResult', params: { keyword: key } }) 
          //   // console.log(`key= ${key}`)
          // })
      }
    },

    fetchActorProfileView({ getters, commit }, id) {
      if (getters.isLoggedIn){
        // 로그인시 토큰 같이
        axios({
          url: drf.movies.actor() + String(id),
          // url: drf.movies.actor(),
          method: 'get',
          headers: getters.authHeader
        })
          .then(res => {
            commit('SET_ACTORPROFILE_VIEW', res.data)
          })
          .catch(err => {
            console.error(err.response.data)
          })
          // .finally(()=>{ router.push({name: 'actorProfile', params: {localId: id}}) })
      } else {
        // 비로그인시 토큰x
        axios({
          url: drf.movies.actor() + String(id),
          method: 'get',
        })
        .then(res => {
          commit('SET_ACTORPROFILE_VIEW', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
        // .finally(()=>{ router.push({name: 'actorProfile', params: {localId: id}}) })
      }
    },

    fetchDirectorProfileView({ getters, commit }, id) {
      if (getters.isLoggedIn){
        // 로그인시 토큰 같이
        axios({
          url: drf.movies.director() + String(id),
          method: 'get',
          headers: getters.authHeader
        })
          .then(res => {
            commit('SET_DIRECTORPROFILE_VIEW', res.data)
          })
          .catch(err => {
            console.error(err.response.data)
          })
          // .then(()=>{router.push({ name: 'directorProfile', params: {localId: id} })})
      } else {
        // 비로그인시 토큰x
        axios({
          url: drf.movies.director() + String(id),
          method: 'get',
        })
        .then(res => {
          commit('SET_DIRECTORPROFILE_VIEW', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
        // .then(()=>{router.push({ name: 'directorProfile', params: {localId: id} })})
      }
    },

    fetchMovieDetail({ getters, commit }, id) {
      if (getters.isLoggedIn){
        // 로그인시 토큰 같이
        axios({
          url: drf.movies.detail() + String(id),
          method: 'get',
          headers: getters.authHeader
        })
          .then(res => {
            commit('SET_MOVIEDETAIL_VIEW', res.data)
            // console.log(`set_id_login: ${id}`)
          })
          .catch(err => {
            console.error(err.response.data)
          })
          // .finally(() => {
          //   router.push({ name: 'movieDetail', params: {localId: id} })
          //   // console.log(`id_login: ${id}`)
          // })
      } else {
        // 비로그인시 토큰x
        axios({
          url: drf.movies.detail() + String(id),
          method: 'get',
        })
        .then(res => {
          commit('SET_MOVIEDETAIL_VIEW', res.data)
          // console.log(`set_id_non: ${id}`)
        })
        .catch(err => {
          console.error(err.response.data)
        })
        // .finally(() => {
        //   router.push({ name: 'movieDetail', params: {localId: id} })
        //   // console.log(`id_non: ${id}`)
        // })
      }
    },
    // setChoicedGenres({commit}, )
  },
}
