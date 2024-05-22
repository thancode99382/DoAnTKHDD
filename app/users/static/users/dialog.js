 // scripts.js

// Get the modal, open button, and close button
const modal = document.getElementById("modal");
const openModalBtn = document.getElementById("openModalBtn");
const closeModalBtn = document.getElementById("closeModalBtn");

// Function to open the modal
openModalBtn.onclick = function(event) {
  event.preventDefault();
  modal.style.display = "block";
}

// Function to close the modal
closeModalBtn.onclick = function() {
  modal.style.display = "none";
}

// Close the modal when clicking outside of the modal content
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}