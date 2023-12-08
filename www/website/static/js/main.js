const contactDeleteBtns = document.querySelectorAll('.contact-delete');

if (contactDeleteBtns) {
  Array.from(contactDeleteBtns).forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if (!confirm('Are you sure want to delete it?')) {
        e.preventDefault();
        return;
      }
    })
  });
}