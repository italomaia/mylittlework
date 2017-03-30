<template>
<div class="container">
  <div class="col-xs-12 col-sm-8 col-sm-offset-2">
    <ul class="results">
      <li v-for="item in results">
        <img class="thumb" :src="item.thumb">
        <a :href="item.url"
          :title.disabled="item.url === undefined"
          title="Click to listen in Spotify"
          target="_blank">{{ item.name }}</a>
      </li>
    </ul>
  </div>
</div>
</template>

<script>
export default {
  props: ['results']
}
</script>
