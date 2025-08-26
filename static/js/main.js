//
const carousel = document.querySelector("div#carousel-track");
const imgs = carousel.querySelectorAll("img");

let totalWidth = 0;

for (let img of imgs) {
	totalWidth += img.offsetWidth + parseInt(getComputedStyle(img).marginRight) + parseInt(getComputedStyle(img).marginLeft);
}

carousel.innerHTML += carousel.innerHTML;

const speed = 50; // px / sec
const duration = totalWidth / speed;

carousel.style.animationName = "scroll";
carousel.style.animationDuration = `${ duration }s`;

//
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
