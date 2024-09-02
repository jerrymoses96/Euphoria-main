const leftArrow = document.querySelector(".left-arrow");
const rightArrow = document.querySelector(".right-arrow");
const arrivalCards = document.querySelector(".arrival-cards");

let currentIndex = 0;
const totalCards = document.querySelectorAll(".arrival-card-content").length;

leftArrow.addEventListener("click", () => {
  if (currentIndex > 0) {
    currentIndex--;
  } else {
    currentIndex = totalCards - 1; // Loop to the last card
  }
  updateSlider();
});

rightArrow.addEventListener("click", () => {
  if (currentIndex < totalCards - 4) {
    currentIndex++;
  } else {
    currentIndex = 0; // Loop to the first card
  }
  updateSlider();
});

function updateSlider() {
  const width = arrivalCards.querySelector(".arrival-card-content").clientWidth;
  arrivalCards.style.transform = `translateX(-${currentIndex * width}px)`;
}
