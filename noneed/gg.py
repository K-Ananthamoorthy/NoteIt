from flask import Flask, render_template, request, redirect, url_for
from models import db, Note

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def landing():
        return render_template('landing.html')

    @app.route('/notes')
    def home():
        notes = Note.query.all()
        return render_template('home.html', notes=notes)

    @app.route('/add_note', methods=['POST'])
    def add_note():
        note_content = request.form['note_content']
        if note_content:
            new_note = Note(content=note_content)
            db.session.add(new_note)
            db.session.commit()
        return redirect(url_for('home'))

    @app.route('/update_note', methods=['POST'])
    def update_note():
        note_id = request.form['note_id']
        note_content = request.form['note_content']
        note = Note.query.get(note_id)
        if note:
            note.content = note_content
            db.session.commit()
        return redirect(url_for('home'))

    @app.route('/delete_note', methods=['POST'])
    def delete_note():
        note_id = request.form['note_id']
        note = Note.query.get(note_id)
        if note:
            db.session.delete(note)
            db.session.commit()
        return redirect(url_for('home'))

    return app
