---
description: A <code>GetPredictiveScalingForecast</code> call returns the load forecast for a predictive scaling policy. This structure includes the data points for that load forecast, along with the timestamps of those data points and the metric specification.
layout: schema
name: LoadForecast
properties_list:
- description: ''
  name: Timestamps
  type: object
- description: ''
  name: Values
  type: object
- description: ''
  name: MetricSpecification
  type: object
provider_name: Amazon EC2 Auto Scaling
provider_slug: amazon-ec2-auto-scaling
schema_file: json-schema/ec2-auto-scaling-load-forecast-schema.json
slug: ec2-auto-scaling-load-forecast
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
title: LoadForecast
---
