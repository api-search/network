---
description: BillingEntity schema from Adyen API
layout: schema
name: BillingEntity
properties_list:
- description: The address details of the billing entity.
  name: address
  type: object
- description: The email address of the billing entity.
  name: email
  type: string
- description: The unique identifier of the billing entity, for use as `billingEntityId` when creating an order.
  name: id
  type: string
- description: The unique name of the billing entity.
  name: name
  type: string
- description: The tax number of the billing entity.
  name: taxId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-billing-entity-schema.json
slug: management-billing-entity
tags:
- Payments
- Financial Services
- Fintech
title: BillingEntity
---
