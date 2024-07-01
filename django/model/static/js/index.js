logout_form = document.querySelector("#logout_form");

logout = document.querySelector("#logout");

logout.addEventListener("click", (e) => {
  e.preventDefault();
  logout_form.submit();
});
