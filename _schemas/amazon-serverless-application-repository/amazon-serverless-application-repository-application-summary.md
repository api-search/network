---
description: Summary of details about the application.
layout: schema
name: ApplicationSummary
properties_list:
- description: The application ARN.
  name: applicationId
  type: string
- description: The name of the application.
  name: name
  type: string
- description: The name of the author.
  name: author
  type: string
- description: The description of the application.
  name: description
  type: string
- description: The date and time when created.
  name: creationTime
  type: string
- description: Labels for discovery.
  name: labels
  type: array
provider_name: Amazon Serverless Application Repository
provider_slug: amazon-serverless-application-repository
schema_file: json-schema/amazon-serverless-application-repository-application-summary-schema.json
slug: amazon-serverless-application-repository-application-summary
tags:
- Application Repository
- AWS
- Lambda
- SAM
- Serverless
title: ApplicationSummary
---
