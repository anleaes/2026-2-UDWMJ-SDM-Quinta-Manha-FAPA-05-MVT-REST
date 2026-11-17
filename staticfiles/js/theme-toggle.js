const root = document.documentElement;

function getSysTheme() {
    return matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function setTheme(theme) {
    let actualTheme = theme;

    if (actualTheme === "system") {
        actualTheme = getSysTheme();
    }

    root.dataset.theme = actualTheme;

    console.log(actualTheme);

    document.querySelectorAll(".data-check").forEach(el => {
        el.toggleAttribute("data-checked", el.id === `${theme}-theme`);
    });

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
        console.log(`INFO: Saved theme is \`${saved}-theme\``);
    }
}

setSavedTheme();

function theme(theme) {
    const el = document.getElementById(`${theme}-theme`);

    el.addEventListener("click", () => {
        setTheme(theme);
    });
}

theme("system");
theme("light");
theme("dark");
