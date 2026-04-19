---
description: The prediction results from a call to <a>DetectAnomalies</a>. <code>DetectAnomalyResult</code> includes classification information for the prediction (<code>IsAnomalous</code> and <code>Confidence</code>). If the model you use is an image segementation model, <code>DetectAnomalyResult</code> also includes segmentation information (<code>Anomalies</code> and <code>AnomalyMask</code>). Classification information is calculated separately from segmentation information and you shouldn't assume a relationship between them.
layout: schema
name: DetectAnomalyResult
properties_list:
- description: ''
  name: Source
  type: object
- description: ''
  name: IsAnomalous
  type: object
- description: ''
  name: Confidence
  type: object
- description: ''
  name: Anomalies
  type: object
- description: ''
  name: AnomalyMask
  type: object
provider_name: Amazon Lookout for Vision
provider_slug: amazon-lookout-for-vision
schema_file: json-schema/amazon-lookout-for-vision-detect-anomaly-result-schema.json
slug: amazon-lookout-for-vision-detect-anomaly-result
tags:
- AWS
- Computer Vision
- Machine Learning
- Manufacturing
- Quality Inspection
- Anomaly Detection
title: DetectAnomalyResult
---
