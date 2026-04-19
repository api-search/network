---
description: The estimated monthly savings after you adjust the configurations of your instances running on the inferred workload types to the recommended configurations. If the <code>inferredWorkloadTypes</code> list contains multiple entries, then the savings are the sum of the monthly savings from instances that run the exact combination of the inferred workload types.
layout: schema
name: InferredWorkloadSaving
properties_list:
- description: ''
  name: inferredWorkloadTypes
  type: object
- description: ''
  name: estimatedMonthlySavings
  type: object
provider_name: Amazon Compute Optimizer
provider_slug: amazon-compute-optimizer
schema_file: json-schema/compute-optimizer-inferred-workload-saving-schema.json
slug: compute-optimizer-inferred-workload-saving
tags:
- AWS
- Cost Optimization
- FinOps
- Machine Learning
- Resource Recommendations
title: InferredWorkloadSaving
---
