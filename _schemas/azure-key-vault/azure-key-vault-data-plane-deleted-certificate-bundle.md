---
description: A deleted certificate bundle consisting of its previous id, attributes, tags, and deletion information.
layout: schema
name: DeletedCertificateBundle
properties_list:
- description: The url of the recovery object, used to identify and recover the deleted certificate.
  name: recoveryId
  type: string
- description: The time when the certificate is scheduled to be purged, in UTC.
  name: scheduledPurgeDate
  type: integer
- description: The time when the certificate was deleted, in UTC.
  name: deletedDate
  type: integer
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-deleted-certificate-bundle-schema.json
slug: azure-key-vault-data-plane-deleted-certificate-bundle
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: DeletedCertificateBundle
---
