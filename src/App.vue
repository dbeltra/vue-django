<template>
	<div id="app">
    <div class="container">
      <div class="columns">
        <div class="column is-one-quarter">
          <h1 class="title is-1">My store</h1>
        </div>
        <div class="colummn">
        </div>
      </div>
      <div class="columns">
        <div class="column is-one-quarter">
          <Navbar />
        </div>
        <div class="colummn">
          <ArticleList />
        </div>
      </div>
    </div>
	</div>
</template>

<script>
import ArticleList from './components/ArticleList.vue'
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
	components: {
    ArticleList,
    Navbar,
	}
}
</script>

<style>
body{
  font-family: 'Jost', sans-serif;
}
</style>
