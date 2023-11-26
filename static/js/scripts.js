// function toggleDetails(card) {
//   var details = card.querySelector('.details');
//   details.classList.toggle('visible');
// }

// ======================== // CARD DETAIL KLIK // ======================== //
// function toggleDetails(card) {

//   card.classList.toggle("active");

//   // Untuk menutup kartu lain jika yang satu diklik
//   var cards = document.querySelectorAll('.card');
//   cards.forEach(function (c) {
//     if (c !== card && c.classList.contains('active')) {
//       c.classList.remove('active');
//     }
//   });
//   // Dapatkan detail dari kartu yang diklik
//   var details = card.querySelector('.details');

//   // Periksa apakah detail sedang terlihat
//   var isVisible = details.classList.contains('visible');

//   // Jika terlihat, sembunyikan detailnya; jika tidak, tampilkan
//   if (isVisible) {
//     details.classList.remove('visible');
//   } else {
//     // Sembunyikan detail dari semua kartu yang sedang terlihat
//     var visibleCards = document.querySelectorAll('.card .details.visible');
//     visibleCards.forEach(function (visibleCard) {
//       visibleCard.classList.remove('visible');
//     });

//     // Tampilkan detail dari kartu yang diklik
//     details.classList.add('visible');
//   }
// }

function toggleDetails(card) {
  // Toggle class 'active' pada kartu yang diklik
  card.classList.toggle("active");

  // Menutup kartu lain jika yang satu diklik
  closeOtherCards(card);

  // Menangani detail kartu yang diklik
  handleCardDetails(card);
}

function closeOtherCards(clickedCard) {
  var cards = document.querySelectorAll('.card');
  cards.forEach(function (c) {
    if (c !== clickedCard && c.classList.contains('active')) {
      c.classList.remove('active');
    }
  });
}

function handleCardDetails(card) {
  var details = card.querySelector('.details');

  // Periksa apakah detail sedang terlihat
  var isVisible = details.classList.contains('visible');

  // Jika terlihat, sembunyikan detailnya; jika tidak, tampilkan
  if (isVisible) {
    details.classList.remove('visible');
  } else {
    // Sembunyikan detail dari semua kartu yang sedang terlihat
    hideVisibleCardDetails();

    // Tampilkan detail dari kartu yang diklik
    details.classList.add('visible');
  }
}

function hideVisibleCardDetails() {
  var visibleCards = document.querySelectorAll('.card .details.visible');
  visibleCards.forEach(function (visibleCard) {
    visibleCard.classList.remove('visible');
  });
}

// ======================== // ANIMASI CARD MEMBER // ======================== //
document.addEventListener("DOMContentLoaded", function () {
  // Get all the cards
  const cards = document.querySelectorAll('.card');

  // Loop through each card and apply the animation
  cards.forEach((card, index) => {
    setTimeout(() => {
      card.style.opacity = 1;
      card.style.transform = 'translateY(0)';
    }, index * 500); // Adjust the delay (500ms in this example) based on your preference
  });
});

// ======================== // FORM VALIDASI // ======================== //
// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()


// ======================== // CARD DETAIL FORM // ======================== //
document.addEventListener("DOMContentLoaded", function () {
  const quoteCard = document.getElementById('quoteCard');
  const cardHeader = document.getElementById('cardHeader');
  const cardBody = document.getElementById('cardBody');
  const cardFooter = document.getElementById('cardFooter');

  cardHeader.addEventListener('click', function () {
    // Toggle display of card body and card footer
    cardBody.style.display = (cardBody.style.display === 'none' || cardBody.style.display === '') ? 'block' : 'none';
    cardFooter.style.display = (cardFooter.style.display === 'none' || cardFooter.style.display === '') ? 'block' : 'none';

    // Toggle active-header class for card header
    cardHeader.classList.toggle('active-header');
  });
});


// ======================== // QUOTES & FORM // ======================== //
function toggleCard() {
  $('#quoteCard').toggleClass('d-none');
  $('#editCard').toggleClass('d-none');
}

function saveChanges() {
  var editedQuote = $('#editQuote').val();
  var editedAuthor = $('#editAuthor').val();

  $('#quoteText').text(editedQuote);
  $('#author').text(editedAuthor);

  toggleCard();
}

function deleteQuote() {
  // Implement your delete functionality here
}