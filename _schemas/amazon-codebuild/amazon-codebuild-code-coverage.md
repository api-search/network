---
description: <p>Contains code coverage report information.</p> <p>Line coverage measures how many statements your tests cover. A statement is a single instruction, not including comments, conditionals, etc.</p> <p>Branch coverage determines if your tests cover every possible branch of a control structure, such as an <code>if</code> or <code>case</code> statement.</p>
layout: schema
name: CodeCoverage
properties_list:
- description: ''
  name: id
  type: object
- description: ''
  name: reportARN
  type: object
- description: ''
  name: filePath
  type: object
- description: ''
  name: lineCoveragePercentage
  type: object
- description: ''
  name: linesCovered
  type: object
- description: ''
  name: linesMissed
  type: object
- description: ''
  name: branchCoveragePercentage
  type: object
- description: ''
  name: branchesCovered
  type: object
- description: ''
  name: branchesMissed
  type: object
- description: ''
  name: expired
  type: object
provider_name: Amazon CodeBuild
provider_slug: amazon-codebuild
schema_file: json-schema/amazon-codebuild-code-coverage-schema.json
slug: amazon-codebuild-code-coverage
tags:
- Amazon
- AWS
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
title: CodeCoverage
---
