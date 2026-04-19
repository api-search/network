---
description: CampaignRequest schema from AB Tasty Decision API
layout: schema
name: CampaignRequest
properties_list:
- description: Unique identifier for the application user or website visitor
  name: visitor_id
  type: string
- description: Identifier for anonymous visitors (e.g., session ID)
  name: anonymous_id
  type: string
- description: JSON object of key-value pairs describing the user and device context
  name: context
  type: object
- description: Determines if visitor has consented to GDPR rules
  name: visitor_consent
  type: boolean
- description: Determines whether a CAMPAIGN hit should be automatically sent
  name: trigger_hit
  type: boolean
- description: Groups visitors to receive the same variation assignment
  name: decision_group
  type: string
provider_name: AB Tasty
provider_slug: ab-tasty
schema_file: json-schema/decision-api-campaign-request-schema.json
slug: decision-api-campaign-request
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
title: CampaignRequest
---
