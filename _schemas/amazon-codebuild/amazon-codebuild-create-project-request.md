---
description: CreateProjectRequest schema from Amazon CodeBuild
layout: schema
name: CreateProjectRequest
properties_list:
- description: The name of the build project.
  name: name
  type: string
- description: A description of the build project.
  name: description
  type: string
- description: ''
  name: source
  type: object
- description: ''
  name: environment
  type: object
- description: The ARN of the IAM role for CodeBuild.
  name: serviceRole
  type: string
- description: Build timeout in minutes.
  name: timeoutInMinutes
  type: integer
provider_name: Amazon CodeBuild
provider_slug: amazon-codebuild
schema_file: json-schema/amazon-codebuild-create-project-request-schema.json
slug: amazon-codebuild-create-project-request
tags:
- Amazon
- AWS
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
title: CreateProjectRequest
---
