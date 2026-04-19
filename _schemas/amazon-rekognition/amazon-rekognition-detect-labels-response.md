---
description: Response from the DetectLabels operation.
layout: schema
name: DetectLabelsResponse
properties_list:
- description: An array of labels for the real-world objects detected.
  name: Labels
  type: array
- description: The value of OrientationCorrection is always null.
  name: OrientationCorrection
  type: string
- description: Version number of the label detection model used.
  name: LabelModelVersion
  type: string
- description: Information about the quality and dominant colors of an input image.
  name: ImageProperties
  type: object
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
schema_file: json-schema/amazon-rekognition-detect-labels-response-schema.json
slug: amazon-rekognition-detect-labels-response
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
