---
description: An on-premises data gateway
layout: schema
name: Gateway
properties_list:
- description: The unique identifier of the gateway
  name: id
  type: string
- description: The display name of the gateway
  name: name
  type: string
- description: The type of gateway
  name: type
  type: string
- description: The public key for encrypting credentials
  name: publicKey
  type: object
- description: Gateway metadata annotation
  name: gatewayAnnotation
  type: string
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-gateway-schema.json
slug: power-bi-rest-gateway
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Gateway
---
