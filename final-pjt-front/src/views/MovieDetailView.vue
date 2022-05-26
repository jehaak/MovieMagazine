<template>
  <div>
    <!-- Header -->
  <header class="w3-border w3-container w3-center w3-padding-48 w3-white">
    <h1 class="w3-xxxlarge"><b>Movie Detail</b></h1>
    <h6>Check the movie <span class="w3-tag">{{movie.title}}</span></h6>
  </header>

    <div class="w3-row w3-padding w3-border">
    <div class="w3-container w3-white w3-margin w3-padding-large">
      <div class="w3-center">
        <h3><b>{{movie.title}}</b></h3>
        <h5>{{movie.genre}}<span class="w3-opacity"></span></h5>
      </div>

      <div class="w3-justify w3-container">
        <div class="w3-center">
        <home-movie-card 
        :movie="movie" :like="movie.like" :watched="movie.watched"
        ></home-movie-card>
        </div>
        <br>
        <p><strong>popularity: {{movie.popularity}}</strong></p>
        <p>{{movie.overview}}</p>
        <!-- 좋아요, 봤어요 -->
        <p v-if="movie.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[likeClick($event), likeAxios(movie.local_id)]">✓ Liked</button></p>
        <p v-if="movie.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[likeClick($event), likeAxios(movie.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
        <p v-if="movie.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[watchedClick($event), watchedAxios(movie.local_id)]">✓ Watched</button></p>
        <p v-if="movie.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="width: 120px; margin: 2px;" @click="[watchedClick($event), watchedAxios(movie.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>
        </div>
      </div>
      </div>
  <h1><b>{{director.name}}</b> directec this movie</h1>
  <div class="w3-row w3-padding w3-border">
    <director-card :director="director"></director-card>
    <hr>
      </div>
    <h1>Featured Actors</h1>

  <div class="w3-row w3-padding w3-border">
    <vue-horizontal scroll>
      <actor-card
        v-for="actor in actors" 
        :key="actor.id"
        :actor="actor"
      ></actor-card>
    </vue-horizontal>
  </div>

</div>
</template>

<script>
  // import MovieCard from '@/components/MovieCard'
  import ActorCard from '@/components/ActorCard'
  import HomeMovieCard from '@/components/HomeMovieCard'
  import DirectorCard from '@/components/DirectorCard'
  import { mapActions, mapGetters, } from 'vuex'
  import VueHorizontal from 'vue-horizontal'
  import axios from 'axios'
  import drf from '@/api/drf'


  export default {
  name: 'UserProfileView',
  components: {
    ActorCard, VueHorizontal, HomeMovieCard, DirectorCard
  },
  data () {
    return {
      load: false,
      like_state: '',
      watched_state: '',
      movie: [],
      director: [],
      actors: [],
      acror_len: 0,
    }
  },
  computed: {
    ...mapGetters([
      'authHeader',
      'isLoggedIn'
      ]),
      imgURL() {
      const img = drf.url.img() + this.movie.poster_url
      if ( this.movie.poster_url ){ return img }
      else { return drf.url.noPhoto() }        
      // return drf.url.img() + this.movie.poster_url
      },
  },
  methods: {
    ...mapActions([
      'fetchMovieLike',
      'fetchMovieWatched',
      ]),
    likeClick(event) {
    console.log(event.target.innerHTML)
    if (event.target.innerHTML === '<i class="fa fa-thumbs-up"></i> Like') {
      event.target.innerHTML = '✓ Liked'
    }
    else {
      event.target.innerHTML = '<i class="fa fa-thumbs-up"></i> Like'
    }
    },
    likeAxios(id) {
    this.fetchMovieLike(id)
    },

    watchedClick(event) {
    if (event.target.innerHTML === '<i class="fa fa-video-camera"></i> Watch') {
      event.target.innerHTML = '✓ Watched'
    }
    else {
      event.target.innerHTML = '<i class="fa fa-video-camera"></i> Watch'
    }
    },
    watchedAxios(id) {
    this.fetchMovieWatched(id)
    },
    },
  created() {
    if (this.isLoggedIn){
        // 로그인시 토큰 같이
        axios({
          url: drf.movies.detail() + this.$route.params.localId,
          method: 'get',
          headers: this.authHeader
        })
          .then(res => {
            this.movie = res.data.movie_info[0]
            this.director = res.data.director[0]
            this.actors = res.data.actor
            this.load = true
            this.acror_len = res.data.actor.length
            console.log(this.acror_len)
          })
          .catch(err => {
            console.error(err.response.data)
          })
      } else {
        // 비로그인시 토큰x
        axios({
          url: drf.movies.detail() + this.$route.params.localId,
          method: 'get',
        })
        .then(res => {
            // console.log('디렉터')
            // console.log(res.data)
          this.movie = res.data.movie_info[0]
          this.director = res.data.director[0]
          this.actors = res.data.actor
          this.load = true
        })
        .catch(err => {
          console.error(err.response.data)
        })
      }
  },
}
</script>

<style></style>