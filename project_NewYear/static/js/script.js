const startBtn = document.getElementById("start-btn");
const container = document.getElementById("hearts-container");
const image = document.getElementById("result-image");
const text = document.getElementById("result-text");
const overlay = document.getElementById("overlay");
const heartImages = [
    "/static/images/hearts/heart1.jpg",
    "/static/images/hearts/heart2.jpg",
    "/static/images/hearts/heart3.jpg"
];

/* ✏️ ТУТ ПИШЕШЬ СВОИ СЛОВА */
const messages = [
    "Ты самый лучший ❤️",
    "Спасибо тебе",
    "Я очень ценю тебя",
    "Ты делаешь меня счастливым",
    "Это для тебя 💖"
];

startBtn.addEventListener("click", () => {
    startBtn.style.display = "none";
    setInterval(createHeart, 200);
});


function createHeart() {
    const heart = document.createElement("img");

    const randomHeart =
        heartImages[Math.floor(Math.random() * heartImages.length)];

    heart.src = randomHeart;
    heart.className = "heart";

    heart.style.left = Math.random() * 90 + "vw";
    heart.style.width = (30 + Math.random() * 80) + "px";

    heart.addEventListener("click", showContent);

    container.appendChild(heart);

    setTimeout(() => heart.remove(), 6000);
}

function showContent() {
    const randomImage = Math.floor(Math.random() * 20) + 1;
    const randomText = messages[Math.floor(Math.random() * messages.length)];

    image.classList.remove("show");
    text.classList.remove("show");
    overlay.classList.remove("show");

    setTimeout(() => {
        image.src = `/static/images/${randomImage}.jpg`;
        text.textContent = randomText;

        overlay.classList.add("show");
        image.classList.add("show");
        text.classList.add("show");

        setTimeout(hideContent, 4000);
    }, 50);
}

function hideContent() {
    image.classList.remove("show");
    text.classList.remove("show");
    overlay.classList.remove("show");
}
