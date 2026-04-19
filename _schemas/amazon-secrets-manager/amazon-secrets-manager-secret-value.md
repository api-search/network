---
description: SecretValue schema from Amazon Secrets Manager API
layout: schema
name: SecretValue
properties_list:
- description: The ARN of the secret.
  name: ARN
  type: string
- description: The friendly name of the secret.
  name: Name
  type: string
- description: The unique identifier of this version of the secret.
  name: VersionId
  type: string
- description: The decrypted secret value in binary format.
  name: SecretBinary
  type: string
- description: The decrypted secret value in string format.
  name: SecretString
  type: string
- description: A list of the staging labels that are attached to this version.
  name: VersionStages
  type: array
- description: The date and time that this version of the secret was created.
  name: CreatedDate
  type: string
provider_name: Amazon Secrets Manager
provider_slug: amazon-secrets-manager
schema_file: json-schema/amazon-secrets-manager-secret-value-schema.json
slug: amazon-secrets-manager-secret-value
tags:
- AWS
- Configuration
- Credentials
- Rotation
- Secrets
- Security
title: SecretValue
---
