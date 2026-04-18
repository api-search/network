---
description: NITRO API error response with details about the failure.
layout: schema
name: NitroErrorResponse
properties_list:
- description: Numeric error code identifying the specific error.
  name: errorcode
  type: integer
- description: Human-readable error message.
  name: message
  type: string
- description: Severity level of the error.
  name: severity
  type: string
provider_name: Citrix NetScaler
provider_slug: citrix-netscaler
schema_file: json-schema/citrix-netscaler-nitro-nitro-error-response-schema.json
slug: citrix-netscaler-nitro-nitro-error-response
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
title: NitroErrorResponse
---
