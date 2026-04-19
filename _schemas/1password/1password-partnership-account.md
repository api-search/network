---
description: Represents a partner billing account for a 1Password customer.
layout: schema
name: Account
properties_list:
- description: The unique identifier for the customer's billing account.
  name: account_uid
  type: string
- description: The 1Password account type. I for individual, F for family.
  name: account_type
  type: string
- description: The domain associated with the customer's 1Password account.
  name: domain
  type: string
- description: The current status of the partner billing account.
  name: status
  type: string
- description: The unique activation token used to link the customer's 1Password account with their partner billing account. Append this to a 1Password partnership redemption link.
  name: activation_token
  type: string
- description: The date and time the customer's account is scheduled to be removed from the partner billing service.
  name: ends_at
  type: string
- description: The date and time the billing account was created.
  name: created_at
  type: string
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-partnership-account-schema.json
slug: 1password-partnership-account
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: Account
---
