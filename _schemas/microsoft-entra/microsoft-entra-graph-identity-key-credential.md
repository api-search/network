---
description: Contains a key credential (certificate) associated with an application or service principal
layout: schema
name: KeyCredential
properties_list:
- description: Unique identifier for the key
  name: keyId
  type: string
- description: Friendly name for the key
  name: displayName
  type: '[''string'', ''null'']'
- description: Type of key credential
  name: type
  type: string
- description: Describes the purpose of the key
  name: usage
  type: string
- description: The certificate's raw data in byte array converted to Base64 string
  name: key
  type: string
- description: The date and time at which the credential becomes valid
  name: startDateTime
  type: string
- description: The date and time at which the credential expires
  name: endDateTime
  type: string
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-key-credential-schema.json
slug: microsoft-entra-graph-identity-key-credential
tags:
- Access Management
- Authentication
- Azure AD
- Entra
- Identity
- Identity Governance
- Microsoft
- Network Security
- Security
- Zero Trust
title: KeyCredential
---
