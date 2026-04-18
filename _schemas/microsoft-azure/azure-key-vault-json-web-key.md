---
description: JSON Web Key (JWK) representation of a key.
layout: schema
name: JsonWebKey
properties_list:
- description: Key identifier.
  name: kid
  type: string
- description: Key type (e.g., RSA, EC, oct, oct-HSM).
  name: kty
  type: string
- description: Allowed key operations.
  name: key_ops
  type: array
- description: RSA modulus.
  name: n
  type: string
- description: RSA public exponent.
  name: e
  type: string
- description: RSA private exponent.
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
- description: RSA secret prime.
  name: q
  type: string
- description: Symmetric key.
  name: k
  type: string
- description: Elliptic curve name.
  name: crv
  type: string
- description: X component of an EC public key.
  name: x
  type: string
- description: Y component of an EC public key.
  name: y
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-json-web-key-schema.json
slug: azure-key-vault-json-web-key
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: JsonWebKey
---
