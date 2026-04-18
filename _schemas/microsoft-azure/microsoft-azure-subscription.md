---
description: An Azure subscription is a logical container used to provision resources in Azure. It holds the details of all your resources like virtual machines (VMs), databases, and more. When you create an Azure resource, you choose the subscription to deploy it to.
layout: schema
name: Azure Subscription
properties_list:
- description: 'The fully qualified ID for the subscription. Format: /subscriptions/{subscriptionId}.'
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
- description: The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.
  name: state
  type: string
- description: The subscription policies.
  name: subscriptionPolicies
  type: object
- description: The authorization source of the request. Valid values are one or more combinations of Legacy, RoleBased, Bypassed, Direct, and Management.
  name: authorizationSource
  type: string
- description: The tags attached to the subscription.
  name: tags
  type: object
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/microsoft-azure-subscription-schema.json
slug: microsoft-azure-subscription
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Azure Subscription
---
