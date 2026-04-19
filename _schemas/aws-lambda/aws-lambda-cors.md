---
description: Cross-origin resource sharing (CORS) settings for a function URL
layout: schema
name: Cors
properties_list:
- description: Whether to allow cookies or other credentials
  name: AllowCredentials
  type: boolean
- description: The HTTP headers allowed in requests
  name: AllowHeaders
  type: array
- description: The HTTP methods allowed
  name: AllowMethods
  type: array
- description: The origins allowed to access the function URL
  name: AllowOrigins
  type: array
- description: The HTTP headers exposed in the response
  name: ExposeHeaders
  type: array
- description: Maximum time in seconds that a browser can cache results of a preflight request
  name: MaxAge
  type: integer
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-cors-schema.json
slug: aws-lambda-cors
tags: []
title: Cors
---
