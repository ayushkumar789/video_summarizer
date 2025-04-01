from flask import Flask
from dotenv import load_dotenv
from routes.api import api
import os

app = Flask(__name__)
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
