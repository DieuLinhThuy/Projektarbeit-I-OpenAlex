$(document).ready( function () {
  $('#myTable').DataTable();
} );

const form = document.querySelector('form');
const alert = document.createElement('div');
alert.classList.add('alert');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const title = document.querySelector('#work_title').value;
  if (title.trim() === '') {
    alert.textContent = 'Bitte geben Sie einen Titel ein.';
    form.appendChild(alert);
  } else {
    alert.textContent = `Sie haben nach "${title}" gesucht.`;
    form.appendChild(alert);
  }
});
