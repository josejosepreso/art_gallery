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
