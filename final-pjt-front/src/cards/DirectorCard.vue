<template>

    <!-- <div class="w3-white w3-margin" style="width: 18rem;">
    <router-link :to="{ name: 'directorProfile', params: {localId: director.id} }">
        <img
          class="card-img" 
          :src="imgURL" 
          :alt="director.name" 
          style="width:100%">
        <div class="w3-container w3-black">
          <h4>{{ director.name }}</h4>
        </div>
      </router-link>
    </div> -->




  <div>
    <router-link :to="{ name: 'directorProfile', params: {localId: director.id} }">
      <div class="card" style="width: 18rem;">
        <img class="card-img-top card-img w3-grayscale" :src="imgURL" alt="Card image cap">
        <div class="card-body">
          <h5 class="card-title">{{ director.name }}</h5>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
import drf from '@/api/drf'

export default {
  name: 'DirectorCard',
  props: {
    director: Object,
  },
  // data() {
  //   return {
  //     imageURL: '',
  //   }
  // },
  computed: {
    // ...mapGetters([]),
    imgURL() {
      const img = drf.url.img() + this.director.profile_url
      if ( this.director.profile_url ){ return img}
      else { return drf.url.noPhoto() }
    }
  },
  methods: {
    // ...mapActions(['fetchSearchResult']),
    // setSearchResult() {
    // },
  },
  created() {
    // this.setSearchResult()
  },
}
</script>

<style>
.card-img {
  width: 270px;
  height: 405px;
  object-fit: cover;
}
</style>