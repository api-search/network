---
description: Metadata about the linked Dataverse instance.
layout: schema
name: LinkedEnvironmentMetadata
properties_list:
- description: The resource identifier of the Dataverse instance.
  name: resourceId
  type: string
- description: The friendly name of the Dataverse instance.
  name: friendlyName
  type: string
- description: The unique name identifier for the Dataverse organization.
  name: uniqueName
  type: string
- description: The domain name prefix for the Dataverse instance.
  name: domainName
  type: string
- description: The Dataverse platform version.
  name: version
  type: string
- description: The URL of the Dataverse instance.
  name: instanceUrl
  type: string
- description: The API URL for the Dataverse instance.
  name: instanceApiUrl
  type: string
- description: The LCID of the base language for the Dataverse instance.
  name: baseLanguage
  type: integer
- description: The state of the Dataverse instance.
  name: instanceState
  type: string
- description: The timestamp when the Dataverse instance was created.
  name: createdTime
  type: string
- description: Whether background operations are enabled.
  name: backgroundOperationsState
  type: string
- description: The scale group identifier.
  name: scaleGroup
  type: string
- description: The platform SKU of the Dataverse instance.
  name: platformSku
  type: string
provider_name: Microsoft Power Platform APIs
provider_slug: power-platform
schema_file: json-schema/power-platform-linked-environment-metadata-schema.json
slug: power-platform-linked-environment-metadata
tags:
- Business Applications
- Copilot Studio
- Dataverse
- Low-Code
- Microsoft
- No-Code
- Power Pages
- Power Platform
title: LinkedEnvironmentMetadata
---
