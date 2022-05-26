<template>
  <div>
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
  </div>
</template>

<script>
  // import ActorCard from '@/components/ActorCard'
  // import DirectorCard from '@/components/DirectorCard'
  import HomeMovieCard from '@/components/HomeMovieCard'
  import { mapActions, } from 'vuex'

  // import { mapActions, mapGetters } from 'vuex'
  // import VueHorizontal from 'vue-horizontal'
  import drf from '@/api/drf'

export default {
  name: 'PerfectMovieResult',
  components: {
    // ActorCard, DirectorCard, VueHorizontal,
    HomeMovieCard
  },
  props: {
    movie: Object,
  },
  data () {
    return {
      // movie_info: [],
      // director: [],
      // actors: [],
    }
  },
  computed: {
    // ...mapGetters([
    //   'moviedetail',
    //   ]),
    imgURL() {
    // console.log(this.movie_info[0]['poster_url'])
    return drf.url.img() + this.movie.poster_url
    },
  },
  methods: {
    ...mapActions([
      'fetchMovieLike',
      'fetchMovieWatched',
    ]),
    myFunction(id) {
      var x = document.getElementById(id);
      if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
      } else { 
        x.className = x.className.replace(" w3-show", "");
      }
      //   event.target.className += " w3-show";
      // } else { 
      //   event.target.className = event.target.className.replace(" w3-show", "");
      // }
    },
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
    console.log(this.movie)
  },
}
</script>

<style>

</style>