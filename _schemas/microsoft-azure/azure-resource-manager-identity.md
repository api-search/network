---
description: Identity for the resource.
layout: schema
name: Identity
properties_list:
- description: The principal ID of resource identity.
  name: principalId
  type: string
- description: The tenant ID of resource.
  name: tenantId
  type: string
- description: The identity type.
  name: type
  type: string
- description: The list of user-assigned identities.
  name: userAssignedIdentities
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-resource-manager-identity-schema.json
slug: azure-resource-manager-identity
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Identity
---
