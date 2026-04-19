---
description: Self-service estimate session with redirect URL for customer
layout: schema
name: SelfServiceEstimateResponse
properties_list:
- description: Unique identifier for the estimate session
  name: session_id
  type: string
- description: URL for the customer to view and complete their estimate
  name: estimate_url
  type: string
- description: Timestamp when the session expires
  name: expires_at
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-self-service-estimate-response-schema.json
slug: api-connect-self-service-estimate-response
tags:
- Financial Services
- Insurance
- Asset Management
title: SelfServiceEstimateResponse
---
