---
description: A stored credential for a user's connector
layout: schema
name: Credential
properties_list:
- description: Unique identifier for the credential
  name: credentialId
  type: string
- description: Connector this credential belongs to
  name: connectorId
  type: string
- description: User this credential belongs to
  name: userId
  type: string
- description: Timestamp when the credential was created
  name: createdAt
  type: string
provider_name: Alloy Automation
provider_slug: alloy-automation
schema_file: json-schema/alloy-connectivity-credential-schema.json
slug: alloy-connectivity-credential
tags:
- Automation
- Embedded Integrations
- Integrations
- iPaaS
- Unified API
- Workflows
title: Credential
---
