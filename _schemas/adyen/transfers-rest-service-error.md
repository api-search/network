---
description: RestServiceError schema from Adyen API
layout: schema
name: RestServiceError
properties_list:
- description: A human-readable explanation specific to this occurrence of the problem.
  name: detail
  type: string
- description: A code that identifies the problem type.
  name: errorCode
  type: string
- description: A unique URI that identifies the specific occurrence of the problem.
  name: instance
  type: string
- description: Detailed explanation of each validation error, when applicable.
  name: invalidFields
  type: array
- description: A unique reference for the request, essentially the same as `pspReference`.
  name: requestId
  type: string
- description: JSON response payload.
  name: response
  type: object
- description: The HTTP status code.
  name: status
  type: integer
- description: A short, human-readable summary of the problem type.
  name: title
  type: string
- description: A URI that identifies the problem type, pointing to human-readable documentation on this problem type.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-rest-service-error-schema.json
slug: transfers-rest-service-error
tags:
- Payments
- Financial Services
- Fintech
title: RestServiceError
---
