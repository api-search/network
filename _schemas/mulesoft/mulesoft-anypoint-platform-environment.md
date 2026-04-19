---
description: A deployment environment within an organization. Environments provide isolated contexts for deploying Mule applications, with types including Design, Sandbox, and Production.
layout: schema
name: Environment
properties_list:
- description: Unique identifier of the environment
  name: id
  type: string
- description: Display name of the environment
  name: name
  type: string
- description: ID of the organization this environment belongs to
  name: organizationId
  type: string
- description: Whether this is a production environment
  name: isProduction
  type: boolean
- description: The environment type classification
  name: type
  type: string
- description: Client ID associated with this environment
  name: clientId
  type: string
- description: Timestamp when the environment was created
  name: createdAt
  type: string
- description: Timestamp when the environment was last updated
  name: updatedAt
  type: string
provider_name: MuleSoft
provider_slug: mulesoft
schema_file: json-schema/mulesoft-anypoint-platform-environment-schema.json
slug: mulesoft-anypoint-platform-environment
tags:
- API Gateway
- API Management
- Enterprise
- Integration
title: Environment
---
