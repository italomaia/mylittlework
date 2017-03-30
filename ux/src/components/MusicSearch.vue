<template>
<div class="container">
  <form @submit.prevent="$emit('search-music', searchTerm)"
    id="search-form" class="form-horizontal">
    <div class="form-group form-group-lg">
      <div class="col-xs-12 col-sm-8 col-sm-offset-2">
        <input v-model="searchTerm"
          class="form-control"
          type="text" id="formGroupInputLarge"
          :placeholder="'Search for Spotify ' + searchType + 's'">
        <a class="search-icon" href=""><i class="fa fa-search" aria-hidden="true"></i></a>
        <p class="error" v-if="searchTerm.length == 0">Please fill out the form.</p>
      </div>
    </div>
  </form>
</div>
</template>

<script>
export default {
  props: ['searchType'],
  data: () => ({
    searchTerm: ''
  })
}
</script>
