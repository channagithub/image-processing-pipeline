""" Generate test data to send to Kafka """

import random
import os
import numpy as np
import pickle
from time import sleep
from json import dumps
from kafka import KafkaProducer, KafkaClient

################################################################################
# Import data
################################################################################

def get_all_images_from_zip(images_path = '../rest-app/image_data/imgs_de/'):

    # get all categories (all folders)
    image_categories = [a_dir for a_dir in os.listdir(images_path) if not a_dir.startswith('.')]
    image_list = []

    # iterating all categories
    for an_img_cat in image_categories:
        image_cat_path = images_path + an_img_cat + '/'

        # iterating each image
        for an_img in os.listdir(image_cat_path):

            # appending each image
            image_list.append(image_cat_path + an_img)
    return image_list


################################################################################
# Loop, add to kafka (standard text)
################################################################################

# TOPIC = 'test-topic'

# TEST_DATA = [
#     {'id': 1, 'foo': 'bar'},
#     {'id': 2, 'foo': 'baz'},
#     {'id': 3, 'foo': 'bnat'}
# ]

# PRODUCER = KafkaProducer(
#     bootstrap_servers='localhost:9092',
#     client_id='test-producer'
# )

# for rown, a_obj in enumerate(TEST_DATA):

#     try:
#         #avro_push(rec)
#         PRODUCER.send(TOPIC, value=dumps(a_obj).encode('utf-8'))
#     except UnicodeDecodeError:
#         pass

#     print('pushed: %s' % rown)

#     # Send records at random intervals; adjust this to send more or less frequently
#     sleep(random.uniform(0.01, 5))



################################################################################
# Loop, add to kafka (images)
################################################################################

TOPIC = 'test-topic'
image_list = get_all_images_from_zip()
for i, an_img in enumerate(image_list):
    PRODUCER = KafkaProducer(value_serializer=lambda m: pickle.dumps(image_list[0].encode('ascii', 'ignore')), 
                                    bootstrap_servers=['localhost:9092'])

    PRODUCER.send(TOPIC, np.zeros((2,2)))
    print(i, ' image pushed')
