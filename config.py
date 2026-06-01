import os

class Config:
    DATABASE_URL = os.environ.get("DATABASE_URL")

    if DATABASE_URL:
        # Render / production
        SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace("postgres://", "postgresql://")
    else:
        # Local development
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:736852@127.0.0.1:5432/productivity_db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'