const toggleBtn = document.getElementById("themeToggle");
const icon = document.getElementById("themeIcon");
const root = document.documentElement;

// Load saved theme
if (localStorage.getItem("theme") === "dark") {
  root.classList.add("dark");
  icon.textContent = "☀️";
} else {
  icon.textContent = "🌙";
}

toggleBtn.addEventListener("click", () => {
  root.classList.toggle("dark");
  const isDark = root.classList.contains("dark");

  icon.textContent = isDark ? "☀️" : "🌙";
  localStorage.setItem("theme", isDark ? "dark" : "light");
});
