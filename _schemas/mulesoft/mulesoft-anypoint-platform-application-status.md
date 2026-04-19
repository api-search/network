---
description: Detailed deployment status of a CloudHub application
layout: schema
name: ApplicationStatus
properties_list:
- description: Application domain name
  name: domain
  type: string
- description: Overall application status
  name: status
  type: string
- description: Status of the most recent deployment update
  name: deploymentUpdateStatus
  type: string
- description: ''
  name: workers
  type: array
provider_name: MuleSoft
provider_slug: mulesoft
schema_file: json-schema/mulesoft-anypoint-platform-application-status-schema.json
slug: mulesoft-anypoint-platform-application-status
tags:
- API Gateway
- API Management
- Enterprise
- Integration
title: ApplicationStatus
---
