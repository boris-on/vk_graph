import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import ForceGraph3D from "3d-force-graph";
import Three from "three";
import VueRouter from "vue-router";
import BasicGraph from "./components/BasicGraph"
import AnotherPage from "./components/Anotherpage"

Vue.config.productionTip = false;
Vue.use(VueRouter);

const routes = [
	{
		path: "",
		component: BasicGraph,
	},
	{
		path: "/build_your_graph",
		component: AnotherPage,
	}
];

const router = new VueRouter({
	routes,
	mode: "history",
});


new Vue({
	vuetify,
	Three,
	ForceGraph3D,
	router,
	render: (h) => h(App),
}).$mount("#app");
