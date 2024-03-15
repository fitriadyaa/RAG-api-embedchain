from flask import Flask, request, jsonify
import os
from embedchain.store.assistants import OpenAIAssistant

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

chatbot = OpenAIAssistant(
    model="gpt-3.5-turbo-0125",
    instructions="""
    You are Chatze, a chatbot designed to provide accurate information based on questions asked. 
    - If a user asks a question not covered by the provided data, respond with: 'Maaf, Chatze tidak mengetahui apa yang Anda maksud. Ada yang bisa chatbot bantu lagi?'
    - Ensure all responses are directly based on the provided data source to maintain accuracy.
    """,
)
chatbot.add("./data.json")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        response = chatbot.chat(query)
        return jsonify({"response": response})
    except Exception as e:
        app.logger.error(f"Error processing query: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
