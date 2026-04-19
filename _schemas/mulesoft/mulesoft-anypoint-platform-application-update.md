---
description: Request body for updating an existing CloudHub application
layout: schema
name: ApplicationUpdate
properties_list:
- description: New Mule runtime version
  name: muleVersion
  type: object
- description: Updated application properties
  name: properties
  type: object
- description: Enable or disable automatic restart
  name: monitoringAutoRestart
  type: boolean
- description: Target CloudHub region
  name: region
  type: string
- description: Enable or disable static IPs
  name: staticIPsEnabled
  type: boolean
- description: Enable or disable next-generation logging
  name: loggingNgEnabled
  type: boolean
- description: Enable or disable persistent queues
  name: persistentQueues
  type: boolean
provider_name: MuleSoft
provider_slug: mulesoft
schema_file: json-schema/mulesoft-anypoint-platform-application-update-schema.json
slug: mulesoft-anypoint-platform-application-update
tags:
- API Gateway
- API Management
- Enterprise
- Integration
title: ApplicationUpdate
---
