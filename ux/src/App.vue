<template>
  <div id="app">
    <page-nav
      v-on:update-search-type="updateSearchType"
      :search-type="searchType"
      :total="total"></page-nav>
    <music-search
      :search-type="searchType"
      v-on:search-music="searchMusic"></music-search>
    <music-result :results="results"></music-result>
  </div>
</template>

<script>
import MusicSearch from './components/MusicSearch'
import MusicResult from './components/MusicResult'
import PageNav from './components/PageNav'

import $ from 'jquery'

const spotifyAPI = {
  search: 'https://api.spotify.com/v1/search?'
}

function pickThumb (images) {
  for (let img of images) {
    if (img.height >= 60 && img.height <= 70 && img.height === img.width) {
      return img.url
    }
  }

  return 'https://placehold.it/64x64'
}

function extractThumb (item) {
  let images = []

  if (item.images) {
    images = item.images
  } else if (item.album && item.album.images) {
    images = item.album.images
  }

  return pickThumb(images)
}

export default {
  name: 'app',
  data: () => ({
    searchType: 'track',
    total: 0,
    results: []
  }),
  components: {
    PageNav,
    MusicSearch,
    MusicResult
  },
  methods: {
    makeSearchCall: function (searchTerm) {
      const queryStr = $.param({
        q: searchTerm,
        type: this.searchType
      })
      return $.get(spotifyAPI.search + queryStr)
    },
    updateSearchType: function (searchType) {
      this.searchType = searchType
    },
    searchMusic: function (searchTerm) {
      const self = this

      this.makeSearchCall(searchTerm)
        .done(function (data) {
          self.total = 0

          for (let resultType of Object.keys(data)) {
            let result = data[resultType]
            let items = result.items
            self.total = self.total + result.total
            self.results = []

            for (let item of items) {
              self.results.push({
                url: item.external_urls && item.external_urls.spotify,
                name: item.name,
                thumb: extractThumb(item)
              })
            }
          }
        })
        .fail(function (jqXHR, textStatus) {
          console.log('fail')
          console.log(textStatus)
        })
    }
  }
}
</script>
