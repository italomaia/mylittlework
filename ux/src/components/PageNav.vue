<template>
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <div class="navbar-brand" href="#"><i class="fa fa-rebel" aria-hidden="true"></i></div>
      </div>
      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li class="dropdown active">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Filter <span class="caret"></span></a>
            <ul class="dropdown-menu music-types">
              <li v-for="opt in typeOptions">
                <a v-text="opt" @click="$emit('update-search-type', opt)"
                  class="capfirst"></a>
              </li>
            </ul>
          </li>
          <li>
            <a class="capfirst" href="#">{{ searchType }}</a>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li class="counter">Counter {{ total }}</li>
        </ul>
      </div><!-- /.navbar-collapse -->
    </div><!-- /.container-->
  </div><!-- /.container-fluid -->
</nav>
</template>

<script>
export default {
  props: ['searchType', 'total'],
  data: () => ({
    typeOptions: [
      'album',
      'artist',
      'playlist',
      'track'
    ]
  })
}
</script>

<style>
.music-types li a {
  cursor: pointer;
}

.capfirst:first-letter {
  text-transform:capitalize;
}
</style>
