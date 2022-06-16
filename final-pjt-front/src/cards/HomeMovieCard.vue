<template>
  <div class="w3-container justify-content-center">
    <div class="w3-white" style="width: 18rem margin:0 auto;">
      <router-link :to="{ name: 'movieDetail', params: {localId: movie.id} }">
          <img :src="imgURL" alt="Card image cap" style="width:100%" class="w3-grayscale">
          <div class="w3-container w3-black">
            <h4>{{ movie.title }}</h4>
            <!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p> -->
            <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
          </div>
      </router-link>
    </div>

  </div>
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
    likeClick(){
    console.log(this.movie.like)
    if (this.like_state === '좋아요') {
      this.like_state = '좋아요 취소'
    }
    else {
      this.like_state = '좋아요'
    }
    this.fetchMovieLike(this.movie.local_id)
    },
    watchedClick(){
    console.log(this.movie.watched)
    if (this.watched_state === '봤어요') {
      this.watched_state = '봤어요 취소'
    }
    else {
      this.watched_state = '봤어요'
    }
    this.fetchMovieWatched(this.movie.local_id)
    },
  },
  created() {
    if (this.like === 'true') {
      this.like_state = '좋아요 취소'
    }
    else {
      this.like_state = '좋아요'
    }
    if (this.watched === 'true') {
      this.watched_state = '봤어요 취소'
    }
    else {
      this.watched_state = '봤어요'
    }
  },
}
</script>