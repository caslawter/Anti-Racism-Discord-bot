import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

# from .model import is_racist
from transformers import pipeline

toxigen_hatebert = pipeline("text-classification", model="tomh/toxigen_hatebert", tokenizer="bert-base-uncased")

#returns true if it is racist, false if it is not
def is_racist(sentence):
    output = toxigen_hatebert(sentence)
    print(output)
    return output[0]['label'] == 'LABEL_1', output[0]['score']



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/check', methods=["POST"])
    def check():
        try:
            payload = request.get_json()
            sentence = payload['sentence']
            result = is_racist(sentence)
            return jsonify({"is_racist": result[0], "score" : result[1]})
        except Exception as e:
            return jsonify({"error": str(e)})

    return app