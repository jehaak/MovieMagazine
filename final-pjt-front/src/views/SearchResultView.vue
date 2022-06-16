<template>
<div>
    <!-- Header -->
  <header class="w3-border w3-container w3-center w3-padding-48 w3-white">
    <h1 class="w3-xxxlarge"><b>Search Result</b></h1>
    <h6>Find your <span class="w3-tag">movies</span></h6>
  </header>
  <br>
  <div v-if="load">
    <div>
      <h1 v-if="isPerfectDirectorResult">We Find Matched Director</h1>
      <perfect-director-result
        v-for="director in perfectDirectors" 
        :key="director.id" 
        :director="director"      
      ></perfect-director-result>

      <h1 v-if="isPerfectActorResult">We Find Matched Actor!</h1>
      <perfect-actor-result
        v-for="actor in perfectActors" 
        :key="actor.id" 
        :actor="actor"      
      ></perfect-actor-result>

      <h1 v-if="isPerfectMovieResult">We Find Matched Movie!</h1>
      <perfect-movie-result
        v-for="movie in perfectMovies"
        :key="movie.id"
        :movie="movie"
      ></perfect-movie-result>
    </div>

    <!-- 디폴트 출력 검색결과 -->
    <div>
      <h1 v-if="isResult">Did you find ...</h1>
    <div class="w3-row w3-padding w3-border">
    <div class="w3-container w3-white w3-margin w3-padding-large">
      <!-- 감독 결과 -->
      <h3>about director</h3>
      <hr>
      <vue-horizontal>
        <director-card 
          v-for="director in directorSearchResult" 
          :key="director.id" 
          :director="director"
        ></director-card>
      </vue-horizontal>
        <br>
        <button v-if="isDirectorResult" @click="toDirectorSearchResult">More Directors</button>
      <br>
      <hr>
      <br>
      <h3>about actor</h3>
      <hr>
      <!-- 배우 결과 -->
      <vue-horizontal>
        <actor-card 
          v-for="actor in actorSearchResult" 
          :key="actor.id" 
          :actor="actor"
        ></actor-card>
      </vue-horizontal>
        <br>
        <button v-if="isActorReselt" @click="toActorSearchResult">More Actors</button>
      <!-- 영화 결과 -->
      <br>
      <hr>
      <br>
      <h3>about movie</h3>
      <hr>
      <vue-horizontal>
        <search-movie-card 
          v-for="movie in movieSearchResult" 
          :key="movie.local_id" 
          :movie="movie"
        ></search-movie-card>
      </vue-horizontal>
      <br v-if="!isLoggedIn">
        <button v-if="isMovieResult" @click="toMovieSearchResult">More Movies</button>
    </div>
  </div>
  </div>
  </div>
</div>
</template>

<script>
import SearchMovieCard from '@/cards/SearchMovieCard'
import ActorCard from '@/cards/ActorCard'
import DirectorCard from '@/cards/DirectorCard'
import PerfectDirectorResult from '@/components/PerfectDirectorResult.vue'
import PerfectActorResult from '@/components/PerfectActorResult.vue'
import PerfectMovieResult from '@/components/PerfectMovieResult.vue'
// import MovieDetailView from '@/views/MovieDetailView.vue'
// import MovieDetailInter from '@/intermission/MovieDetailIntermission.vue'

import drf from '@/api/drf'
import axios from 'axios'
import { mapGetters, mapActions } from 'vuex'
import router from '@/router'
import VueHorizontal from 'vue-horizontal'

