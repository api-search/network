---
description: Response object from the Amazon Rekognition DetectLabels operation containing detected labels with confidence scores and bounding box information.
layout: schema
name: DetectLabelsResponse
properties_list:
- description: An array of labels for the real-world objects detected in the image.
  name: Labels
  type: array
- description: Version number of the label detection model that was used to detect labels.
  name: LabelModelVersion
  type: string
- description: Information about the properties of the input image.
  name: ImageProperties
  type: object
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
schema_file: json-schema/amazon-rekognition-detectlabelsresponse-schema.json
slug: amazon-rekognition-detectlabelsresponse
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
title: DetectLabelsResponse
---
