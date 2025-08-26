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

//
const N_DIVS = 7

const newImg = (src) => {
	const img = document.createElement("img");
	img.src = src ?? "";
	img.style.flex = "0 0 100px";
	img.style.maxWidth = "15vw";
	img.style.margin = "10px";
	img.style.borderRadius = "0px";
	return img;
}

const carousel = document.querySelector("div#carousel-track");

let totalWidth = 0;

for (let i = 0; i < N_DIVS; ++i) {
	const img = newImg("img/01.jpg");
	carousel.appendChild(img);
	totalWidth += img.offsetWidth + parseInt(getComputedStyle(img).marginRight) + parseInt(getComputedStyle(img).marginLeft);
}

carousel.innerHTML += carousel.innerHTML;

const speed = 50; // px / sec
const duration = totalWidth / speed;

carousel.style.animationName = "scroll";
carousel.style.animationDuration = `${ duration }s`;

console.log(duration);

//
const grid = document.querySelector("div#art-grid");
for (let i = 0; i < N_DIVS * 2; ++i) {
	const item = new GalleryItem("AAA", "img/01.jpg", "#");
	grid.appendChild(item);
}

//
class Card extends HTMLDivElement {
	constructor(title, description) {
		super();

		this.classList.add("home-card");

		const h2 = document.createElement("h2");
		h2.innerText = title;

		const p = document.createElement("p");
		p.innerText = description;

		this.appendChild(h2);
		this.appendChild(p);
	}
}

customElements.define("home-card", Card, { extends: "div" });

const homeCards = [
	{
		title: "15",
		description: "YEARS OF LIVING WITH ART, MADE EASY",
	},
	{
		title: "130,000+",
		description: "HOMES WITH ART",
	},
	{
		title: "153",
		description: "COLLECTOR COUNTRIES",
	},
	{
		title: "100,000+",
		description: "ARTISTS COLLECTED",
	},
];

const cards = document.querySelector("div#cards");
homeCards.forEach(card => cards.appendChild(new Card(card.title, card.description)));
