const darkModeToggle = document.getElementById("dark-mode-toggle");
const body = document.body;

// Check if user has a preferred color scheme and set initial mode accordingly
if (
  window.matchMedia &&
  window.matchMedia("(prefers-color-scheme: dark)").matches
) {
  body.classList.add("dark-mode");
}

// Toggle dark mode on button click
darkModeToggle.addEventListener("change", () => {
  body.classList.toggle("dark-mode");
});
