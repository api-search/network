---
description: SOAP response containing session and security tokens.
layout: schema
name: SessionLogonResponse
properties_list:
- description: Session token to be passed as __sessiontoken cookie on subsequent requests.
  name: sessionToken
  type: string
- description: Security token to be passed as X-Security-Token header on subsequent requests.
  name: securityToken
  type: string
- description: Information about the authenticated session.
  name: sessionInfo
  type: object
provider_name: Adobe Campaign
provider_slug: adobe-campaign
schema_file: json-schema/adobe-campaign-classic-session-logon-response-schema.json
slug: adobe-campaign-classic-session-logon-response
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
title: SessionLogonResponse
---
