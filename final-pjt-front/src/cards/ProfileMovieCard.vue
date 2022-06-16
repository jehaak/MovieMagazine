<template>
<div>
  <div class="w3-center" style="height:310px;">
    <div class="w3-white w3-margin" style="width: 10rem;">
      <router-link :to="{ name: 'movieDetail', params: {localId: movie.id} }">
          <img :src="imgURL" alt="Card image cap" style="width: 150px; height: 225px;" class="w3-grayscale">
          <div id="profile-movie-card-in" class="w3-container w3-black" :style="blackBoxHeight">
            <span style="font-size: 5px;">{{ movie.title }}</span>
            <!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p> -->
            <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
          </div>
      </router-link>
    </div>
    <p v-if="movie.like==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="position:relative; bottom:38.5px; left:14px; width: 74.5px; height:20px; margin:2px; padding:1px; font-size: 5px;  " @click="[likeClick($event), likeAxios(movie.local_id)]">✓ Liked</button></p>
    <p v-if="movie.like==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="position:relative; bottom:38.5px; left:14px; width: 74.5px; height:20px; margin:2px; padding:1px; font-size: 5px;  " @click="[likeClick($event), likeAxios(movie.local_id)]"><i class="fa fa-thumbs-up" style="font-size: 5px;"></i> Like</button></p>
    <p v-if="movie.watched==='true'" class="w3-left"><button class="w3-button w3-white w3-border" style="position:relative; bottom:38.5px; left:11px; width: 74.5px; height:20px; margin:2px; padding:1px; font-size: 5px;  " @click="[watchedClick($event), watchedAxios(movie.local_id)]">✓ Watched</button></p>
    <p v-if="movie.watched==='false'" class="w3-left"><button class="w3-button w3-white w3-border" style="position:relative; bottom:38.5px; left:11px; width: 74.5px; height:20px; margin:2px; padding:1px; font-size: 5px;  " @click="[watchedClick($event), watchedAxios(movie.local_id)]"><i class="fa fa-video-camera" style="font-size: 5px;"></i> Watch</button></p>
  </div>


</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import drf from '@/api/drf'

export default {
  name: 'MovieCard',
  props: {
    movie: Object,
    // like: String,
    // watched: String,
  },
  components: {  },
  data() {
    return {
      like_state: '',
      watched_state: '',
    }
  },
  computed: {
    ...mapGetters([ 'isLoggedIn', ]),
    imgURL() {
      return drf.url.img() + this.movie.poster_url
    },
    blackBoxHeight() {
      if (this.isLoggedIn) {return "height: 45px;"}
      else {return ""}
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
    if (event.target.innerHTML === '<i class="fa fa-thumbs-up" style="font-size: 5px;"></i> Like') {
      event.target.innerHTML = '✓ Liked'
    }
    else {
      event.target.innerHTML = '<i class="fa fa-thumbs-up" style="font-size: 5px;"></i> Like'
    }
    },
    likeAxios(id) {
    this.fetchMovieLike(id)
    },

    watchedClick(event) {
    if (event.target.innerHTML === '<i class="fa fa-video-camera" style="font-size: 5px;"></i> Watch') {
      event.target.innerHTML = '✓ Watched'
    }
    else {
      event.target.innerHTML = '<i class="fa fa-video-camera" style="font-size: 5px;"></i> Watch'
    }
    },
    watchedAxios(id) {
    this.fetchMovieWatched(id)
    },
  },
  // created() {
  //   console.log("프로필 무비카드 만듦")
  //   console.log(this.isLoggedIn)
  // //   if (this.movie.like === 'true') {
  // //     this.like_state = '좋아요 취소'
  // //   }
  // //   else {
  // //     this.like_state = '좋아요'
  // //   }
  // //   if (this.movie.watched === 'true') {
  // //     this.watched_state = '봤어요 취소'
  // //   }
  // //   else {
  // //     this.watched_state = '봤어요'
  // //   }
  // },
}
</script>