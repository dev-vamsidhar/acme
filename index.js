const inputField = document.getElementById("rollno");
console.log(inputField);

inputField.addEventListener("input", function () {
  if (inputField.value.length === 10) {
    const imageDiv = document.getElementById("image");
    const image = new Image();
    image.src = "images/" + inputField.value + ".jpg";
    image.alt = "Image not found";
    if (imageDiv.firstChild) {
      imageDiv.replaceChild(image, imageDiv.firstChild);
    } else {
      imageDiv.appendChild(image);
    }
  }
});
