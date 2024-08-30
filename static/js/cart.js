document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".add-cart").forEach(function (button) {
    button.addEventListener("click", function (event) {
      event.preventDefault();
      var productId = this.getAttribute("data-product-id");

      fetch(`/add_to_cart/${productId}/`, {
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
            alert("Failed to add product to cart");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("login to add product to cart");
        });
    });
  });
});
