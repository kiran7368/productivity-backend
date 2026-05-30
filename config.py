class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:736852@127.0.0.1:5432/productivity_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'