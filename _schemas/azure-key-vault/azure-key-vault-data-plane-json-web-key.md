---
description: As of http://tools.ietf.org/html/draft-ietf-jose-json-web-key-18.
layout: schema
name: JsonWebKey
properties_list:
- description: Key identifier.
  name: kid
  type: string
- description: Supported key operations.
  name: key_ops
  type: array
- description: RSA modulus.
  name: n
  type: string
- description: RSA public exponent.
  name: e
  type: string
- description: RSA private exponent, or the D component of an EC private key.
  name: d
  type: string
- description: RSA private key parameter.
  name: dp
  type: string
- description: RSA private key parameter.
  name: dq
  type: string
- description: RSA private key parameter.
  name: qi
  type: string
- description: RSA secret prime.
  name: p
  type: string
- description: RSA secret prime, with p < q.
  name: q
  type: string
- description: Symmetric key.
  name: k
  type: string
- description: Protected Key, used with Bring Your Own Key.
  name: key_hsm
  type: string
- description: X component of an EC public key.
  name: x
  type: string
- description: Y component of an EC public key.
  name: y
  type: string
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-json-web-key-schema.json
slug: azure-key-vault-data-plane-json-web-key
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: JsonWebKey
---
