---
description: Request body for creating a new CloudHub application
layout: schema
name: ApplicationCreate
properties_list:
- description: Unique domain name for the application
  name: domain
  type: string
- description: Target Mule runtime version
  name: muleVersion
  type: object
- description: CloudHub region to deploy to
  name: region
  type: string
- description: Application properties
  name: properties
  type: object
- description: Enable automatic restart on failure
  name: monitoringAutoRestart
  type: boolean
- description: Enable persistent queues
  name: persistentQueues
  type: boolean
- description: Enable static IP allocation
  name: staticIPsEnabled
  type: boolean
- description: Enable next-generation logging
  name: loggingNgEnabled
  type: boolean
provider_name: MuleSoft
provider_slug: mulesoft
schema_file: json-schema/mulesoft-anypoint-platform-application-create-schema.json
slug: mulesoft-anypoint-platform-application-create
tags:
- API Gateway
- API Management
- Enterprise
- Integration
title: ApplicationCreate
---
