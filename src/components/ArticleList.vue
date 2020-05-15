<template>
    <section v-if="errored">
        <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
    </section>
    <section v-else>
        <div v-if="loading">Loading...</div>
        <div v-else>
            <button 
                class="button"
                v-on:click="switchDisplay()"
            >
            <span v-if="isList">Grid</span>
            <span v-else>List</span>
            </button>

            <div>
                <p class="control has-icons-left">
                <input v-model="query" class="input" type="text" placeholder="Search">
                <span class="icon is-left">
                    <i class="fas fa-search" aria-hidden="true"></i>
                </span>
                </p>
            </div>
            <div v-if="computedArticles.length">
                <transition-group
                    name="articles-list"
                    tag="div"
                    class="columns is-multiline"
                    @toggle-expand="handleEvent()">
                    <Article
                        v-for="article in computedArticles"
                        :key="article.id"
                        :article="article"
                        :isList="isList"
                        v-on:toggle-info="toggleInfo(article)"
                    ></Article>
                </transition-group>
            </div>
            <div v-else>
                No articles found
            </div>
        </div>
    </section>
</template>


<script>

import Article from './Article.vue'
import axios from "axios"
import Cookies from 'js-cookie'

export default {
  /* eslint-disable */
    components: {
        Article
    },
    name: 'ArticleList',
    data() {
        return { 
            allArticles: [],
            loading: true,
            errored: false,
            isList: false,
            query: '',
        }
    },
    created: function() {
        axios({
          url: 'http://localhost:8000/api/articles/',
          method: 'get',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': Cookies.get('csrftoken')
          },     
        })
        .then(res => {
            res.data.forEach(article => { article['isInfoExpanded'] = false });
            this.allArticles = res.data;
        })
        .catch(() => {
            this.errored = true
        })
        .finally(() => {
            this.loading = false
        })

    },
    computed: {
        computedArticles: function () {
            var self = this
            return this.allArticles.filter(function (article) {
                return article.name.toLowerCase().indexOf(self.query.toLowerCase()) !== -1
            })
        }
    },
	methods: {
        switchDisplay: function(){
            this.isList = !this.isList
        },
        toggleInfo: function (article) {
            console.log(article)
            const foundArticle = this.allArticles.find((articleListEl) => articleListEl.id === article.id)
            foundArticle.isInfoExpanded = !foundArticle.isInfoExpanded
        }
    },
};
</script>

<style>
.column {
  display: flex;
}
.articles-list-enter, .articles-list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}
.articles-list-leave-active {
  position: absolute;
}
</style>
