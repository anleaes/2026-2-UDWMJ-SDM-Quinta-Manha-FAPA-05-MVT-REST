const root = document.documentElement;

function setTheme(theme) {
    root.dataset.theme = theme;
    try {
        localStorage.setItem("theme", theme);
    } catch {}
}

function setSavedTheme() {
    let saved = null;

    try {
        saved = localStorage.getItem("theme");
    } catch {}

    if (saved !== null) {
        setTheme(saved);
        console.log(`INFO: Saved theme is \`${saved}\``);
    }
}

setSavedTheme();

function systemTheme() {
    const el    = document.getElementById("system-theme");
    const theme = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";

    el.addEventListener("click", () => {
        setTheme(theme);
    })
}

function lightTheme() {
    const el = document.getElementById("light-theme");

    el.addEventListener("click", () => {
        setTheme("light");
    })
}

function darkTheme() {
    const el = document.getElementById("dark-theme");

    el.addEventListener("click", () => {
        setTheme("dark");
    })
}

systemTheme();
lightTheme();
darkTheme();
