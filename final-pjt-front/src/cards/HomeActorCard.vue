<template>
  <div>
    <router-link :to="{ name: 'actorProfile', params: {localId: actor.id} }">
      <div class="card" style="width: 10rem;">
        <img class="card-img-top card-img" :src="imgURL" alt="Card image cap">
      </div>
    </router-link>
  </div>
</template>

<script>
import drf from '@/api/drf'

export default {
  name: 'HomeActorCard',
  props: {
    actor: Object,
  },
  computed: {
    IMG() {return "@/assets/images/noimage.png"},
    imgURL() {
      const img = drf.url.img() + this.actor.profile_url
      if ( this.actor.profile_url ){ return img}
      else { return drf.url.noPhoto() }
    }
  },
  methods: {
  },
  created() {
    console.log(this.actor)
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