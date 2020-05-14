<template>
  <div 
    class="column article-list-item"
    :class="articleWidth"
  >
    <div class="box">
      <article class="media">
        <figure class="media-left">
            <p class="image is-64x64">
            <img :src="article.imgUrl">
            </p>
            <div>{{article.price}}</div>
        </figure>
        <div class="media-content">
            <p>
              <strong>{{article.name}}</strong>
              <br>{{article.description}}
            </p>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Article',
  props: {
    article: {
      type: Object,
      required: true
    },
    isList: {
      type: Boolean,
    }
  },
  computed: {
    articleWidth: function(){
      return this.isList ? 'is-full' : 'is-half'
    }
  }
};
</script>

<style>
.box{
  width: 100%;
}
</style>

