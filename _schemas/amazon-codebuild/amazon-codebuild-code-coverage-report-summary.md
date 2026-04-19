---
description: <p>Contains a summary of a code coverage report.</p> <p>Line coverage measures how many statements your tests cover. A statement is a single instruction, not including comments, conditionals, etc.</p> <p>Branch coverage determines if your tests cover every possible branch of a control structure, such as an <code>if</code> or <code>case</code> statement.</p>
layout: schema
name: CodeCoverageReportSummary
properties_list:
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
provider_name: Amazon CodeBuild
provider_slug: amazon-codebuild
schema_file: json-schema/amazon-codebuild-code-coverage-report-summary-schema.json
slug: amazon-codebuild-code-coverage-report-summary
tags:
- Amazon
- AWS
- CI/CD
- Build
- Continuous Integration
- DevOps
- Testing
title: CodeCoverageReportSummary
---
