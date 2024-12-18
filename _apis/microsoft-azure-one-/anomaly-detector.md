---
name: Anomaly Detector
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: https://example.com
properties:
  - url: https://example.com
    type: Documentation
  - url: properties/anomaly-detector-openapi-original.yml
    type: OpenAPI
description: >-
  The Anomaly Detector API detects anomalies automatically in time series data.

  It supports both a stateless detection mode and a

  stateful detection mode. In stateless mode, there are three functionalities.
  Entire

  Detect is for detecting the whole series, with the model trained by the time
  series.

  Last Detect is for detecting the last point, with the model trained by points
  before.

  ChangePoint Detect is for detecting trend changes in the time series. In
  stateful

  mode, the user can store time series. The stored time series will be used for

  detection anomalies. In this mode, the user can still use the preceding three

  functionalities by only giving a time range without preparing time series on
  the

  client side. Besides the preceding three functionalities, the stateful model

  provides group-based detection and labeling services. By using the labeling

  service, the user can provide labels for each detection result. These labels
  will be

  used for retuning or regenerating detection models. Inconsistency detection is

  a kind of group-based detection that finds inconsistencies in

  a set of time series. By using the anomaly detector service, business
  customers can

  discover incidents and establish a logic flow for root cause analysis.

---