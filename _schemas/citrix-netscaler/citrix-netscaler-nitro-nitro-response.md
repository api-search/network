---
description: Standard NITRO API success response.
layout: schema
name: NitroResponse
properties_list:
- description: Error code. 0 indicates success.
  name: errorcode
  type: integer
- description: Human-readable message describing the result.
  name: message
  type: string
- description: Severity level of the response.
  name: severity
  type: string
provider_name: Citrix NetScaler
provider_slug: citrix-netscaler
schema_file: json-schema/citrix-netscaler-nitro-nitro-response-schema.json
slug: citrix-netscaler-nitro-nitro-response
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
title: NitroResponse
---
