---
description: The certificate management attributes.
layout: schema
name: CertificateAttributes
properties_list:
- description: Determines whether the object is enabled.
  name: enabled
  type: boolean
- description: Not before date in UTC.
  name: nbf
  type: integer
- description: Expiry date in UTC.
  name: exp
  type: integer
- description: Creation time in UTC.
  name: created
  type: integer
- description: Last updated time in UTC.
  name: updated
  type: integer
- description: softDelete data retention days. Value should be >=7 and <=90 when softDelete enabled, otherwise 0.
  name: recoverableDays
  type: integer
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-certificate-attributes-schema.json
slug: azure-key-vault-data-plane-certificate-attributes
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: CertificateAttributes
---
