---
description: ''
layout: schema
name: ErrorDetail
properties_list:
- description: A unique identifier for this error occurrence
  name: id
  type: string
- description: The HTTP status code for this error
  name: status
  type: string
- description: A machine-readable error code
  name: code
  type: string
- description: A short summary of the error
  name: title
  type: string
- description: A detailed explanation of the error
  name: detail
  type: string
- description: ''
  name: source
  type: object
provider_name: Apple
provider_slug: apple
schema_file: json-schema/app-store-connect-error-detail-schema.json
slug: app-store-connect-error-detail
tags:
- Developer
- iOS
- macOS
- Mobile
- Technology
title: ErrorDetail
---
