document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.edit-button').forEach(button => {
        button.addEventListener('click', function () {
            const noteId = this.dataset.id;
            const noteContent = this.closest('li').querySelector('.note-content').innerText;
            const textarea = document.querySelector('textarea[name="note_content"]');
            const form = textarea.closest('form');

            textarea.value = noteContent;
            form.action = '/update_note';
            form.innerHTML += `<input type="hidden" name="note_id" value="${noteId}">`;
            textarea.focus();
        });
    });

    document.querySelectorAll('.delete-button').forEach(button => {
        button.addEventListener('click', function () {
            const noteId = this.dataset.id;
            const form = document.createElement('form');
            form.action = '/delete_note';
            form.method = 'POST';
            form.innerHTML = `<input type="hidden" name="note_id" value="${noteId}">`;
            document.body.appendChild(form);
            form.submit();
        });
    });
});
