---
description: Request body for creating a function alias
layout: schema
name: CreateAliasRequest
properties_list:
- description: The name of the alias
  name: Name
  type: string
- description: The function version that the alias invokes
  name: FunctionVersion
  type: string
- description: Description of the alias
  name: Description
  type: string
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-create-alias-request-schema.json
slug: aws-lambda-create-alias-request
tags: []
title: CreateAliasRequest
---
