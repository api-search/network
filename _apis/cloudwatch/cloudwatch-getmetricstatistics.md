---
aid: cloudwatch:cloudwatch-getmetricstatistics
name: Retrieve statistics for a specified metric
tags:
- Metrics
humanURL: 
properties: []
description: >-
  Gets statistics for the specified metric. The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. CloudWatch retains metric data as follows - data points with a period of less than 60 seconds are available for 3 hours, data points with a period of 60 seconds are available for 15 days, data points with a period of 300 seconds are available for 63 days, and data points with a period of 3600 seconds are avai...

---
