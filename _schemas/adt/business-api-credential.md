---
description: An access control credential.
layout: schema
name: Credential
properties_list:
- description: Unique identifier of the credential.
  name: id
  type: string
- description: ID of the user this credential belongs to.
  name: userId
  type: string
- description: Type of credential.
  name: type
  type: string
- description: Credential status.
  name: status
  type: string
- description: Start of credential validity period.
  name: validFrom
  type: string
- description: End of credential validity period.
  name: validTo
  type: string
provider_name: ADT
provider_slug: adt
schema_file: json-schema/business-api-credential-schema.json
slug: business-api-credential
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: Credential
---
