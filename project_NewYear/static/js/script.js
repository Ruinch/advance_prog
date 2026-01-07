const startBtn = document.getElementById("start-btn");
const container = document.getElementById("hearts-container");
const image = document.getElementById("result-image");
const text = document.getElementById("result-text");
const overlay = document.getElementById("overlay");

/* картинки-сердца */
const heartImages = [
    "/static/images/hearts/heart1.png",
    "/static/images/hearts/heart2.png",
    "/static/images/hearts/heart3.png"
];

/* твои слова */
const messages = [
    "Ты самый лучший ❤️",
    "Спасибо тебе",
    "Я очень ценю тебя",
    "Ты делаешь меня счастливым",
    "Это для тебя 💖"
];

let intervalId = null;
let hideTimer = null;

startBtn.addEventListener("click", () => {
    startBtn.style.display = "none";
    if (!intervalId) {
        intervalId = setInterval(createHeart, 400);
    }
});

function createHeart() {
    const heart = document.createElement("img");
    heart.className = "heart";

    heart.src = heartImages[
        Math.floor(Math.random() * heartImages.length)
    ];

    heart.style.left = Math.random() * 90 + "vw";
    heart.style.width = (60 + Math.random() * 60) + "px";

    heart.addEventListener("click", showContent);

    container.appendChild(heart);
    setTimeout(() => heart.remove(), 6000);
}

function showContent() {
    const randomImage = Math.floor(Math.random() * 20) + 1;
    const randomText =
        messages[Math.floor(Math.random() * messages.length)];

    if (hideTimer) {
        clearTimeout(hideTimer);
        hideTimer = null;
    }

    // сброс
    image.classList.remove("show");
    text.classList.remove("show");

    overlay.classList.add("show");

    setTimeout(() => {
        image.src = `/static/images/${randomImage}.jpg`;
        text.textContent = randomText;

        image.classList.add("show");
        text.classList.add("show");

        hideTimer = setTimeout(hideContent, 4000);
    }, 50);
}

function hideContent() {
    overlay.classList.remove("show");
    image.classList.remove("show");
    text.classList.remove("show");
}
