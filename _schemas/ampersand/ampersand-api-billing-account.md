---
description: BillingAccount schema from Ampersand API
layout: schema
name: BillingAccount
properties_list:
- description: The billing account ID.
  name: id
  type: string
- description: The display name of the billing account.
  name: displayName
  type: string
- description: The billing provider that this account is associated with.
  name: billingProvider
  type: string
- description: The ID used by the billing provider to identify the account.
  name: billingProviderRef
  type: string
- description: The time the billing account was created.
  name: createTime
  type: string
- description: The time the billing account was last updated.
  name: updateTime
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-billing-account-schema.json
slug: ampersand-api-billing-account
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: BillingAccount
---
