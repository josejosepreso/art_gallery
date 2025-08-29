function setPagination(pagesShow) {
	console.log(pagesShow)
	const pages = document.querySelector("div#pages");
	if (!pages)
		return;

	const page_arg = window.location.href.match(/\?p=\d+/g);

	let page = 1;
	if (page_arg) {
		page = parseInt(page_arg[0].split("=")[1]);
	}

	const href = page_arg ? window.location.href : window.location.href + "?p=1";

	function pageBtn(n) {
		const a = document.createElement("a");
		a.innerText = n;
		a.href = href.replace(/\?p=\d+/, `?p=${ n }`);
		a.href += "#art-grid";
		a.style.margin = "0 3px";
		if (page == n) {
			a.style.fontWeight = "bold";
			a.style.color = "red";
		}

		return a;
	}

	for (let i = 1; i < pagesShow + 1; ++i)
		pages.appendChild(pageBtn(i));
}
