const grid = document.querySelector("div#art-grid");
for (let i = 0; i < N_DIVS * 2; ++i) {
	const item = new GalleryItem("AAA", "assets/img/01.jpg", "#");
	grid.appendChild(item);
}
