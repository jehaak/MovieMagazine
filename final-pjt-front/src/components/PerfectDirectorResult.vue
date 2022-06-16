<template>
  <div>
    <div class="w3-row w3-padding w3-border">
    <div class="w3-container w3-white w3-margin w3-padding-large">
    <div class="w3-col l3 m6 w3-margin-bottom ">
    <div class="w3-row w3-border w3-margin-top">
      <router-link :to="{ name: 'directorProfile', params: {localId: directorInfo.id} }">
      <img :src="imgURL" :alt="directorInfo.name" style="width:100%">
      </router-link>
      <h3 style="padding-left: 5px;">{{ directorInfo.name }}</h3>
      <p class="w3-opacity" style="padding-left: 5px;">My level: {{ directorLevel }}</p>
    </div>
    </div>
    <div class="w3-container w3-col l8 m9 w3-margin-bottom w3-light-grey" style="background-color: lightgrey; height: 460px; padding: 50px; margin-top: 15px; margin-left:55px;">
      <p style="font-family: 'Brush Script MT'; font-size: 20px;">However, once you start to appreciate {{ directorInfo.name }} effort to understand lines and lay out the feelings inside, you would definately be more into {{ directorInfo.name }}. Find more about the actor, by scrolling through the filmography of {{ directorInfo.name }} for the film just apt for your vibe. It is always fun to explore foreign fields to find the life friend of yours. This actor's might be it!</p>
    </div>
    <!-- 출연작 -->
    <div>
      <h3>Directed Movie</h3>
      <div class="container">
      <vue-horizontal>
        <profile-movie-card
          v-for="movie in directedMovie" 
          :key="movie.id" 
          :movie="movie"
        ></profile-movie-card>
      </vue-horizontal>
      </div>
    </div>
  </div>
  </div>
  </div>
</template>

<script>
  import ProfileMovieCard from '@/cards/ProfileMovieCard.vue'
  import VueHorizontal from 'vue-horizontal'
  import drf from '@/api/drf'

  import { mapGetters } from 'vuex'

  export default {
  name: 'PerfectActor',
  props: { director: Object},
  components: {
    ProfileMovieCard, VueHorizontal,
  },
  data () {
    return {
      directorId: this.$route.params.localId,
      directorLevel: null,
      // recomendMovie: [],
      directorInfo: [],
      directedMovie: [],
    }
  },
  computed: {
    ...mapGetters([
      // 'actorprofile',
      'isLoggedIn',
      ]),
    imgURL() {
      // console.log('액터디테일')
      // console.log(this.actorprofile)
      return drf.url.img() + this.directorInfo.profile_url
    }
  },
  methods: {
    // ...mapActions([
    //   'fetchActorProfileView',
    //   ]),
      setDirectorProfileData() {
      if (this.isLoggedIn) {
        // 로그인시에만 레벨정보, 추천영화 정보 보여줌
        this.directorLevel = this.director.director_level
        // if (this.actor.recomend_movie !== "no_movie") {
        //   this.recomendMovie = this.actorprofile.recomend_movie
        // }
      }
      this.directorInfo = this.director.director_info
      this.directedMovie = this.director.directed_movies
    },
    },
  created() {
    // this.fetchActorProfileView(this.$route.params.localId)
    this.setDirectorProfileData()
  },
}
</script>

<style></style>