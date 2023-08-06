const forms = document.querySelector(".forms"),
      pwShowHide = document.querySelectorAll(".eye-icon"),
      links = document.querySelectorAll(".link");

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");
        
        pwFields.forEach(password => {
            if(password.type === "password"){
                password.type = "text";
                eyeIcon.classList.replace("bx-hide", "bx-show");
                return;
            }
            password.type = "password";
            eyeIcon.classList.replace("bx-show", "bx-hide");
        })
        
    })
})      

links.forEach(link => {
    link.addEventListener("click", e => {
       e.preventDefault(); //preventing form submit
       forms.classList.toggle("show-signup");
    })
})


// JavaScript
const loginForm = document.getElementById("form login");
const signupForm = document.getElementById("form signup");

loginForm.addEventListener("field button-field", async (e) => {
  e.preventDefault();
  const formData = new FormData(loginForm);
  const responseData = await fetch("/login/", {
    method: "POST",
    body: formData,
  }).then((response) => response.json());
  console.log(responseData);
});

signupForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(signupForm);
  const responseData = await fetch("/signup/", {
    method: "POST",
    body: formData,
  }).then((response) => response.json());
  console.log(responseData);
});
