from flask import Flask
from RAG.api import bp
import os
app = Flask(__name__)

# Register blueprint
app.register_blueprint(bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)