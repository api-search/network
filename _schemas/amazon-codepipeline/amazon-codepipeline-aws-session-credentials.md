---
description: Represents an Amazon Web Services session credentials object. These credentials are temporary credentials that are issued by Amazon Web Services Secure Token Service (STS). They can be used to access input and output artifacts in the S3 bucket used to store artifact for the pipeline in CodePipeline.
layout: schema
name: AWSSessionCredentials
properties_list:
- description: ''
  name: accessKeyId
  type: object
- description: ''
  name: secretAccessKey
  type: object
- description: ''
  name: sessionToken
  type: object
provider_name: Amazon CodePipeline
provider_slug: amazon-codepipeline
schema_file: json-schema/amazon-codepipeline-aws-session-credentials-schema.json
slug: amazon-codepipeline-aws-session-credentials
tags:
- Amazon
- AWS
- CI/CD
- Continuous Delivery
- DevOps
- Pipeline
- Release Automation
title: AWSSessionCredentials
---
