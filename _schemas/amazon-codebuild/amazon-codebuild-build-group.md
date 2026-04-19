---
description: Contains information about a batch build build group. Build groups are used to combine builds that can run in parallel, while still being able to set dependencies on other build groups.
layout: schema
name: BuildGroup
properties_list:
- description: ''
  name: identifier
  type: object
- description: ''
  name: dependsOn
  type: object
- description: ''
  name: ignoreFailure
  type: object
- description: ''
  name: currentBuildSummary
  type: object
- description: ''
  name: priorBuildSummaryList
  type: object
provider_name: Amazon CodeBuild
provider_slug: amazon-codebuild
schema_file: json-schema/amazon-codebuild-build-group-schema.json
slug: amazon-codebuild-build-group
tags:
- Amazon
- AWS
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
title: BuildGroup
---
