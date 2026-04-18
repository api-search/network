---
description: A deleted secret bundle.
layout: schema
name: DeletedSecretBundle
properties_list:
- description: The URL of the recovery object.
  name: recoveryId
  type: string
- description: The time when the secret is scheduled to be purged.
  name: scheduledPurgeDate
  type: integer
- description: The time when the secret was deleted.
  name: deletedDate
  type: integer
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-deleted-secret-bundle-schema.json
slug: azure-key-vault-deleted-secret-bundle
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: DeletedSecretBundle
---
