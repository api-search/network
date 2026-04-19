---
description: Snowflake account object.
layout: schema
name: ManagedAccount
properties_list:
- description: Cloud in which the managed account is located. For reader accounts, this is always the same as the cloud for the provider account.
  name: cloud
  type: string
- description: Region in which the managed account is located. For reader accounts, this is always the same as the region for the provider account.
  name: region
  type: string
- description: Legacy identifier for the account.
  name: locator
  type: string
- description: Date and time the account was created.
  name: created_on
  type: string
- description: Account URL that is used to connect to the account, in the account name format. The account identifier in this format follows the pattern <orgname>-<account_name>.
  name: url
  type: string
- description: Account URL that is used to connect to the account, in the legacy account locator format.
  name: account_locator_url
  type: string
- description: Optional comment in which to store information related to the account.
  name: comment
  type: string
- description: Name of the account administrator.
  name: admin_name
  type: string
- description: Password for the account administrator.
  name: admin_password
  type: string
- description: Type of the account.
  name: account_type
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/managed-account-managed-account-schema.json
slug: managed-account-managed-account
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ManagedAccount
---
