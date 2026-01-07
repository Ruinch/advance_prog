const startBtn = document.getElementById("start-btn");
const container = document.getElementById("hearts-container");
const image = document.getElementById("result-image");
const text = document.getElementById("result-text");
const overlay = document.getElementById("overlay");
const sparklesContainer = document.getElementById("sparkles-container");

/* картинки-сердца */
const heartImages = [
    "/static/images/hearts/heart1.png",
    "/static/images/hearts/heart2.png",
    "/static/images/hearts/heart3.png"
];

/* твои слова */
const messages = [
    "Я люблю твои нежные руки",
    "Когда мы вместе, всё вокруг оживает",
    "Любовь - это ты",
    "Я люблю смотреть с тобой на закат",
    "Если ты хочешь плакать - я буду плакать тоже",
    "Мы будем вместе, даже если всё вокруг глупо", 
    "Мне хорошо, когда ты рядом",
    "Я слышу тебя и чувствую тебя",
    "Мне не важно где я, если я с тобой",
    "Ты мой воздух",
    "Посмотри, как спокойна бывает любовь",
    "Ты мой самый тихий свет",
    "Мне не нужен весь мир, если есть ты",
    "Я тону в твоих глазах",
    "Ты мне снишься чаще, чем реальность",
    "Не хочу просыпаться без тебя",
    "Твоё тепло лечит меня",
    "Мне спокойно рядом с тобой",
    "Давай жить медленно, вдвоём",
    "Мне нравится теряться в тебе",
    "Ночь становится мягче, когда ты рядом",
    "Я боюсь темноты без твоих рук",
    "Я пишу тебе даже молча",
    "Ты читаешь меня между строк"
];

let intervalId = null;
let hideTimer = null;

startBtn.addEventListener("click", () => {
    startBtn.style.display = "none";
    if (!intervalId) {
        intervalId = setInterval(createHeart, 300);
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
    const speed = 0.7 + Math.random() * 0.7;
    const frequency = 0.02 + Math.random() * 0.02;
    const rotationAmplitude = 15 + Math.random() * 10;

    heart.style.width = (60 + Math.random() * 60) + "px";
    heart.style.left = startX + "px";
    heart.style.top = y + "px";

    heart.addEventListener("click", (e) => {
    const rect = heart.getBoundingClientRect();

    for (let i = 0; i < 12; i++) {
        createSparkleAt(
            rect.left + rect.width / 2,
            rect.top + rect.height / 2
        );
    }

    showContent();
});


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
        if (Math.random() < 0.15) {
       const rect = heart.getBoundingClientRect();
        createSparkleAt(
        rect.left + rect.width / 2,
        rect.top + rect.height / 2
    );
}

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

function createSparkle() {
    const sparkle = document.createElement("div");
    sparkle.className = "sparkle";

    const x = Math.random() * window.innerWidth;
    const y = Math.random() * window.innerHeight;

    sparkle.style.left = x + "px";
    sparkle.style.top = y + "px";

    const size = 2 + Math.random() * 3;
    sparkle.style.width = size + "px";
    sparkle.style.height = size + "px";

    sparklesContainer.appendChild(sparkle);

    let life = 0;
    const maxLife = 60 + Math.random() * 40;

    function animate() {
        life++;

        sparkle.style.opacity = Math.sin((life / maxLife) * Math.PI);
        sparkle.style.transform = `translateY(${-life * 0.05}px)`;

        if (life < maxLife) {
            requestAnimationFrame(animate);
        } else {
            sparkle.remove();
        }
    }

    animate();
}

setInterval(() => {
    createSparkle();
    if (Math.random() > 0.5) createSparkle();
}, 300);

function createSparkleAt(x, y) {
    const sparkle = document.createElement("div");
    sparkle.className = "sparkle";

    const size = 2 + Math.random() * 4;
    sparkle.style.width = size + "px";
    sparkle.style.height = size + "px";

    sparkle.style.left = x + "px";
    sparkle.style.top = y + "px";

    sparklesContainer.appendChild(sparkle);

    let life = 0;
    const maxLife = 40 + Math.random() * 20;
    const driftX = (Math.random() - 0.5) * 0.6;
    const driftY = -0.5 - Math.random();

    function animate() {
        life++;

        sparkle.style.opacity = Math.sin((life / maxLife) * Math.PI);
        sparkle.style.transform =
            `translate(${driftX * life}px, ${driftY * life}px)`;

        if (life < maxLife) {
            requestAnimationFrame(animate);
        } else {
            sparkle.remove();
        }
    }

    animate();
}
