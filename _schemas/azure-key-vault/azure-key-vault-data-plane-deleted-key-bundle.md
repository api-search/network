---
description: A deleted key bundle consisting of a WebKey plus its attributes.
layout: schema
name: DeletedKeyBundle
properties_list:
- description: The url of the recovery object, used to identify and recover the deleted key.
  name: recoveryId
  type: string
- description: The time when the key is scheduled to be purged, in UTC.
  name: scheduledPurgeDate
  type: integer
- description: The time when the key was deleted, in UTC.
  name: deletedDate
  type: integer
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-deleted-key-bundle-schema.json
slug: azure-key-vault-data-plane-deleted-key-bundle
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: DeletedKeyBundle
---
