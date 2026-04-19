---
description: Parameters for the issuer of the X509 component of a certificate.
layout: schema
name: IssuerParameters
properties_list:
- description: Name of the referenced issuer object or reserved names; for example, 'Self' or 'Unknown'.
  name: name
  type: string
- description: Certificate type as supported by the provider (optional); for example 'OV-SSL', 'EV-SSL'.
  name: cty
  type: string
- description: Indicates if the certificates generated under this policy should be published to certificate transparency logs.
  name: cert_transparency
  type: boolean
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-issuer-parameters-schema.json
slug: azure-key-vault-data-plane-issuer-parameters
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: IssuerParameters
---
