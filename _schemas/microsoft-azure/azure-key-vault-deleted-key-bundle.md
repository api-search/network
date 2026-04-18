---
description: A deleted key bundle.
layout: schema
name: DeletedKeyBundle
properties_list:
- description: The URL of the recovery object.
  name: recoveryId
  type: string
- description: The time when the key is scheduled to be purged (Unix time).
  name: scheduledPurgeDate
  type: integer
- description: The time when the key was deleted (Unix time).
  name: deletedDate
  type: integer
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-deleted-key-bundle-schema.json
slug: azure-key-vault-deleted-key-bundle
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: DeletedKeyBundle
---
