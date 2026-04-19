---
description: Properties of a Power Platform environment.
layout: schema
name: EnvironmentProperties
properties_list:
- description: The Azure region where the environment is hosted.
  name: azureRegion
  type: string
- description: The display name of the environment.
  name: displayName
  type: string
- description: A text description of the environment purpose.
  name: description
  type: '[''string'', ''null'']'
- description: The timestamp when the environment was created.
  name: createdTime
  type: string
- description: The timestamp of the last modification to the environment.
  name: lastModifiedTime
  type: string
- description: The current provisioning state of the environment.
  name: provisioningState
  type: string
- description: How the environment was created.
  name: creationType
  type: string
- description: The SKU type of the environment.
  name: environmentSku
  type: string
- description: Whether this is the default environment for the tenant.
  name: isDefault
  type: boolean
- description: Capacity consumption details for the environment.
  name: capacity
  type: array
- description: Add-on allocations for the environment.
  name: addons
  type: array
- description: URLs for accessing the environment through different client interfaces.
  name: clientUris
  type: object
- description: Runtime service endpoints for the environment.
  name: runtimeEndpoints
  type: object
- description: The type of database provisioned for the environment.
  name: databaseType
  type: '[''string'', ''null'']'
- description: The data retention period in ISO 8601 duration format.
  name: retentionPeriod
  type: string
- description: Current states of the environment.
  name: states
  type: object
- description: The update cadence setting for the environment.
  name: updateCadence
  type: object
- description: Encryption key management information.
  name: protectionStatus
  type: object
provider_name: Microsoft Power Platform APIs
provider_slug: power-platform
schema_file: json-schema/power-platform-environment-properties-schema.json
slug: power-platform-environment-properties
tags:
- Business Applications
- Copilot Studio
- Dataverse
- Low-Code
- Microsoft
- No-Code
- Power Pages
- Power Platform
title: EnvironmentProperties
---
