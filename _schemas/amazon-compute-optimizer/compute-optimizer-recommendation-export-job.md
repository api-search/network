---
description: <p>Describes a recommendation export job.</p> <p>Use the <a>DescribeRecommendationExportJobs</a> action to view your recommendation export jobs.</p> <p>Use the <a>ExportAutoScalingGroupRecommendations</a> or <a>ExportEC2InstanceRecommendations</a> actions to request an export of your recommendations.</p>
layout: schema
name: RecommendationExportJob
properties_list:
- description: ''
  name: jobId
  type: object
- description: ''
  name: destination
  type: object
- description: ''
  name: resourceType
  type: object
- description: ''
  name: status
  type: object
- description: ''
  name: creationTimestamp
  type: object
- description: ''
  name: lastUpdatedTimestamp
  type: object
- description: ''
  name: failureReason
  type: object
provider_name: Amazon Compute Optimizer
provider_slug: amazon-compute-optimizer
schema_file: json-schema/compute-optimizer-recommendation-export-job-schema.json
slug: compute-optimizer-recommendation-export-job
tags:
- AWS
- Cost Optimization
- FinOps
- Machine Learning
- Resource Recommendations
title: RecommendationExportJob
---
