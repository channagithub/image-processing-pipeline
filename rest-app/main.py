#!flask/bin/python
import os
from flask import Flask
from flask import request
from flask import jsonify
from PIL import Image
from kafka import KafkaProducer, KafkaClient

#*****************************************************************
# init app
#*****************************************************************
app = Flask(__name__)

#*****************************************************************
# connect to kafka as a producer
#*****************************************************************

# will uncomment the following set of lines once I'm able to connect to kafka Q

# kafka_client = KafkaClient('localhost:9092')
# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092',
#     client_id='test-producer'
# )
# TOPIC = 'test-topic'

#*****************************************************************
# REST endpoints
#*****************************************************************
@app.route('/is_alive', methods=['GET'])
def index():
	return jsonify(ret_ack = "Channa works on granular data pipeline.")

@app.route('/post_image', methods=['POST'])
def _post_image():
	img = Image.open(request.files['file'])

	# # push it to kafka 
	# # kafka will publish this image
	# # all the subscribers get this image 
	# # in our setting, geo location extraction module and image data augmentation module

	# # I'm not able to connect to the kafka container as of now
	# # Will look into this issue at later point of time

	# try:
	# 	producer.send(TOPIC, value=dumps(a_obj).encode('utf-8'))
	# except UnicodeDecodeError:
	# 	pass
	return jsonify(ret_ack = "Success. Got your image. Thank you. " + str(type(img)))

if __name__ == "__main__":
	pass