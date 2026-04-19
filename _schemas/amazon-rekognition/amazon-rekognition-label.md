---
description: Structure containing details about the detected label.
layout: schema
name: Label
properties_list:
- description: The name of the label detected in the image or video.
  name: Name
  type: string
- description: Level of confidence for the label.
  name: Confidence
  type: number
- description: Bounding boxes for each instance of the detected object.
  name: Instances
  type: array
- description: The parent labels for a label in the taxonomy hierarchy.
  name: Parents
  type: array
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
schema_file: json-schema/amazon-rekognition-label-schema.json
slug: amazon-rekognition-label
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
title: Label
---
