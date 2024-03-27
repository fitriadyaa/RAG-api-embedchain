from flask import Blueprint, request, jsonify
from embedchain import App
import os

bp = Blueprint("API", __name__)
embedchain_app = App()

# Kunci API disimpan di sini
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def error_response(message, status_code):
    return jsonify({"error": message}), status_code

@bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get("question", "")
    if not question:
        return error_response("No query provided", 400)
    try:
        response = embedchain_app.query(question)
        return jsonify({"response": response})
    except Exception as e:
        return error_response(f"Error processing query: {e}", 500)

@bp.route('/add_reference', methods=['POST'])
def add_reference():
    data = request.json
    reference_url = data.get('reference_url', '')

    if not reference_url:
        return error_response("No reference URL provided", 400)

    try:
        embedchain_app.add(reference_url)
        return jsonify({"message": "Reference added successfully"}), 200
    except Exception as e:
        return error_response(f"Error adding reference: {e}", 500)
