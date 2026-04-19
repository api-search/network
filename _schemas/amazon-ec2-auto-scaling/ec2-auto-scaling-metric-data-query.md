---
description: <p>The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.</p> <p>For more information and examples, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-customized-metric-specification.html">Advanced predictive scaling policy configurations using custom metrics</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>
layout: schema
name: MetricDataQuery
properties_list:
- description: ''
  name: Id
  type: object
- description: ''
  name: Expression
  type: object
- description: ''
  name: MetricStat
  type: object
- description: ''
  name: Label
  type: object
- description: ''
  name: ReturnData
  type: object
provider_name: Amazon EC2 Auto Scaling
provider_slug: amazon-ec2-auto-scaling
schema_file: json-schema/ec2-auto-scaling-metric-data-query-schema.json
slug: ec2-auto-scaling-metric-data-query
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
title: MetricDataQuery
---
