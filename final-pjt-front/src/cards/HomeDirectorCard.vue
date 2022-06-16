<template>
  <div>
    <router-link :to="{ name: 'directorProfile', params: {localId: director.id} }">
      <div class="card" style="width: 10rem;">
        <img class="card-img-top card-img" :src="imgURL" alt="Card image cap">
      </div>
    </router-link>
  </div>
</template>

<script>
import drf from '@/api/drf'

export default {
  name: 'HomeDirectorCard',
  props: {
    director: Object,
  },
  computed: {
    imgURL() {
      const img = drf.url.img() + this.director.profile_url
      if ( this.director.profile_url ){ return img}
      else { return drf.url.noPhoto() }
    }
  },
  methods: {
  },
  created() {
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