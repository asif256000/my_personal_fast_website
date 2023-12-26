const darkModeToggle = document.getElementById("dark-mode-toggle");
let toggleText = document.getElementById("toggle-text");
const body = document.body;
const dark_mode_text = "Welcome to the dark side!";
const light_mode_text = "Come to the dark side...";

// Check if user has a preferred color scheme and set initial mode accordingly
if (
  window.matchMedia &&
  window.matchMedia("(prefers-color-scheme: dark)").matches
) {
  body.classList.add("dark-mode");
  darkModeToggle.checked = true;
  toggleText.innerHTML = dark_mode_text;
} else {
  body.classList.remove("dark-mode");
  darkModeToggle.checked = false;
  toggleText.innerHTML = light_mode_text;
}

// Toggle dark mode on button click
darkModeToggle.addEventListener("change", () => {
  body.classList.toggle("dark-mode");
  if (body.classList.contains("dark-mode")) {
    toggleText.innerHTML = dark_mode_text;
  } else {
    toggleText.innerHTML = light_mode_text;
  }
});
