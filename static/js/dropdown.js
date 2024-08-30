document.addEventListener("DOMContentLoaded", function () {
  const accountIcon = document.querySelector(
    ".navbar-right span:nth-child(2) img"
  );
  const accountDropdown = document.getElementById("accountDropdown");

  accountIcon.addEventListener("click", function () {
    // Toggle display of the account dropdown
    if (accountDropdown.style.display === "block") {
      accountDropdown.style.display = "none";
    } else {
      accountDropdown.style.display = "block";
    }
  });

  // Hide the dropdown if clicked outside
  document.addEventListener("click", function (event) {
    if (
      !accountIcon.contains(event.target) &&
      !accountDropdown.contains(event.target)
    ) {
      accountDropdown.style.display = "none";
    }
  });
});
