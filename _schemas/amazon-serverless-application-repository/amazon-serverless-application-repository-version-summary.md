---
description: Summary of details about an application version.
layout: schema
name: VersionSummary
properties_list:
- description: The application ARN.
  name: applicationId
  type: string
- description: The semantic version of the application.
  name: semanticVersion
  type: string
- description: The date and time when this version was created.
  name: creationTime
  type: string
- description: A link to a public repository for the source code.
  name: sourceCodeUrl
  type: string
provider_name: Amazon Serverless Application Repository
provider_slug: amazon-serverless-application-repository
schema_file: json-schema/amazon-serverless-application-repository-version-summary-schema.json
slug: amazon-serverless-application-repository-version-summary
tags:
- Application Repository
- AWS
- Lambda
- SAM
- Serverless
title: VersionSummary
---
