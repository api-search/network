---
description: ''
layout: schema
name: DescribeAnomalyDetectorsInput
properties_list:
- description: Use the token returned by the previous operation to request the next page of results.
  name: NextToken
  type: string
- description: The maximum number of results to return in one operation.
  name: MaxResults
  type: integer
- description: Limits the results to only the anomaly detection models that are associated with the specified namespace.
  name: Namespace
  type: string
- description: Limits the results to only the anomaly detection models that are associated with the specified metric name.
  name: MetricName
  type: string
- description: Limits the results to only the anomaly detection models that are associated with the specified metric dimensions.
  name: Dimensions
  type: array
- description: The anomaly detector types to request when using DescribeAnomalyDetectors.
  name: AnomalyDetectorTypes
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-describe-anomaly-detectors-input-schema.json
slug: cloudwatch-describe-anomaly-detectors-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: DescribeAnomalyDetectorsInput
---
