---
description: Management policy for a certificate.
layout: schema
name: CertificatePolicy
properties_list:
- description: The certificate id.
  name: id
  type: string
- description: Actions that will be performed by Key Vault over the lifetime of a certificate.
  name: lifetime_actions
  type: array
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-certificate-policy-schema.json
slug: azure-key-vault-data-plane-certificate-policy
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: CertificatePolicy
---
