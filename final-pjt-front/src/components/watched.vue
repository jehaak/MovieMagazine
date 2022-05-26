<template>
  <div>
    <button @click="watchedClick(movieId)">{{watched_state}}</button>
  </div>
</template>

<script>
  import {mapActions } from 'vuex'

  export default {
  name: 'WatchedMovie',
  components: {
  },
  props: {
    movieId: Number,
    watched: String,
  },
  data () {
    return {
      watched_state: ''
    }
  },
  methods: {
    ...mapActions([
      'fetchMovieWatched',
      ]),
    watchedClick(){
      if (this.watched_state === '봤어요') {
      this.watched_state = '봤어요 취소'
      }
      else {
      this.watched_state = '봤어요'
      }
      this.fetchMovieWatched(this.movieId)
    },
  },
   created() {
    if (this.watched === 'true') {
      this.watched_state = '봤어요 취소'
    }
    else {
      this.watched_state = '봤어요'
    }
  },
}
</script>

<style>

</style>