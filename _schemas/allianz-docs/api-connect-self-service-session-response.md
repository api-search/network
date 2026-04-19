---
description: Self-service session URL for customer to complete policy details
layout: schema
name: SelfServiceSessionResponse
properties_list:
- description: Unique identifier for the self-service session
  name: session_id
  type: string
- description: URL for the customer to complete their policy application
  name: session_url
  type: string
- description: Timestamp when the session expires
  name: expires_at
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-self-service-session-response-schema.json
slug: api-connect-self-service-session-response
tags:
- Financial Services
- Insurance
- Asset Management
title: SelfServiceSessionResponse
---
