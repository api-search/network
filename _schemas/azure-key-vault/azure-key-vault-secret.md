---
description: A secret consisting of a value, id and its attributes as returned by the Azure Key Vault data plane API. Based on the SecretBundle definition from the Azure Key Vault REST API reference at https://learn.microsoft.com/en-us/rest/api/keyvault/secrets.
layout: schema
name: Azure Key Vault Secret Bundle
properties_list:
- description: The secret value.
  name: value
  type: string
- description: The secret id. The format is https://{vault-name}.vault.azure.net/secrets/{secret-name}/{secret-version}.
  name: id
  type: string
- description: The content type of the secret (e.g., 'application/x-pkcs12', 'text/plain', 'application/json').
  name: contentType
  type: string
- description: ''
  name: attributes
  type: object
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
- description: If this is a secret backing a KV certificate, then this field specifies the corresponding key backing the KV certificate.
  name: kid
  type: string
- description: True if the secret's lifetime is managed by key vault. If this is a secret backing a certificate, then managed will be true.
  name: managed
  type: boolean
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-secret-schema.json
slug: azure-key-vault-secret
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: Azure Key Vault Secret Bundle
---
