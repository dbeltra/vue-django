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
            Switch
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
                    name="staggered-fade"
                    tag="div"
                    v-on:before-enter="beforeEnter"
                    v-on:enter="enter"
                    v-on:leave="leave"
                    v-bind:css="false"
                    class="columns is-multiline">
                    <Article
                        v-for="article in computedArticles"
                        :key="article.id"
                        :article="article"
                        :isList="isList"
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
            var vm = this
            return this.allArticles.filter(function (article) {
                return article.name.toLowerCase().indexOf(vm.query.toLowerCase()) !== -1
            })
        }
    },
	methods: {
        switchDisplay: function(){
            this.isList = !this.isList
        },

        beforeEnter: function (el) {
            el.style.opacity = 0
            el.style.height = 0
        },
        enter: function (el, done) {
            var delay = el.dataset.index * 150
            // setTimeout(function () {
            // Velocity(
            //     el,
            //     { opacity: 1, height: "auto"},
            //     { complete: done }
            // )
            // }, delay)
        },
        leave: function (el, done) {
            var delay = el.dataset.index * 150
            // setTimeout(function () {
            //     Velocity(
            //     el,
            //     { opacity: 0, height: 0 },
            //     { complete: done }
            //     )
            // }, delay)
        },
        // showAllArticles: function(){
        //     this.allArticles.forEach(element => {
        //         this.displayedArticles.push(element)                
        //     });
        // },
        // flashList: function(){
        //     console.log('flash')
        //     let numArticles = this.displayedArticles.length
        //     let articlesCopy = this.displayedArticles.slice()

        //     for (let index = 0; index < numArticles; index++) {
        //         this.displayedArticles.pop()
        //     }

        //     articlesCopy.forEach(element => {
        //         this.displayedArticles.push(element)                
        //     });

        // }
    },
};
</script>

<style>
.column {
  display: flex;
}
</style>
