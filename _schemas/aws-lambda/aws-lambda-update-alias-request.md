---
description: Request body for updating a function alias
layout: schema
name: UpdateAliasRequest
properties_list:
- description: The function version that the alias invokes
  name: FunctionVersion
  type: string
- description: Description of the alias
  name: Description
  type: string
- description: Update only if the revision ID matches
  name: RevisionId
  type: string
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-update-alias-request-schema.json
slug: aws-lambda-update-alias-request
tags: []
title: UpdateAliasRequest
---
