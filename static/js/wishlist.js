document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".wishlist img").forEach(function (icon) {
    icon.addEventListener("click", function (event) {
      event.preventDefault();
      var productId = this.getAttribute("data-product-id");

      fetch(`/add_to_wishlist/${productId}/`, {
        method: "GET",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "success") {
            alert(data.message);
          } else {
            alert("Failed to add product to wishlist");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("login to add product to wishlist");
        });
    });
  });
});
