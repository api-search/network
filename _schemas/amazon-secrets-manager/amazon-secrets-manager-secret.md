---
description: Secret schema from Amazon Secrets Manager API
layout: schema
name: Secret
properties_list:
- description: The ARN of the secret.
  name: ARN
  type: string
- description: The friendly name of the secret.
  name: Name
  type: string
- description: The description of the secret.
  name: Description
  type: string
- description: The ARN of the KMS key used to encrypt the secret.
  name: KmsKeyId
  type: string
- description: Whether rotation is enabled for this secret.
  name: RotationEnabled
  type: boolean
- description: The ARN of the Lambda function that rotates the secret.
  name: RotationLambdaARN
  type: string
- description: ''
  name: RotationRules
  type: object
- description: The most recent date and time that rotation was triggered.
  name: LastRotatedDate
  type: string
- description: The last date and time that this secret was modified.
  name: LastChangedDate
  type: string
- description: The last date that this secret was accessed.
  name: LastAccessedDate
  type: string
- description: The date and time the deletion of the secret occurred.
  name: DeletedDate
  type: string
- description: The list of tags attached to the secret.
  name: Tags
  type: array
- description: A list of the versions of the secret that have staging labels attached.
  name: SecretVersionsToStages
  type: object
- description: The name of the service that created this secret.
  name: OwningService
  type: string
- description: The date and time when the secret was created.
  name: CreatedDate
  type: string
- description: The Region the secret is in.
  name: PrimaryRegion
  type: string
provider_name: Amazon Secrets Manager
provider_slug: amazon-secrets-manager
schema_file: json-schema/amazon-secrets-manager-secret-schema.json
slug: amazon-secrets-manager-secret
tags:
- AWS
- Configuration
- Credentials
- Rotation
- Secrets
- Security
title: Secret
---
