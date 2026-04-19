---
description: Properties of the X509 component of a certificate.
layout: schema
name: X509CertificateProperties
properties_list:
- description: The subject name. Should be a valid X509 distinguished name.
  name: subject
  type: string
- description: The enhanced key usage.
  name: ekus
  type: array
- description: Defines how the certificate's key may be used.
  name: key_usage
  type: array
- description: The duration that the certificate is valid in months.
  name: validity_months
  type: integer
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-x509-certificate-properties-schema.json
slug: azure-key-vault-data-plane-x509-certificate-properties
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: X509CertificateProperties
---
