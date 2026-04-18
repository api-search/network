---
description: ''
layout: schema
name: BlpapiRequest
properties_list:
- description: BLPAPI service URI (e.g., //blp/refdata)
  name: serviceUri
  type: string
- description: Name of the BLPAPI operation
  name: operationName
  type: string
- description: The operation-specific request payload
  name: requestObject
  type: object
provider_name: Bloomberg AIM
provider_slug: bloomberg-aim
schema_file: json-schema/bloomberg-http-blpapi-request-schema.json
slug: bloomberg-http-blpapi-request
tags:
- Financial Data
- Market Data
- Order Management
- Portfolio Management
- Trading
title: BlpapiRequest
---
