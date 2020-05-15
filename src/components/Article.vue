/* eslint-disable no-console */
<template>
  <div 
    class="column article-list-item"
    :class="articleWidth"
  >
    <div
      class="box"
      :class="{'is-expanded':article.isInfoExpanded}"
    >
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
            <button 
                class="button"
                v-on:click="$emit('toggle-info', article)"
            >
            <span v-if="article.isInfoExpanded">-</span>
            <span v-else>+</span>
            </button>
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
    },
    expanded: {
      type: Boolean,
    }
  },
  computed: {
    articleWidth: function(){
      return this.isList ? 'is-full' : 'is-half'
    },
  },
	methods: {
  },
  created: function (){
  }
};
</script>

<style>
.box{
  width: 100%;
}
</style>

