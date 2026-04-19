---
description: A certificate bundle consists of a certificate (X509) plus its attributes.
layout: schema
name: CertificateBundle
properties_list:
- description: The certificate id.
  name: id
  type: string
- description: The key id.
  name: kid
  type: string
- description: The secret id.
  name: sid
  type: string
- description: Thumbprint of the certificate.
  name: x5t
  type: string
- description: CER contents of x509 certificate.
  name: cer
  type: string
- description: The content type of the secret.
  name: contentType
  type: string
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-certificate-bundle-schema.json
slug: azure-key-vault-data-plane-certificate-bundle
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: CertificateBundle
---
