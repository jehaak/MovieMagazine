<template>
  <div>
    <input type="checkbox" :id="genre" :name="genre"
     checked>
    <label :for="genre">{{ genre }}</label>    
  </div>
</template>

<script>
export default {
  name: 'GenreChoice',
  props: {
    genre: String, 
  },
}
</script>

<style>

</style>