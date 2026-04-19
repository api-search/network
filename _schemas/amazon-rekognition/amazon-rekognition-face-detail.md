---
description: Structure containing attributes of the face that the algorithm detected.
layout: schema
name: FaceDetail
properties_list:
- description: ''
  name: BoundingBox
  type: object
- description: The estimated age range in years for the face.
  name: AgeRange
  type: object
- description: ''
  name: Smile
  type: object
- description: ''
  name: Gender
  type: object
- description: ''
  name: Emotions
  type: array
- description: Confidence level that the bounding box contains a face.
  name: Confidence
  type: number
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
schema_file: json-schema/amazon-rekognition-face-detail-schema.json
slug: amazon-rekognition-face-detail
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
title: FaceDetail
---
