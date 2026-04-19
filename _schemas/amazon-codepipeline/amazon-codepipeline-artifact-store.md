---
description: <p>The S3 bucket where artifacts for the pipeline are stored.</p> <note> <p>You must include either <code>artifactStore</code> or <code>artifactStores</code> in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use <code>artifactStores</code>.</p> </note>
layout: schema
name: ArtifactStore
properties_list:
- description: ''
  name: type
  type: object
- description: ''
  name: location
  type: object
- description: ''
  name: encryptionKey
  type: object
provider_name: Amazon CodePipeline
provider_slug: amazon-codepipeline
schema_file: json-schema/amazon-codepipeline-artifact-store-schema.json
slug: amazon-codepipeline-artifact-store
tags:
- Amazon
- AWS
- CI/CD
- Continuous Delivery
- DevOps
- Pipeline
- Release Automation
title: ArtifactStore
---
