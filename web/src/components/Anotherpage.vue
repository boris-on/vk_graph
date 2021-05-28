<template>
  <div id="Auth">
    <a href="https://vk.com">using your token...</a>
    {{ groupsList }}
  </div>
</template>


<script>
import axios from "axios";
export default {
  name: "Auth",

  components: {},

  data() {
    return {
      key:
        "50d69cb643b0a669e672f32fb2d6b0df18bfd0369d1acd7e20f1e16d3b4d84924f02758cd32f32732133b",
      groupsList: null,
    };
  },

  mounted() {
    axios
      //   .get("https://questions.diaryapp.ru/auth/diary?authCode=1&name=0&level=11")
      //   .then((response) => (this.key = response));
	
      .get("https://api.vk.com/method/groups.get", {
        params: {
          extended: 0,
          count: 1000,
          access_token: this.key,
          v: "5.130",
        },
      })
      .then((response) => (this.groupsList = response["data"]["response"]["items"]));
  },
};
</script>
