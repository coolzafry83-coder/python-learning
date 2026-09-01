// Cybersecurity Portfolio
// Basic interactive behavior

document.addEventListener("DOMContentLoaded", () => {
    console.log("Cybersecurity Portfolio loaded successfully.");
});
function openImage(src) {
    const overlay = document.createElement("div");

    overlay.className = "image-overlay";

    const image = document.createElement("img");
    image.src = src;

    overlay.appendChild(image);
    document.body.appendChild(overlay);

    overlay.addEventListener("click", function () {
        overlay.remove();
    });
}