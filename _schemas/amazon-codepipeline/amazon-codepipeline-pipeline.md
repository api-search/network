---
description: Pipeline schema from Amazon CodePipeline
layout: schema
name: Pipeline
properties_list:
- description: The name of the pipeline.
  name: name
  type: string
- description: The ARN of the IAM role used by the pipeline.
  name: roleArn
  type: string
- description: ''
  name: stages
  type: array
- description: The version number of the pipeline.
  name: version
  type: integer
provider_name: Amazon CodePipeline
provider_slug: amazon-codepipeline
schema_file: json-schema/amazon-codepipeline-pipeline-schema.json
slug: amazon-codepipeline-pipeline
tags:
- Amazon
- AWS
- CI/CD
- Continuous Delivery
- DevOps
- Pipeline
- Release Automation
title: Pipeline
---
