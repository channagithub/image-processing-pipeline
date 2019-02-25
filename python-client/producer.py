""" Generate test data to send to Kafka """

import random
from time import sleep
from json import dumps

from kafka import KafkaProducer, KafkaClient

################################################################################
# Import test data
################################################################################

TEST_DATA = [
    {'id': 1, 'foo': 'bar'},
    {'id': 2, 'foo': 'baz'},
    {'id': 3, 'foo': 'bnat'}
]

################################################################################
# Set up producer
################################################################################
from kafka import KafkaProducer, KafkaClient

KAFKA = KafkaClient('localhost:9092')
# PRODUCER = KafkaProducer(bootstrap_servers='localhost:9092', 
#                             request_timeout_ms=1000000)
# ,                         api_version_auto_timeout_ms=1000000)
PRODUCER = KafkaProducer(
    bootstrap_servers='localhost:9092',
    client_id='test-producer'
)

TOPIC = 'test-topic'

################################################################################
# Loop, add to kafka
################################################################################

for rown, a_obj in enumerate(TEST_DATA):

    try:
        #avro_push(rec)
        PRODUCER.send(TOPIC, value=dumps(a_obj).encode('utf-8'))
    except UnicodeDecodeError:
        pass

    print('pushed: %s' % rown)

    # Send records at random intervals; adjust this to send more or less frequently
    sleep(random.uniform(0.01, 5))
