---
description: Standard error response from the iControl REST API.
layout: schema
name: ErrorResponse
properties_list:
- description: HTTP status code.
  name: code
  type: integer
- description: Error message describing what went wrong.
  name: message
  type: string
- description: Stack trace for debugging (when available).
  name: errorStack
  type: array
- description: API-specific error code.
  name: apiError
  type: integer
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-error-response-schema.json
slug: bigip-icontrol-rest-error-response
tags:
- API Gateway
- Application Delivery
- Automation
- Edge Computing
- Kubernetes
- Load Balancing
- Multi-Cloud
- NGINX
- Security
- WAF
title: ErrorResponse
---
