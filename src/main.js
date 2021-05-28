import Vue from "vue";
import App from "./App.vue";
// import vuetify from "./plugins/vuetify";
import ForceGraph3D from "3d-force-graph";
import Three from "three";
import VueRouter from "vue-router";
import BasicGraph from "./components/BasicGraph"


Vue.config.productionTip = false;
Vue.use(VueRouter);

const routes = [
	{
		path: "",
		component: BasicGraph,
	},
];

const router = new VueRouter({
	routes,
	mode: "history",
});


new Vue({
	// vuetify,
	Three,
	ForceGraph3D,
	router,
	render: (h) => h(App),
}).$mount("#app");
