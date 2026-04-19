---
description: ''
layout: schema
name: ServiceEndpoint
properties_list:
- description: User-friendly endpoint name that represents the corresponding port.
  name: name
  type: string
- description: The network port the service is listening on. NULL, when portRange is specified.
  name: port
  type: integer
- description: The network port range the service is listening on. NULL, when port is specified.
  name: portRange
  type: string
- description: Supported network protocol (TCP, HTTP, or HTTPS).
  name: protocol
  type: string
- description: True, if the endpoint is public, accessible from internet.
  name: is_public
  type: boolean
- description: Endpoint URL accessible from the internet.
  name: ingress_url
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/service-service-endpoint-schema.json
slug: service-service-endpoint
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ServiceEndpoint
---
