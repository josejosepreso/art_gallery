function checkAdmin() {
	const token = localStorage.getItem("token");
	if (!token)
		return;

	//
	const signoutA = document.createElement("a");
	signoutA.innerText = "Sign out";
	signoutA.href = `/signout?token=${ token }`;
	const accountsBtns = document.querySelector("div#accounts");
	accountsBtns.firstElementChild.remove();
	accountsBtns.appendChild(signoutA);

	//
	const nav = document.querySelector("div#navlinks");
	const dashboardA = document.createElement("a");
	dashboardA.innerText = "Dashboard";
	dashboardA.href = `/dashboard?token=${ token }`;
	nav.appendChild(dashboardA);
}

checkAdmin();
