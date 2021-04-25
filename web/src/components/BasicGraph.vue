<template>
	<div>
		<div id="3d-graph"></div>
	</div>
</template>

<script>
	import ForceGraph3D from "3d-force-graph";
	// import * as THREE from "three";
	import SpriteText from "three-spritetext";

	export default {
		name: "BasicGraph",
		mounted() {
			const jsonData = require("../../../data/result2.json");
			const graph = ForceGraph3D({ controlType: "orbit" })(document.getElementById("3d-graph"));

			let temp = {
				nodes: [],
				links: [],
			};

			for (let link of jsonData["links"]) {
				if (link.value > 0.23) {
					temp["links"].push(link);
				}
			}

			temp["nodes"] = jsonData["nodes"];

			// TODO: Iterate over links; add source to .neighbors for target and vise-versa; add all links to .links

			const highlightNodes = new Set();
			const highlightLinks = new Set();
			let hoverNode = null;

			graph
				.nodeLabel("id")
				.graphData(temp)
				.linkOpacity(0.5)
				.nodeColor((node) => (highlightNodes.has(node) ? (node === hoverNode ? "rgb(255,0,0,1)" : "rgba(255,160,0,0.8)") : "rgba(0,255,255,0.6)"))
				.linkWidth((link) => (highlightLinks.has(link) ? 4 : 0.75))
				.linkDirectionalParticles((link) => (highlightLinks.has(link) ? 4 : 0))
				.linkDirectionalParticleWidth(4)
				// .onNodeHover((node) => {
				// 	if ((!node && !highlightNodes.size) || (node && hoverNode === node)) return;

				// 	highlightNodes.clear();
				// 	highlightLinks.clear();
				// 	if (node) {
				// 		highlightNodes.add(node);
				// 		node.neighbors.forEach((neighbor) => highlightNodes.add(neighbor));
				// 		node.links.forEach((link) => highlightLinks.add(link));
				// 	}

				// 	hoverNode = node || null;

				// 	updateHighlight();
				// })
				// .onLinkHover((link) => {
				// 	highlightNodes.clear();
				// 	highlightLinks.clear();

				// 	if (link) {
				// 		highlightLinks.add(link);
				// 		highlightNodes.add(link.source);
				// 		highlightNodes.add(link.target);
				// 	}

				// 	updateHighlight();
				// })

				.enableNodeDrag(false)
				.nodeLabel((node) => node.name)

				// .nodeThreeObject(({ id }) => {
				// 	const imgTexture = new THREE.TextureLoader().load(`./imgs/${id}.jpg`);
				// 	const material = new THREE.SpriteMaterial({ map: imgTexture });
				// 	const sprite = new THREE.Sprite(material);
				// 	sprite.scale.set(16, 16);
				// 	return sprite;
				// })

				.nodeThreeObject((node) => {
					const sprite = new SpriteText(node.name);
					sprite.material.depthWrite = true; // ma	ke sprite background transparent
					sprite.color = "White";
					sprite.textHeight = 6;
					return sprite;
				})

				// .nodeThreeObject(({ id }) => {
				// 	let texture = new THREE.TextTexture({
				// 		alignment: "left",
				// 		color: "#24ff00",
				// 		fontFamily: '"Times New Roman", Times, serif',
				// 		fontSize: 32,
				// 		fontStyle: "italic",
				// 		text: ["Twinkle, twinkle, little star,", "How I wonder what you are!", "Up above the world so high,", "Like a diamond in the sky."].join("\n"),
				// 	});
				// 	const imgTexture = new THREE.TextureLoader().load(`./imgs/${id}.jpg`);
				// 	const material = new THREE.SpriteMaterial({ map: imgTexture });
				// 	let sprite = new THREE.Sprite(material);
				// 	return sprite;
				// })

				.onNodeClick((node) => {
					const distance = 250;
					const distRatio = 1 + distance / Math.hypot(node.x, node.y, node.z);
					graph.cameraPosition({ x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio }, node, 3000);
				})

				.d3Force("link")
				.distance((link) => Math.abs(link.value / 0.5 - 1) * 100);

			// function updateHighlight() {
			// 	// trigger update of highlighted objects in scene
			// 	graph
			// 		.nodeColor(graph.nodeColor())
			// 		.linkWidth(graph.linkWidth())
			// 		.linkDirectionalParticles(graph.linkDirectionalParticles());
			// }

			// function findNode(id) {
			// 	temp.nodes.forEach((node) => {
			// 		if (node.id === id) {
			// 			return node;
			// 		}
			// 	});
			// 	return { id: -1, name: "undefined" };
			// }
		},
	};
</script>
