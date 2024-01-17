let darkMode = localStorage.getItem("darkMode");
const systemDarkMode =
  window.matchMedia &&
  window.matchMedia("(prefers-color-scheme: dark)").matches;

// const darkModeToggle = document.querySelector("#dark-mode-toggle");
const darkModeToggle = document.getElementById("dark-mode-toggle");
const toggleText = document.getElementById("toggle-text");
const body = document.body;
const dark_mode_text = "Welcome to the dark side!&nbsp;&nbsp;&nbsp;";
const light_mode_text = "Come to the dark side...&nbsp;&nbsp;&nbsp;";

const enableDarkMode = () => {
  // 1. Add the class to the body
  body.classList.add("dark-mode");
  // 2. Update darkMode in localStorage
  localStorage.setItem("darkMode", "enabled");
  darkModeToggle.checked = true;
  toggleText.innerHTML = dark_mode_text;
};

const disableDarkMode = () => {
  // 1. Remove the class from the body
  body.classList.remove("dark-mode");
  // 2. Update darkMode in localStorage
  localStorage.setItem("darkMode", "disabled");
  darkModeToggle.checked = false;
  toggleText.innerHTML = light_mode_text;
};

// Check if user has a preferred color scheme and set initial mode accordingly
if (darkMode === "enabled") {
  enableDarkMode();
} else if (darkMode === "disabled") {
  disableDarkMode();
} else if (systemDarkMode) {
  enableDarkMode();
} else {
  disableDarkMode();
}

darkModeToggle.addEventListener("click", () => {
  // get the current value of the "darkMode" item in the localStorage
  darkMode = localStorage.getItem("darkMode");

  if (darkMode === "enabled") {
    disableDarkMode();
  } else {
    enableDarkMode();
  }
});

// Toggle dark mode on button click
// darkModeToggle.addEventListener("change", () => {
//   body.classList.toggle("dark-mode");
//   if (body.classList.contains("dark-mode")) {
//     toggleText.innerHTML = dark_mode_text;
//   } else {
//     toggleText.innerHTML = light_mode_text;
//   }
// });
