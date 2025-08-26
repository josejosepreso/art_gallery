const N_DIVS = 7

const newImg = (src) => {
	const img = document.createElement("img");
	img.src = src ?? "";
	img.style.flex = "0 0 100px";
	img.style.maxWidth = "15vw";
	img.style.margin = "10px";
	img.style.borderRadius = "5px";
	return img;
}

const carousel = document.querySelector("div#carousel-track");

let totalWidth = 0;

for (let i = 0; i < N_DIVS; ++i) {
	const img = newImg("assets/img/01.jpg");
	carousel.appendChild(img);
	totalWidth += img.offsetWidth + parseInt(getComputedStyle(img).marginRight) + parseInt(getComputedStyle(img).marginLeft);
}

carousel.innerHTML += carousel.innerHTML;

const speed = 50; // px / sec
const duration = totalWidth / speed;

carousel.style.animationName = "scroll";
carousel.style.animationDuration = `${ duration }s`;
