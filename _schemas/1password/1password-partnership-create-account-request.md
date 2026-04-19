---
description: The request body for creating a new partner billing account.
layout: schema
name: CreateAccountRequest
properties_list:
- description: The unique identifier for the customer's billing account, supplied by the partner. Can be up to 200 characters with alphanumeric characters, hyphens, and periods.
  name: account_uid
  type: string
- description: The 1Password account type for the customer. Individual (I) or Family (F). Team and business accounts are not supported.
  name: account_type
  type: string
- description: The domain the customer can use for their new or existing 1Password account.
  name: domain
  type: string
- description: The optional date and time to remove the customer's account from the partner billing service. ISO 8601 format.
  name: ends_at
  type: string
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-partnership-create-account-request-schema.json
slug: 1password-partnership-create-account-request
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: CreateAccountRequest
---
