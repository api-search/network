---
description: The certificate import parameters.
layout: schema
name: CertificateImportParameters
properties_list:
- description: Base64 encoded representation of the certificate object to import. This certificate needs to contain the private key.
  name: value
  type: string
- description: If the private key in base64EncodedCertificate is encrypted, the password used for encryption.
  name: pwd
  type: string
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-certificate-import-parameters-schema.json
slug: azure-key-vault-data-plane-certificate-import-parameters
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: CertificateImportParameters
---
