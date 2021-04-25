import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import ForceGraph3D from "3d-force-graph";
import Three from "three";

Vue.config.productionTip = false;

new Vue({
	vuetify,
	Three,
	ForceGraph3D,
	render: (h) => h(App),
}).$mount("#app");
