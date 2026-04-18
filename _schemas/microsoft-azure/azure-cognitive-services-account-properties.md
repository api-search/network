---
description: Properties of Cognitive Services account.
layout: schema
name: AccountProperties
properties_list:
- description: The status of the cognitive services account at the time of the operation.
  name: provisioningState
  type: string
- description: Endpoint of the created account.
  name: endpoint
  type: string
- description: Dictionary of endpoints for the cognitive services account.
  name: endpoints
  type: object
- description: The capabilities of the cognitive services account.
  name: capabilities
  type: array
- description: Whether this account has been migrated.
  name: isMigrated
  type: boolean
- description: The date of creation.
  name: dateCreated
  type: string
- description: Optional subdomain name used for token-based authentication.
  name: customSubDomainName
  type: string
- description: Whether or not public endpoint access is allowed.
  name: publicNetworkAccess
  type: string
- description: Whether to disable local authentication methods.
  name: disableLocalAuth
  type: boolean
- description: Whether to restrict outbound network access.
  name: restrictOutboundNetworkAccess
  type: boolean
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-cognitive-services-account-properties-schema.json
slug: azure-cognitive-services-account-properties
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: AccountProperties
---
