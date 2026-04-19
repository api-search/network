---
description: An AWS KMS key (formerly customer master key) used for cryptographic operations.
layout: schema
name: Key
properties_list:
- description: The globally unique identifier for the KMS key.
  name: KeyId
  type: string
- description: The Amazon Resource Name (ARN) of the KMS key.
  name: KeyArn
  type: string
- description: The current status of the KMS key.
  name: KeyState
  type: string
- description: The cryptographic operations for which the KMS key can be used.
  name: KeyUsage
  type: string
- description: Describes the type of key material in the KMS key.
  name: KeySpec
  type: string
- description: The description of the KMS key.
  name: Description
  type: string
- description: The date and time when the KMS key was created.
  name: CreationDate
  type: string
- description: The date and time after which KMS deletes this KMS key.
  name: DeletionDate
  type: string
- description: Specifies whether the KMS key is enabled.
  name: Enabled
  type: boolean
- description: Indicates whether the KMS key is a multi-Region key.
  name: MultiRegion
  type: boolean
provider_name: Amazon KMS
provider_slug: amazon-kms
schema_file: json-schema/amazon-kms-key-schema.json
slug: amazon-kms-key
tags:
- AWS
- Cryptography
- Data Protection
- Encryption
- Key Management
- Security
title: Key
---
