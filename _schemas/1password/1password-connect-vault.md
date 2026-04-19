---
description: Represents a 1Password vault that contains items. Vaults are used to organize and control access to secrets.
layout: schema
name: Vault
properties_list:
- description: The unique identifier for the vault.
  name: id
  type: string
- description: The name of the vault.
  name: name
  type: string
- description: A description of the vault's purpose.
  name: description
  type: string
- description: The version of the vault attributes.
  name: attributeVersion
  type: integer
- description: The version of the vault contents.
  name: contentVersion
  type: integer
- description: The number of items in the vault.
  name: items
  type: integer
- description: The type of the vault.
  name: type
  type: string
- description: The date and time the vault was created.
  name: createdAt
  type: string
- description: The date and time the vault was last updated.
  name: updatedAt
  type: string
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-connect-vault-schema.json
slug: 1password-connect-vault
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: Vault
---
