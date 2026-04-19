---
description: <p>The metric policy that is associated with the container. A metric policy allows AWS Elemental MediaStore to send metrics to Amazon CloudWatch. In the policy, you must indicate whether you want MediaStore to send container-level metrics. You can also include rules to define groups of objects that you want MediaStore to send object-level metrics for.</p> <p>To view examples of how to construct a metric policy for your use case, see <a href="https://docs.aws.amazon.com/mediastore/latest/ug/policies-metric-examples.html">Example Metric Policies</a>.</p>
layout: schema
name: MetricPolicy
properties_list:
- description: ''
  name: ContainerLevelMetrics
  type: object
- description: ''
  name: MetricPolicyRules
  type: object
provider_name: Amazon MediaStore
provider_slug: amazon-mediastore
schema_file: json-schema/mediastore-api-metric-policy-schema.json
slug: mediastore-api-metric-policy
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: MetricPolicy
---
