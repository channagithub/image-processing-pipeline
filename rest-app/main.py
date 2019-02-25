#!flask/bin/python
import os
from flask import Flask
from flask import request
from flask import jsonify
from joblib import load

app = Flask(__name__)


global tfidf, model, id_to_class

tfidf = load('/usr/intermediate/tfidf.pkl') 
print("[DEBUG] loading tfidf done!", flush=True)
model = load('pkl_files/model.pkl') 
print("[DEBUG] loading model done!", flush=True)
id_to_class = load('pkl_files/id_to_class.pkl') 
print("[DEBUG] loading id_to_class done!", flush=True)

@app.route('/isAlive', methods=['GET'])
def index():
    return jsonify(return_value = "channa works on ML classification algorithm")

@app.route('/get_prediction', methods=['POST'])
def _get_prediction():

    filters = request.get_json()
    sentences_list = filters.get('sentences', dict())

    vectorized_input = tfidf.transform(sentences_list).toarray()
    predicted_values = [id_to_class[i] for i in model.predict(vectorized_input)]

    return jsonify(ret_pred_values = predicted_values)

if __name__ == "__main__":
    print("Loading!")
