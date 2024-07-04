from flask import render_template
from flask import current_app as app
from flask import Flask, request, jsonify
from models import db, Note
def create_app():
    app = Flask(__name__, static_folder='static')

    @app.route("/")
    def home_route():
        return render_template("home.html")

    @app.route("/save_note", methods=["POST"])
    def save_note():
        content = request.form.get("content")
        if content:
            new_note = Note(content=content)
            db.session.add(new_note)
            db.session.commit()
            return jsonify({"message": "Note saved successfully!"}), 200
        return jsonify({"message": "Failed to save note."}), 400

    return app