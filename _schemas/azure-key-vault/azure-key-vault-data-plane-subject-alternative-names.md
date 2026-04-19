---
description: The Subject Alternative Names of a X509 object.
layout: schema
name: SubjectAlternativeNames
properties_list:
- description: Email addresses.
  name: emails
  type: array
- description: Domain names.
  name: dns_names
  type: array
- description: User Principal Names.
  name: upns
  type: array
- description: Uniform Resource Identifiers.
  name: uris
  type: array
- description: IP addresses; supports IPv4 and IPv6.
  name: ipAddresses
  type: array
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-subject-alternative-names-schema.json
slug: azure-key-vault-data-plane-subject-alternative-names
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: SubjectAlternativeNames
---
