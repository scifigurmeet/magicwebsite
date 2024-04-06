document.getElementById("magicButton").addEventListener("click", function () {
  // Generate random RGB color values
  var randomColor =
    "rgb(" +
    Math.floor(Math.random() * 256) +
    "," +
    Math.floor(Math.random() * 256) +
    "," +
    Math.floor(Math.random() * 256) +
    ")";

  // Apply the random color to the body background
  document.body.style.backgroundColor = randomColor;
});
