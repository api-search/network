---
description: The certificate item containing certificate metadata.
layout: schema
name: CertificateItem
properties_list:
- description: Certificate identifier.
  name: id
  type: string
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
- description: Thumbprint of the certificate.
  name: x5t
  type: string
- description: The subject name of the certificate.
  name: subject
  type: string
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-certificate-item-schema.json
slug: azure-key-vault-data-plane-certificate-item
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: CertificateItem
---
