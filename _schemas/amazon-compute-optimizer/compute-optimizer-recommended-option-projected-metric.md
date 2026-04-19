---
description: <p>Describes a projected utilization metric of a recommendation option.</p> <note> <p>The <code>Cpu</code> and <code>Memory</code> metrics are the only projected utilization metrics returned when you run the <a>GetEC2RecommendationProjectedMetrics</a> action. Additionally, the <code>Memory</code> metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent">Enabling Memory Utilization with the CloudWatch Agent</a>.</p> </note>
layout: schema
name: RecommendedOptionProjectedMetric
properties_list:
- description: ''
  name: recommendedInstanceType
  type: object
- description: ''
  name: rank
  type: object
- description: ''
  name: projectedMetrics
  type: object
provider_name: Amazon Compute Optimizer
provider_slug: amazon-compute-optimizer
schema_file: json-schema/compute-optimizer-recommended-option-projected-metric-schema.json
slug: compute-optimizer-recommended-option-projected-metric
tags:
- AWS
- Cost Optimization
- FinOps
- Machine Learning
- Resource Recommendations
title: RecommendedOptionProjectedMetric
---
