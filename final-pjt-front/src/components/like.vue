<template>
  <div>
    <button @click="likeClick(movieId)">{{like_state}}</button>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
  name: 'LikeMovie',
  components: {
  },
  props: {
    movieId: Number,
    like: String,
  },
  data () {
    return {
      like_state: '',
    }
  },
  methods: {
    ...mapActions([
      'fetchMovieLike',
      ]),
    likeClick(){
      if (this.like_state === '좋아요') {
      this.like_state = '좋아요 취소'
      }
      else {
      this.like_state = '좋아요'
      }
      console.log('라이크 보내기 전')
      this.fetchMovieLike(this.movieId)
      console.log('라이크 보낸 후')
    },
  },
   created() {
     console.log(this.like)
    if (this.like === 'true') {
      this.like_state = '좋아요 취소'
    }
    else {
      this.like_state = '좋아요'
    }
  },
}
</script>

<style>

</style>