<template>
<div class="w3-col l3 m6 w3-margin-bottom">
  <router-link :to="{ name: 'directorProfile', params: {localId: director.id} }">
    <img :src="directorProfileUrl" alt="John" style="width:212.49px;height:318.72px;object-fit:cover;">
    <h3>{{director.name}}</h3> <span><i class="fa fa-heart" :style="directorColor"></i>  My Actor Level: {{director.level}}%</span>
  </router-link>
  <!-- <p class="w3-opacity">CEO & Founder</p> -->
  <!-- <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p> -->
  <p><button 
        @click="modalOpen(director.id)"
        class="w3-button w3-light-grey w3-block"
        id="myBtn">
    Movie Recommend    
  </button></p>
</div>
</template>

<script>
import drf from '@/api/drf'

export default {
  name: 'UserProfileCard',
  props: { director: Object, },
  data() {
    return {
      directorProfileUrl: '',
      directorColor: '',      
    }
  },
  methods: {
    modalOpen(id) {
      var inst = document.getElementById(id);
      inst.style = "display: block;"
    },
  },
  created() {

    const color = ["color: #D3D3D3;", "color: #A9A9A9", "color: #787878;", "color: #484848;", "color: #000000;", "color: #000000;"]
    this.directorColor = color[parseInt(this.director.level/20)]

    if ( this.director === 'no_actor' ){ this.directorProfileUrl = drf.url.noPhoto() }
    else if ( !this.director.profile_url ){ this.directorProfileUrl = drf.url.noPhoto() }
    else { this.directorProfileUrl = drf.url.img() + this.director.profile_url }
  
  }
}
</script>

<style>

</style>