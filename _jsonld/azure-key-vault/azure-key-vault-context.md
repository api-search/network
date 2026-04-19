---
class_count: 0
classes: []
context_file: json-ld/azure-key-vault-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/azure-key-vault/refs/heads/main/json-ld/azure-key-vault-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Azure Key Vault from Azure Key Vault.
layout: jsonld
name: Azure Key Vault Context
namespaces:
- prefix: kv
  uri: https://schema.api.gov/azure/key-vault/
- prefix: azure
  uri: https://schema.api.gov/azure/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: sec
  uri: https://w3id.org/security#
- prefix: jwk
  uri: https://www.iana.org/assignments/jose/
properties:
- container: ''
  name: KeyVault
  type: reference
- container: ''
  name: SecretBundle
  type: reference
- container: ''
  name: KeyBundle
  type: reference
- container: ''
  name: CertificateBundle
  type: reference
- container: ''
  name: CertificatePolicy
  type: reference
- container: ''
  name: CertificateOperation
  type: reference
- container: ''
  name: JsonWebKey
  type: reference
- container: ''
  name: id
  type: reference
- container: ''
  name: kid
  type: reference
- container: ''
  name: sid
  type: reference
- container: ''
  name: value
  type: ''
- container: ''
  name: contentType
  type: ''
- container: ''
  name: attributes
  type: reference
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: nbf
  type: integer
- container: ''
  name: exp
  type: integer
- container: ''
  name: created
  type: integer
- container: ''
  name: updated
  type: integer
- container: ''
  name: recoveryLevel
  type: ''
- container: ''
  name: recoverableDays
  type: integer
- container: ''
  name: managed
  type: boolean
- container: ''
  name: tags
  type: ''
- container: ''
  name: key
  type: reference
- container: ''
  name: kty
  type: ''
- container: ''
  name: key_ops
  type: ''
- container: ''
  name: key_size
  type: integer
- container: ''
  name: crv
  type: ''
- container: ''
  name: n
  type: ''
- container: ''
  name: e
  type: ''
- container: ''
  name: d
  type: ''
- container: ''
  name: x
  type: ''
- container: ''
  name: y
  type: ''
- container: ''
  name: release_policy
  type: reference
- container: ''
  name: exportable
  type: boolean
- container: ''
  name: policy
  type: reference
- container: ''
  name: key_props
  type: reference
- container: ''
  name: secret_props
  type: reference
- container: ''
  name: x509_props
  type: reference
- container: ''
  name: issuer
  type: reference
- container: ''
  name: subject
  type: ''
- container: ''
  name: sans
  type: reference
- container: ''
  name: dns_names
  type: ''
- container: ''
  name: emails
  type: ''
- container: ''
  name: validity_months
  type: integer
- container: ''
  name: lifetime_actions
  type: ''
- container: ''
  name: reuse_key
  type: boolean
- container: ''
  name: cer
  type: ''
- container: ''
  name: x5t
  type: ''
- container: ''
  name: csr
  type: ''
- container: ''
  name: status
  type: ''
- container: ''
  name: request_id
  type: ''
- container: ''
  name: recoveryId
  type: reference
- container: ''
  name: scheduledPurgeDate
  type: integer
- container: ''
  name: deletedDate
  type: integer
- container: ''
  name: name
  type: ''
- container: ''
  name: description
  type: ''
- container: ''
  name: url
  type: reference
property_count: 57
provider_name: Azure Key Vault
provider_slug: azure-key-vault
slug: azure-key-vault-context
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
- JSON-LD
- Linked Data
- Semantic Web
---
