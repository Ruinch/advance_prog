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
        intervalId = setInterval(createHeart, 150);
    }
});

function createHeart() {
    const heart = document.createElement("img");
    heart.className = "heart";

    heart.src = heartImages[
        Math.floor(Math.random() * heartImages.length)
    ];

    const startX = Math.random() * window.innerWidth;
    let y = window.innerHeight + 100;

    const amplitude = 40 + Math.random() * 40; // ширина волны
    const speed = 1.2 + Math.random() * 1.2;
    const frequency = 0.02 + Math.random() * 0.02;
    const rotationAmplitude = 15 + Math.random() * 10;

    heart.style.width = (60 + Math.random() * 60) + "px";
    heart.style.left = startX + "px";
    heart.style.top = y + "px";

    heart.addEventListener("click", showContent);

    container.appendChild(heart);

    let t = Math.random() * 100;

    function animateHeart() {
        t += 1;
        y -= speed;

        const xOffset = Math.sin(t * frequency) * amplitude;
        const rotation = Math.cos(t * frequency) * rotationAmplitude;

        heart.style.transform =
            `translate(${xOffset}px, 0) rotate(${rotation}deg)`;

        heart.style.top = y + "px";

        if (y < -150) {
            heart.remove();
            return;
        }

        requestAnimationFrame(animateHeart);
    }

    animateHeart();
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
