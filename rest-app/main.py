#!flask/bin/python
import os
from flask import Flask
from flask import request
from flask import jsonify
from PIL import Image

app = Flask(__name__)

@app.route('/is_alive', methods=['GET'])
def index():
	return jsonify(ret_ack = "Channa works on granular data pipeline.")

@app.route('/post_image', methods=['POST'])
def _post_image():
	img = Image.open(request.files['file'])
	return jsonify(ret_ack = "Success. Got your image. Thank you. " + str(type(img)))

if __name__ == "__main__":
	pass