function checkAdmin() {
	const token = localStorage.getItem("token");
	if (!token)
		return;

	//
	const signoutA = document.createElement("a");
	signoutA.innerText = "Sign out";
	signoutA.href = `/signout?token=${ token }`;
	//
	const accountsBtns = document.querySelector("div#accounts");
	accountsBtns.firstElementChild.remove();
	accountsBtns.appendChild(signoutA);

	//
	const nav = document.querySelector("div#navlinks");
	//
	const dashboardA = document.createElement("a");
	dashboardA.innerText = "Dashboard";
	dashboardA.href = `/dashboard?p=1&token=${ token }`;
	//
	const messagesA = document.createElement("a");
	messagesA.innerText = "Messages";
	messagesA.href = `/messages?token=${ token }`;
	//
	nav.appendChild(dashboardA);
	nav.appendChild(messagesA);
}

checkAdmin();
