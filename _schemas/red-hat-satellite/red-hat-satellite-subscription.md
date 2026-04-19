---
description: A Red Hat subscription providing product entitlements for an organization.
layout: schema
name: Subscription
properties_list:
- description: Unique identifier for the subscription.
  name: id
  type: integer
- description: Candlepin subscription identifier.
  name: cp_id
  type: string
- description: Subscription pool identifier.
  name: subscription_id
  type: integer
- description: Subscription name (product name).
  name: name
  type: string
- description: Subscription description.
  name: description
  type: '[''string'', ''null'']'
- description: Red Hat product identifier.
  name: product_id
  type: string
- description: Red Hat product name.
  name: product_name
  type: string
- description: Contract number associated with the subscription.
  name: contract_number
  type: '[''string'', ''null'']'
- description: Customer account number.
  name: account_number
  type: '[''string'', ''null'']'
- description: Total quantity of entitlements in the subscription.
  name: quantity
  type: integer
- description: Number of entitlements currently consumed.
  name: consumed
  type: integer
- description: Number of entitlements available for attachment.
  name: available
  type: integer
- description: Subscription start date.
  name: start_date
  type: string
- description: Subscription end date.
  name: end_date
  type: string
- description: Support level (e.g., Premium, Standard, Self-Support).
  name: support_level
  type: '[''string'', ''null'']'
- description: Subscription type.
  name: type
  type: string
- description: Whether this subscription is for virtual systems only.
  name: virt_only
  type: boolean
- description: Whether this subscription requires virt-who reporting.
  name: virt_who
  type: boolean
- description: Whether multiple entitlements can be attached to a single host.
  name: multi_entitlement
  type: boolean
- description: Stacking identifier for stackable subscriptions.
  name: stacking_id
  type: '[''string'', ''null'']'
- description: Pool identifier from the upstream subscription source.
  name: upstream_pool_id
  type: '[''string'', ''null'']'
- description: Organization this subscription belongs to.
  name: organization_id
  type: integer
- description: Products provided by this subscription.
  name: provided_products
  type: array
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-subscription-schema.json
slug: red-hat-satellite-subscription
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: Subscription
---
