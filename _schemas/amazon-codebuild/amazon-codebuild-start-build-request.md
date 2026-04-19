---
description: StartBuildRequest schema from Amazon CodeBuild
layout: schema
name: StartBuildRequest
properties_list:
- description: The name of the CodeBuild build project.
  name: projectName
  type: string
- description: The version of the build input to be built.
  name: sourceVersion
  type: string
- description: ''
  name: environmentVariablesOverride
  type: array
provider_name: Amazon CodeBuild
provider_slug: amazon-codebuild
schema_file: json-schema/amazon-codebuild-start-build-request-schema.json
slug: amazon-codebuild-start-build-request
tags:
- Amazon
- AWS
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
title: StartBuildRequest
---