export default {
  name: 'SearchResult',
  components: {
    SearchMovieCard, ActorCard, DirectorCard, 
    PerfectDirectorResult, 
    PerfectActorResult,
    PerfectMovieResult,
    VueHorizontal,
  },
  data() {
    return {
      load: false,
      keyword: this.$route.params.keyword,
      // 검색결과 유무 - 버튼 나타낼 때 사용
      isPerfectDirectorResult: false,
      isPerfectActorResult: false,
      isPerfectMovieResult: false,
      isDirectorResult: false,
      isActorReselt: false,
      isMovieResult: false,
      isResult: false,
      // 완전 일치 검색 결과 저장
      perfectDirectors: [],
      perfectActors: [],
      perfectMovies: [],
      
      // directorSearchResult: [],
      // actorSearchResult: [],
      // movieSearchResult: [],
// fiveDirectors: [],
      // fiveActors: [],
      // fvieMovies: [],
    }
  },
  computed: {
    ...mapGetters([
      'directorSearchResult',
      'actorSearchResult',
      'movieSearchResult',
      // 'perfectDirectorResult',
      // 'perfectActorResult',
      // 'perfectMovieResult',
      'isLoggedIn',
      'authHeader',
    ]),
  },
  methods: {
    ...mapActions(['setSearchResult']),
    toDirectorSearchResult() {router.push({ name: 'directorSearchResult', params: {keyword: this.keyword} })},
    toActorSearchResult() {router.push({ name: 'actorSearchResult', params: {keyword: this.keyword} })},
    toMovieSearchResult() {router.push({ name: 'movieSearchResult', params: {keyword: this.keyword} })},
    // 검색결과 유무 업뎃
    // isPerfectSearch() {
    //   if (this.perfectDirectorResult.length) {this.isPerfectDirectorResult = true}
    //   if (this.perfectActorResult.length) {this.isPerfectActorResult = true}
    //   if (this.perfectMovieResult.length) {this.isPerfectMovieResult = true}
    //   if (this.directorSearchResult.length) {this.isDirectorResult = true}
    //   if (this.actorSearchResult.length) {this.isActorReselt = true}
    //   if (this.movieSearchResult.length) {this.isMovieResult = true}
    //   this.isResult = this.isDirectorResult || this.isActorReselt || this.isMovieResult
    // },
    // setSearchResult() {
    //   // console.log('서치 창 세트 시작')
    //   this.perfectDirectorResult.forEach((director) => {
    //     // console.log('디렉터')
    //     // console.log(director)
    //     this.perfectDirectors = [...this.perfectDirectors, director]
    //   }) 
    //   this.perfectActorResult.forEach((actor) => {
    //     this.perfectActors = [...this.perfectActors, actor]
    //     // console.log('액터')
    //     // console.log(actor)
    //   })
    //   this.perfectMovieResult.forEach((movie) => {
    //     this.perfectMovies = [...this.perfectMovies, ...movie.movie_info]
    //     // this.perfectMovies.push(movie.movie_info)
    //     })
    //   // console.log('퍼팩트무비스')
    //   // console.log(this.perfectActors)
    //   // this.fiveDirectors = this.directorSearchResult.filter(function (dir, idx) {return idx<5});
    //   // this.fiveActors = this.actorSearchResult.filter(function (actor, idx) {return idx<5});
    //   // this.fiveMovies = this.movieSearchResult.filter(function (movie, idx) {return idx<5});
    // }
  },
  created() {
        if (this.isLoggedIn){
        axios({
          url: drf.searche.search() + this.keyword,
          method: 'post',
          data: {
            keyword: this.keyword,
          },
          headers: this.authHeader
        })
          .then(res => {
            // state에 데이터 저장
            this.setSearchResult({
              res: res.data, 
              key: this.keyword,
            })
            this.load = false
            // 
            res.data.perfect.director.forEach((director) => {
              this.perfectDirectors = [...this.perfectDirectors, director]
            }) 
            res.data.perfect.actor.forEach((actor) => {
              this.perfectActors = [...this.perfectActors, actor]
            })
            res.data.perfect.movie.forEach((movie) => {
              this.perfectMovies = [...this.perfectMovies, ...movie.movie_info]
              // this.perfectMovies.push(movie.movie_info)
              })
              console.log('per')
              console.log(res.data.perfect.movie)
            // this.directorSearchResult = res.data.director
            // this.actorSearchResult = res.data.actor
            // this.movieSearchResult = res.data.movie
      
            if (res.data.perfect.director.length) {this.isPerfectDirectorResult = true}
            if (res.data.perfect.actor.length) {this.isPerfectActorResult = true}
            if (res.data.perfect.movie.length) {this.isPerfectMovieResult = true}
            if (res.data.director.length) {this.isDirectorResult = true}
            if (res.data.actor.length) {this.isActorReselt = true}
            if (res.data.movie.length) {this.isMovieResult = true}
            this.isResult = this.isDirectorResult || this.isActorReselt || this.isMovieResult
            this.load = true
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
          url: drf.searche.search() + this.keyword,
          method: 'post',
          data: {
            keyword: this.keyword,
          },
        })
          .then(res => {
            this.setSearchResult({
              res: res.data, 
              key: this.keyword,
            })
            console.log(res.data)
            res.data.perfect.director.forEach((director) => {
              this.perfectDirectors = [...this.perfectDirectors, director]
            }) 
            res.data.perfect.actor.forEach((actor) => {
              this.perfectActors = [...this.perfectActors, actor]
              // console.log('액터')
              // console.log(actor)
            })
            res.data.perfect.movie.forEach((movie) => {
              this.perfectMovies = [...this.perfectMovies, ...movie.movie_info]
              // this.perfectMovies.push(movie.movie_info)
              })
            // this.directorSearchResult = res.data.director
            // this.actorSearchResult = res.data.actor
            // this.movieSearchResult = res.data.movie
      
            if (res.data.perfect.director.length) {this.isPerfectDirectorResult = true}
            if (res.data.perfect.actor.length) {this.isPerfectActorResult = true}
            if (res.data.perfect.movie.length) {this.isPerfectMovieResult = true}
            if (res.data.director.length) {this.isDirectorResult = true}
            if (res.data.actor.length) {this.isActorReselt = true}
            if (res.data.movie.length) {this.isMovieResult = true}
            this.isResult = this.isDirectorResult || this.isActorReselt || this.isMovieResult
          
            this.load = true
          })
          .catch(err => {
            console.error(err.response.data)
          })
          // .finally(() => { 
          //   router.push({ name: 'searchResult', params: { keyword: key } }) 
            // console.log(`key= ${key}`)
          // })
      }
    // this.fetchSearchResult(this.keyword)
    // this.isPerfectSearch()
    // this.setSearchResult()
  },
}
</script>

<style>

</style>

