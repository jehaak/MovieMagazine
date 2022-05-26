<template>
  <div class="w3-container justify-content-center">
    <div class="w3-white" style="width: 18rem margin:0 auto;">
      <router-link :to="{ name: 'movieDetail', params: {localId: movie.id} }">
          <img class="user-movie-card w3-grayscale" :src="imgURL" alt="Card image cap" style="width:100%; height:325.65px; objec-fit:cover;">
          <div class="w3-container w3-black">
            <h4 style="font-size:15px; text-align: center;">{{ movie.title }}</h4>
            <!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p> -->
            <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
          </div>
      </router-link>
  </div>
          <p v-if="movie.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="position:relative; right: 3px; width: 113px; margin: 2px;" @click="[likeClick($event), likeAxios(movie.local_id)]">✓ Liked</button></p>
          <p v-if="movie.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="position:relative; right: 3px; width: 113px; margin: 2px;" @click="[likeClick($event), likeAxios(movie.local_id)]"><i class="fa fa-thumbs-up"></i> Like</button></p>
          <p v-if="movie.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="position:relative; left: 113px; bottom: 60px; width: 113px; margin: 2px" @click="[watchedClick($event), watchedAxios(movie.local_id)]">✓ Watched</button></p>
          <p v-if="movie.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="position:relative; left: 113px; bottom: 60px; width: 113px; margin: 2px" @click="[watchedClick($event), watchedAxios(movie.local_id)]"><i class="fa fa-video-camera"></i> Watch</button></p>   </div>
</template>

<script>
import { mapActions } from 'vuex'
import drf from '@/api/drf'

export default {
  name: 'MovieCard',
  props: {
    movie: Object,
    like: String,
    watched: String,
  },
  components: {  },
  data() {
    return {
      like_state: '',
      watched_state: '',
    }
  },
  computed: {
    imgURL() {
      return drf.url.img() + this.movie.poster_url
    }
  },
  methods: {
    ...mapActions([
      'fetchSearchResult',
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
  created() {},
}
</script>
<style>

</style>