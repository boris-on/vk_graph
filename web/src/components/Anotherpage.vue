<template>
  <div id="Auth">
    <h1>Header</h1>
    <a href="https://vk.com">something another</a>
	{{key}}
  </div>
</template>


<script>
import axios from 'axios';
export default {
  name: "Auth",

  components: {},

  data() {
    return {
      key: null,
    };
  },

  mounted() {
    axios
      .get("https://questions.diaryapp.ru/auth/diary?authCode=1&name=0&level=11")
      .then((response) => (this.key = response));
  },

};
</script>
