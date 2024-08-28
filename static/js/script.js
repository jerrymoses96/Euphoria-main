document.addEventListener("DOMContentLoaded", function () {
  const menubar = document.getElementById("menubar");
  const dropdownMenu = document.getElementById("dropdownMenu");
  const closeIcon = document.getElementById("closeIcon");

  if (menubar && dropdownMenu && closeIcon) {
    // Toggle dropdown on menubar click
    menubar.addEventListener("click", function () {
      dropdownMenu.classList.toggle("show");
    });

    // Hide dropdown on close icon click
    closeIcon.addEventListener("click", function () {
      dropdownMenu.classList.remove("show");
    });

    // Optional: Hide dropdown when clicking outside
    document.addEventListener("click", function (event) {
      if (
        !menubar.contains(event.target) &&
        !dropdownMenu.contains(event.target)
      ) {
        dropdownMenu.classList.remove("show");
      }
    });
  } else {
    console.error("Element not found");
  }

  // Slider script

  const slider = document.querySelector("#spotlight .spotlight-slider");
  const cards = document.querySelectorAll("#spotlight .spotlight-card");
  const buttonLeft = document.querySelector("#spotlight .button-1");
  const buttonRight = document.querySelector("#spotlight .button-2");
  const progressBar = document.querySelector(".progress-bar");

  let currentIndex1 = 0;
  const visibleCards = Math.floor(slider.offsetWidth / cards[0].offsetWidth);
  const maxIndex = cards.length - visibleCards;

  // Update slider position and progress bar
  function updateSliderPosition(direction = 0) {
    const cardWidth = cards[0].offsetWidth;

    // Update current index based on direction
    if (direction === 1 && currentIndex1 < maxIndex) {
      currentIndex1++;
    } else if (direction === -1 && currentIndex1 > 0) {
      currentIndex1--;
    }

    // Calculate new scroll value
    const newTransformValue = currentIndex1 * cardWidth;

    // Update slider position
    slider.scrollLeft = newTransformValue;

    // Update progress bar width
    const progress = ((currentIndex1 + 1) / (maxIndex + 1)) * 100;
    progressBar.style.width = `${progress}%`;
  }

  buttonLeft.addEventListener("click", () => {
    updateSliderPosition(-1);
  });

  buttonRight.addEventListener("click", () => {
    updateSliderPosition(1);
  });

  // Initialize progress bar
  updateSliderPosition();
});
