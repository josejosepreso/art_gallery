class GalleryItem extends HTMLDivElement {
	constructor (title, img_src, link) {
		super();

		this.classList.add("gallery-item");

		const img = document.createElement("img");
		img.src = img_src;

		const h3 = document.createElement("h3");
		h3.innerText = title;

		const a = document.createElement("a");
		a.innerText = "Explore the Best Art of the Season";
		a.href = link;

		this.appendChild(img);
		this.appendChild(h3);
		this.appendChild(a);
	}
}

customElements.define("gallery-item", GalleryItem, { extends: "div" });
