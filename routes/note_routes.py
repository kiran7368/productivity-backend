from flask import Blueprint, request, jsonify
from models.note import Note
from utils.db import db
from flask_jwt_extended import jwt_required, get_jwt_identity

note_bp = Blueprint('notes', __name__)

# CREATE NOTE (Protected)
@note_bp.route('/notes', methods=['POST'])
@jwt_required()
def create_note():
    user_id = get_jwt_identity()
    data = request.json

    new_note = Note(
        user_id=user_id,
        title=data.get('title'),
        content=data.get('content')
    )

    db.session.add(new_note)
    db.session.commit()

    return jsonify({"msg": "Note created"}), 201


# GET NOTES (Protected)
@note_bp.route('/notes', methods=['GET'])
@jwt_required()
def get_notes():
    user_id = get_jwt_identity()

    notes = Note.query.filter_by(user_id=user_id).all()

    result = []
    for note in notes:
        result.append({
            "id": note.id,
            "title": note.title,
            "content": note.content
        })

    return jsonify(result), 200

# UPDATE NOTE
@note_bp.route('/notes/<int:id>', methods=['PUT'])
@jwt_required()
def update_note(id):
    user_id = get_jwt_identity()
    data = request.json

    note = Note.query.filter_by(id=id, user_id=user_id).first()

    if not note:
        return jsonify({"msg": "Note not found"}), 404

    note.title = data.get('title')
    note.content = data.get('content')

    db.session.commit()

    return jsonify({"msg": "Note updated"}), 200

# DELETE NOTE
@note_bp.route('/notes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_note(id):
    user_id = get_jwt_identity()

    note = Note.query.filter_by(id=id, user_id=user_id).first()

    if not note:
        return jsonify({"msg": "Note not found"}), 404

    db.session.delete(note)
    db.session.commit()

    return jsonify({"msg": "Note deleted"}), 200

# SEARCH NOTES
@note_bp.route('/search', methods=['GET'])
@jwt_required()
def search_notes():
    user_id = get_jwt_identity()
    query = request.args.get('q')

    notes = Note.query.filter(
        Note.user_id == user_id,
        Note.title.ilike(f"%{query}%")
    ).all()

    result = []
    for note in notes:
        result.append({
            "id": note.id,
            "title": note.title,
            "content": note.content
        })

    return jsonify(result), 200