---
description: Request for the DetectLabels operation.
layout: schema
name: DetectLabelsRequest
properties_list:
- description: ''
  name: Image
  type: object
- description: Maximum number of labels to return.
  name: MaxLabels
  type: integer
- description: Minimum confidence level for labels to return.
  name: MinConfidence
  type: number
- description: A list of the types of analysis to perform.
  name: Features
  type: array
- description: Optional settings for label detection.
  name: Settings
  type: object
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
schema_file: json-schema/amazon-rekognition-detect-labels-request-schema.json
slug: amazon-rekognition-detect-labels-request
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
title: DetectLabelsRequest
---
