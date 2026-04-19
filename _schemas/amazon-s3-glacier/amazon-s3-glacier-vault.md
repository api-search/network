---
description: Schema representing an Amazon S3 Glacier vault resource. A vault is a container for storing archives in Amazon S3 Glacier, providing durable and low-cost storage for data archiving and long-term backup.
layout: schema
name: Amazon S3 Glacier Vault
properties_list:
- description: The Amazon Resource Name (ARN) of the vault.
  name: VaultARN
  type: string
- description: The name of the vault.
  name: VaultName
  type: string
- description: The Universal Coordinated Time (UTC) date when the vault was created.
  name: CreationDate
  type: string
- description: The Universal Coordinated Time (UTC) date when Amazon S3 Glacier completed the last vault inventory.
  name: LastInventoryDate
  type: string
- description: The number of archives in the vault as of the last inventory date.
  name: NumberOfArchives
  type: integer
- description: Total size, in bytes, of the archives in the vault as of the last inventory date.
  name: SizeInBytes
  type: integer
- description: ''
  name: VaultAccessPolicy
  type: object
- description: ''
  name: VaultNotificationConfig
  type: object
- description: The tags that are assigned to the vault.
  name: Tags
  type: object
provider_name: Amazon S3 Glacier
provider_slug: amazon-s3-glacier
schema_file: json-schema/amazon-s3-glacier-vault-schema.json
slug: amazon-s3-glacier-vault
tags:
- Archive
- AWS
- Backup
- Storage
title: Amazon S3 Glacier Vault
---
