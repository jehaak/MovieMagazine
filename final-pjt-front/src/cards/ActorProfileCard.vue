<template>
<div class="w3-col l3 m6 w3-margin-bottom">
  <router-link :to="{ name: 'actorProfile', params: {localId: actor.id} }">
    <img :src="actorProfileUrl" alt="John" style="width:212.49px;height:318.72px;object-fit:cover;">
    <h3>{{actor.name}}</h3> <span><i class="fa fa-heart" :style="actorColor"></i>  My Actor Level: {{actor.level}}%</span>
  </router-link>
  <!-- <p class="w3-opacity">CEO & Founder</p> -->
  <!-- <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p> -->
  <p><button 
        @click="modalOpen(actor.id)"
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
  props: { actor: Object, },
  data() {
    return {
      actorProfileUrl: '',
      actorColor: '',      
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
    this.actorColor = color[parseInt(this.actor.level/20)]

    if ( this.actor === 'no_actor' ){ this.actorProfileUrl = drf.url.noPhoto() }
    else if ( !this.actor.profile_url ){ this.actorProfileUrl = drf.url.noPhoto() }
    else { this.actorProfileUrl = drf.url.img() + this.actor.profile_url }
  
  }
}
</script>

<style>

</style>