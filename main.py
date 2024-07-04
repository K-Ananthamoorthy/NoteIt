import logging
from flask import Flask, render_template
from routes import create_app, db
import os

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)
with app.app_context():
    db.create_all()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
