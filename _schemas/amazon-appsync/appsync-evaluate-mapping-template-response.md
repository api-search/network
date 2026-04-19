---
description: Response from evaluating a mapping template
layout: schema
name: EvaluateMappingTemplateResponse
properties_list:
- description: The evaluated template result
  name: evaluationResult
  type: string
- description: Error from template evaluation if any
  name: error
  type: object
- description: Evaluation log messages
  name: logs
  type: array
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-evaluate-mapping-template-response-schema.json
slug: appsync-evaluate-mapping-template-response
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: EvaluateMappingTemplateResponse
---
