// ===== STYLE SELECTION =====

const styleCards = document.querySelectorAll(".style-card");
let selectedStyle = "";

styleCards.forEach(card => {
  card.addEventListener("click", () => {
    styleCards.forEach(c => c.classList.remove("selected"));
    card.classList.add("selected");
    selectedStyle = card.innerText;
  });
});

// ===== GENERATE DESIGN =====

async function generateDesign() {
  const fileInput = document.getElementById("imageInput");
  const loader = document.getElementById("loader");
  const resultImg = document.getElementById("resultImage");

  if (!fileInput.files[0]) {
    alert("Please upload an image.");
    return;
  }

  if (!selectedStyle) {
    alert("Please select a style.");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  loader.style.display = "block";

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/upload?style=${selectedStyle.toLowerCase()}`,
      {
        method: "POST",
        body: formData
      }
    );

    const data = await response.json();

    loader.style.display = "none";

    if (data.image_url) {
      resultImg.src = data.image_url;
    } else {
      alert("Something went wrong!");
    }

  } catch (error) {
    loader.style.display = "none";
    console.error(error);
    alert("Server error. Make sure backend is running.");
  }
}