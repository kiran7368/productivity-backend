from flask import Flask, render_template
from config import Config
from utils.db import db
from utils.auth import jwt
from routes.auth_routes import auth_bp
from routes.note_routes import note_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(note_bp)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)