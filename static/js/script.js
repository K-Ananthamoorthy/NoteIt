document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.querySelector('[data-collapse-toggle="mobile-menu"]');
    const menu = document.querySelector('#mobile-menu');
    // Ensure the mobile menu is hidden initially
    menu.style.display = 'none';
    toggleButton.addEventListener('click', () => {
        if (menu.style.display === 'none') {
            menu.style.display = 'block';
        } else {
            menu.style.display = 'none';
        }
    });
    const noteForm = document.getElementById('note-form');
    noteForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(noteForm);
        const response = await fetch('/save_note', {
            method: 'POST',
            body: formData
        });
        if (response.ok) {
            document.getElementById('confirmation-message').style.display = 'block';
            noteForm.reset();
        }
        const createNoteBtn = document.getElementById('create-note-btn');
        const noteFormContainer = document.getElementById('note-form');
        createNoteBtn.addEventListener('click', () => {
            noteFormContainer.style.display = 'block';
            createNoteBtn.style.display = 'none';
        });
    });
});