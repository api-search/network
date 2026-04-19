---
description: 'Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip'
layout: schema
name: Artifact
properties_list:
- description: ''
  name: name
  type: object
- description: ''
  name: revision
  type: object
- description: ''
  name: location
  type: object
provider_name: Amazon CodePipeline
provider_slug: amazon-codepipeline
schema_file: json-schema/amazon-codepipeline-artifact-schema.json
slug: amazon-codepipeline-artifact
tags:
- Amazon
- AWS
- CI/CD
- Continuous Delivery
- DevOps
- Pipeline
- Release Automation
title: Artifact
---
