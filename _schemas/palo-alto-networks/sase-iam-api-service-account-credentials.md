---
description: ServiceAccountCredentials schema from Palo Alto Networks SASE IAM Service API
layout: schema
name: ServiceAccountCredentials
properties_list:
- description: Unique identifier of the generated key.
  name: key_id
  type: string
- description: OAuth 2.0 client ID for this credential set.
  name: client_id
  type: string
- description: OAuth 2.0 client secret. Returned only once at creation time. Store this value securely as it cannot be retrieved again.
  name: client_secret
  type: string
- description: Description provided when the key was created.
  name: description
  type: string
- description: Expiration timestamp, or null if credentials do not expire.
  name: expires_at
  type: string
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-iam-api-service-account-credentials-schema.json
slug: sase-iam-api-service-account-credentials
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ServiceAccountCredentials
---
