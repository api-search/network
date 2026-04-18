---
description: Subscription information.
layout: schema
name: Subscription
properties_list:
- description: The fully qualified ID for the subscription.
  name: id
  type: string
- description: The subscription ID.
  name: subscriptionId
  type: string
- description: The subscription display name.
  name: displayName
  type: string
- description: The subscription tenant ID.
  name: tenantId
  type: string
- description: The subscription state.
  name: state
  type: string
- description: The authorization source of the request. Valid values are one or more combinations of Legacy, RoleBased, Bypassed, Direct, Management.
  name: authorizationSource
  type: string
- description: The tags attached to the subscription.
  name: tags
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-resource-manager-subscription-schema.json
slug: azure-resource-manager-subscription
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Subscription
---
