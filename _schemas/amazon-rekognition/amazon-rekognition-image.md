---
description: Provides the input image either as bytes or an S3 object.
layout: schema
name: Image
properties_list:
- description: Blob of image bytes up to 5 MBs.
  name: Bytes
  type: string
- description: ''
  name: S3Object
  type: object
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
schema_file: json-schema/amazon-rekognition-image-schema.json
slug: amazon-rekognition-image
tags:
- AWS
- Celebrity Recognition
- Computer Vision
- Content Moderation
- Custom Labels
- Deep Learning
- Face Liveness
- Facial Recognition
- Image Analysis
- Machine Learning
- Object Detection
- Text Detection
- Video Analysis
title: Image
---
