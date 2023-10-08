<script setup>


// ■■■■■■ import > Packages ■■■■■■
import { computed } from 'vue';
// import { onMounted } from 'vue';
// import { ref } from 'vue';
import { useStore } from 'vuex';
// import { useRoute } from 'vue-router';



// ■■■■■■ import > Others ■■■■■■
// import { Icon } from '@iconify/vue';




// ■■■■■■ import > Components ■■■■■■
// import Btn_1 from '../components/_Btn_1_mottomiru.vue';
// import Text_1 from '../components/_Text_1.vue';
// import HelloWorld from './components/HelloWorld.vue'
// import Header from './components/Header.vue';
// import ToolBar from './components/ToolBar.vue';
// import Topimage from './components/Topimage.vue';
// import Footer from './components/Footer.vue';
// import Breadcrumbs from './components/Breadcrumbs.vue';





// ■■■■■■ VueStore ■■■■■■
const store = useStore();
const VIDEOS = computed(() => { return store.getters.GET_VIDEOS; });
// const PERFORMER_LIST = computed(() => { return store.getters.GET_PERFORMER_LIST; });
// const TAG_LIST = computed(() => { return store.getters.GET_TAG_LIST; });
// const MAKER_LIST = computed(() => { return store.getters.GET_MAKER_LIST; });
// const LABEL_LIST = computed(() => { return store.getters.GET_LABEL_LIST; });
// const SERIES_LIST = computed(() => { return store.getters.GET_SERIES_LIST; });
// const KYOUNUKI_LIST = computed(() => { return store.getters.GET_KYOUNUKI_LIST; });
// const VIDEOS_LOADED = computed(() => { return store.getters.GET_VIDEOS_LOADED; });
// const URL_LIST = computed(() => { return store.getters.GET_URL_LIST; });
// const URL_PARAM = computed(() => { return store.getters.GET_URL_PARAM; });
// const URL_JUDGE_PARAM = computed(() => { return store.getters.GET_URL_JUDGE_PARAM; });
// const SUBCONTENTS = computed(() => { return store.getters.GET_SUBCONTENTS; });
// const SUBCONTENTS_ALL = computed(() => { return store.getters.GET_SUBCONTENTS_ALL; });
const DEBUG = computed(() => { return store.getters.GET_DEBUG; });
console.log("DEBUG", DEBUG.value)


// ■■■■■■ VueRouter ■■■■■■
// const route = useRoute();




// import { useMeta } from 'vue-meta'
import { useMeta } from 'vue-meta';
const { meta } = useMeta({});



meta.title = ""


meta.metaTags = [
    { charset: 'utf-8' },
    { name: 'theme-color', content: '#455045' },
    { name: 'langueage', content: '日本語' },
    { name: 'author', content: 'BOOK I.C.'},
    { name: 'robots', content: 'text/html', charset: 'UTF-8'},
    //{ name: 'robots', content: 'index' },
    { "http-equiv": 'Content-Language', content: 'ja' },
    { "http-equiv": 'Expires', content: '86400' },
    { "http-equiv": 'Content-Type', content: 'text/html', charset: 'UTF-8'},



    //■基本設定
    //{ name: 'description', content: '「他の人はどう感じているんだろう」。本を読み終えた後の思いを満たすための本感想ブログです！。今後、本に関する様々な情報を掲載予定です！'},
    { name: 'keywords', content: 'book-ic,本,本感想,本の感想,感想,書評,書店,小説,文庫,ブログ,個人ブログ,読書,書籍,記録,ネタバレ読書,読書記録' },
    { name: 'thumbnail', content: '/src/assets/book-ic_picture.svg' },


    // og 設定
    // １．page type
    //{ property: 'og:type', content: 'website' }, //content: article 
    // ２．title
    //{ property: 'og:title', content: 'BOOK I.C. ～本の感想を創造するブログ～' }, 
    // ３．ページ説明文
    //{ property: 'og:description', content: ' 「他の人はどう感じているんだろう」。本を読み終えた後の思いを満たすための本感想ブログです！。タグ | 小説,文庫,ブログ,本の感想,本感想,読書,書評,書籍,記録,ネタバレ | BOOK I.C.' }, 
    // ４．URL
    //{ property: 'og:url', content: 'absolute_url' }, 
    // ５．サイト名
    { property: 'og:site_name', content: 'BOOK I.C.' }, 
    // ６．その他
    //{ property: 'article:publisher', content: '(6)FacebookページのURL' }, 
    // ７．表示画像
    { property: 'og:image', content: '/src/assets/book-ic.png' }, 

    // Twitterカードの設定 
    //{ name: 'twitter:title', content: 'summary' }, 
    { name: 'twitter:card', content: 'summary' }, 
    { name: 'twitter:site', content: '@BOOK_IC' },

  ]

meta.link = [
    { rel: 'icon', href: '/src/assets/book-ic_icon.svg', type: 'image/x-icon' },
    // { rel: 'stylesheet', href: 'styles.css' },
    { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Sawarabi+Gothic&display=swap',},
    //{ rel: 'canonical', href: 'url',}, 正規化
    //{ rel: 'prev', href: '前のページのURL',}, 
    //{ rel: 'next', href: '次のページのURL',},

  ]

// meta.script = [
//       // Google ADSense
//       { async: true, src: "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1203419703310974", crossorigin: "anonymous"},
//     // Google tag (gtag.js)
//     { async: true, src: "https://www.googletagmanager.com/gtag/js?id=G-BS7M4Z8XRZ", crossorigin: "anonymous"},
//     {
//       innerHTML: `
//         window.dataLayer = window.dataLayer || [];
//         function gtag(){dataLayer.push(arguments);}
//         gtag('js', new Date());
//         gtag('config', 'G-BS7M4Z8XRZ');
//         gtag('config', 'UA-244839165-1');
//       `,
//       type: "text/javascript",
//     },
//     {
//       innerHTML: `
//         (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
//         new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
//         j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
//         'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
//         })(window,document,'script','dataLayer','GTM-KKTTVX3');
//       `,
//       type: "text/javascript",
//     },
//     { async: true, type: "application/javascript", src: "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1203419703310974", crossorigin: "anonymous"},

//   ]






</script>




<template>

<v-app>
  <!-- <Header /> -->

    <!-- <template v-slot:title="{ content }">{{ content ? `${content} | SITE_NAME` : `SITE_NAME` }}</template> -->
  <!-- </metaInfo> -->


  <!-- <ToolBar /> -->
  <!-- <Topimage /> -->


  <!-- <Judgeurl /> -->
  <!-- <v-row no-gutters> -->
    <!-- <v-col cols="12"> -->
      <!-- <Breadcrumbs /> -->
    <!-- </v-col> -->
  <!-- </v-row> -->
  <!-- <div id="app"></div> -->
  <v-main class="my-bg-color-white">
    <!-- <router-view /> -->
  </v-main>


  <div>
      データを読み込んでいます...
      <!-- url_judge_param: {{ URL_JUDGE_PARAM }} -->
      VIDEOS: {{ VIDEOS }}
  </div>

  <!-- <Footer /> -->
</v-app>





</template>

<style>

</style>
