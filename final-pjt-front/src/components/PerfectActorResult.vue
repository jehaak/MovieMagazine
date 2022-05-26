<template>
  <div>
    <div class="w3-row w3-padding w3-border">
    <div class="w3-container w3-white w3-margin w3-padding-large">
    <div class="w3-col l3 m6 w3-margin-bottom ">
    <div class="w3-row w3-border w3-margin-top">
      <router-link :to="{ name: 'actorProfile', params: {localId: actorInfo.id} }">
      <img :src="imgURL" :alt="actorInfo.name" style="width:100%">
      </router-link>
      <h3 style="padding-left: 5px;">{{ actorInfo.name }}</h3>
      <p class="w3-opacity" style="padding-left: 5px;">My level: {{ actorLevel }}</p>
    </div>
    </div>
    <div class="w3-container w3-col l8 m9 w3-margin-bottom w3-light-grey" style="background-color: lightgrey; height: 460px; padding: 50px; margin-top: 15px; margin-left:55px;">
      <p style="font-family: 'Brush Script MT'; font-size: 20px;">However, once you start to appreciate {{ actorInfo.name }} effort to understand lines and lay out the feelings inside, you would definately be more into {{ actorInfo.name }}. Find more about the actor, by scrolling through the filmography of {{ actorInfo.name }} for the film just apt for your vibe. It is always fun to explore foreign fields to find the life friend of yours. This actor's might be it!</p>
    </div>
    </div>
    <div>
      <h3>Casted Movie</h3>
      <vue-horizontal>
        <profile-movie-card
          v-for="movie in castedMovie" 
          :key="movie.id" 
          :movie="movie"
        ></profile-movie-card>
      </vue-horizontal>
    </div>
  </div>
  </div>
</template>

<script>
  import ProfileMovieCard from '@/components/ProfileMovieCard.vue'
  import VueHorizontal from 'vue-horizontal'
  import drf from '@/api/drf'

  import { mapGetters } from 'vuex'

  export default {
  name: 'PerfectActor',
  props: { actor: Object},
  components: {
    ProfileMovieCard, VueHorizontal,
  },
  data () {
    return {
      actorId: this.$route.params.localId,
      actorLevel: null,
      // recomendMovie: [],
      actorInfo: [],
      castedMovie: [],
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
      return drf.url.img() + this.actorInfo.profile_url
    }
  },
  methods: {
    // ...mapActions([
    //   'fetchActorProfileView',
    //   ]),
      setActorProfileData() {
      if (this.isLoggedIn) {
        // 로그인시에만 레벨정보, 추천영화 정보 보여줌
        this.actorLevel = this.actor.actor_level
        // if (this.actor.recomend_movie !== "no_movie") {
        //   this.recomendMovie = this.actorprofile.recomend_movie
        // }
      }
      this.actorInfo = this.actor.actor_info
      this.castedMovie = this.actor.casted_movies
    },
    },
  created() {
    // this.fetchActorProfileView(this.$route.params.localId)
    this.setActorProfileData()
  },
}
</script>

<style></style>