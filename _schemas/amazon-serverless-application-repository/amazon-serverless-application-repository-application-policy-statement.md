---
description: Policy statement for an application.
layout: schema
name: ApplicationPolicyStatement
properties_list:
- description: A unique ID for the statement.
  name: statementId
  type: string
- description: An array of AWS account IDs or * for public access.
  name: principals
  type: array
- description: For each action, specify the permission to be granted.
  name: actions
  type: array
provider_name: Amazon Serverless Application Repository
provider_slug: amazon-serverless-application-repository
schema_file: json-schema/amazon-serverless-application-repository-application-policy-statement-schema.json
slug: amazon-serverless-application-repository-application-policy-statement
tags:
- Application Repository
- AWS
- Lambda
- SAM
- Serverless
title: ApplicationPolicyStatement
---
