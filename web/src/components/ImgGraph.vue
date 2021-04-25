<template>
	<div id="3d-graph"></div>
</template>

<script>
	import ForceGraph3D from "3d-force-graph";
	import * as THREE from "three";

	export default {
		name: "ImgGraph",
		mounted() {
			const imgs = ["pic.jpg", "ayy.jpg", "ec.jpg", "kart.jpg"];

			const gData = {
				nodes: imgs.map((img, id) => ({ id, img })),
				links: [...Array(imgs.length).keys()]
					.filter((id) => id)
					.map((id) => ({
						source: id,
						target: Math.round(Math.random() * (id - 1)),
					})),
			};

			const g = ForceGraph3D()(document.getElementById("3d-graph"));
			g.nodeThreeObject(({ img }) => {
				const imgTexture = new THREE.TextureLoader().load(`${img}`);
				const material = new THREE.SpriteMaterial({ map: imgTexture });
				const sprite = new THREE.Sprite(material);
				sprite.scale.set(16, 16);
				console.log(sprite);
				return sprite;
			}).graphData(gData);
		},
	};
</script>
