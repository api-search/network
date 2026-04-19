---
description: Information about the results from running a series of test cases during the run of a build project. The test cases are specified in the buildspec for the build project using one or more paths to the test case files. You can specify any type of tests you want, such as unit tests, integration tests, and functional tests.
layout: schema
name: Report
properties_list:
- description: ''
  name: arn
  type: object
- description: ''
  name: type
  type: object
- description: ''
  name: name
  type: object
- description: ''
  name: reportGroupArn
  type: object
- description: ''
  name: executionId
  type: object
- description: ''
  name: status
  type: object
- description: ''
  name: created
  type: object
- description: ''
  name: expired
  type: object
- description: ''
  name: exportConfig
  type: object
- description: ''
  name: truncated
  type: object
- description: ''
  name: testSummary
  type: object
- description: ''
  name: codeCoverageSummary
  type: object
provider_name: Amazon CodeBuild
provider_slug: amazon-codebuild
schema_file: json-schema/amazon-codebuild-report-schema.json
slug: amazon-codebuild-report
tags:
- Amazon
- AWS
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
title: Report
---
