---
description: Configuration of a Lambda function alias
layout: schema
name: AliasConfiguration
properties_list:
- description: The ARN of the alias
  name: AliasArn
  type: string
- description: The name of the alias
  name: Name
  type: string
- description: The function version that the alias invokes
  name: FunctionVersion
  type: string
- description: Description of the alias
  name: Description
  type: string
- description: A unique identifier that changes when you update the alias
  name: RevisionId
  type: string
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-alias-configuration-schema.json
slug: aws-lambda-alias-configuration
tags: []
title: AliasConfiguration
---
