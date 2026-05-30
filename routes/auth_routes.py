from flask import Blueprint, request, jsonify
from models.user import User
from utils.db import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(
        username=data.get('username'),
        email=data.get('email'),
        password=data.get('password')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Registered"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(
        email=data.get('email'),
        password=data.get('password')
    ).first()

    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))

    return jsonify({"token": token}), 200