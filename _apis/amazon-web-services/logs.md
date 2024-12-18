---
aid: amazon-web-services:logs
name: Amazon CloudWatch Logs
tags:
  - Anomaly
  - Detectors
  - Logs
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://example.com
humanURL: >-
  https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html
overlays:
  - url: overlays/logs-openapi-search.yml
    type: APIs.io Search
  - url: overlays/logs-openapi-api-evangelist-ratings.yml
    type: API Evangelist Ratings
properties:
  - url: >-
      https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html
    type: Documentation
  - url: properties/logs-openapi-original.yml
    type: OpenAPI
description: >-
  This API allows you to monitor, store, and access log files from EC2
  instances, CloudTrail, and other sources using Amazon CloudWatch Logs. You can
  retrieve log data through the CloudWatch console, AWS CLI, API, or SDK. 

---