import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("postgresql://postgres1:Cj84E5QgJOlyMwjIcFEeJG6jgipv2xVt@dpg-d8dha0q8qa3s739nk9c0-a/productivity_db_jsd0")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'