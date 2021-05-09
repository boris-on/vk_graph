<template>
  <v-app>
    <v-app-bar color="#000F11" dark flat>
      <v-row align="center">
        <v-col class="pl-6">
          <v-row align="center">
            <v-img src="logo.png" max-height="40" max-width="40"></v-img>
            <v-toolbar-title class="ml-3">VK Audience Graph</v-toolbar-title>
          </v-row>
        </v-col>

        <v-spacer></v-spacer>

        <v-col class="text-right">
          <v-tooltip bottom transition="None">
            <template v-slot:activator="{ on, attrs }">
              <v-hover v-slot="{ hover }" open-delay="0" close-delay="0">
                <v-icon
                  class="mr-8"
                  v-bind="attrs"
                  v-on="on"
                  size="big"
                  :color="hover ? 'rgb(90, 90, 255)' : 'rgb(180, 180, 180)'"
                >
                  mdi-cog-outline
                </v-icon>
              </v-hover>
            </template>
            <span>Settings</span>
          </v-tooltip>

          <v-tooltip class="pr-7" bottom transition="None">
            <template v-slot:activator="{ on, attrs }">
              <v-hover v-slot="{ hover }" open-delay="0" close-delay="0">
				<a href="/build_your_graph">
                <v-icon
                  class="mr-8"
                  v-bind="attrs"
                  v-on="on"
                  size="big"
                  :color="hover ? 'rgb(90, 90, 255)' : 'rgb(180, 180, 180)'"
                >
                  mdi-account-group
                </v-icon></a>
              </v-hover>
            </template>
            <span>Community</span>
          </v-tooltip>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-main>
      <!-- <ImgGraph /> -->
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
// import ImgGraph from "./components/ImgGraph";
// import BasicGraph from "./components/BasicGraph";

export default {
  name: "App",

  components: {
    // ImgGraph,
    // BasicGraph,
  },

  data: () => ({
    //
  }),
};
</script>
