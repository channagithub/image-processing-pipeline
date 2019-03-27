# Image Processing Pipeline
---

## Objectives
1. Extract and format information from raw images.
2. Prepare data for ingestion by a machine learning model.
3. Create an easily reproduceable pipeline along with documenation.
4. Visualize geolocation data.

## Proposed Pipeline
Here is my proposed pipeline which has flask, kafka, spark, s3 and elasticsearch components. 

![](pipeline_architecture/initial_architecture.jpg)

  * Flask - for RESTful service to collect images from mobile application or any other equivalent source
  * Kafka - for event driven architecture (distributed)
  * Spark - distributed data processing modules (distributed)
  * S3 - for storing augmented images, used by data scientists to train CNN models
  * Elasticsearch - for storing extracted geo location (also distributed)

## Usage
run deploy.sh, like
./deploy.sh

## Test api
curl http://0.0.0.0:8000/is_alive

> expected response
> {
>   "ret_ack": "Channa works on granular data pipeline."
> }

curl -F "file=@imgs_de/alfalfa/17254133335_e3c5643574_z.jpg" http://0.0.0.0:8000/post_image

> expected response
> {
>   "ret_ack": "Success. Got your image. Thank you. <class 'PIL.JpegImagePlugin.JpegImageFile'>"
> }