---
description: ActivationRequest schema from AB Tasty Decision API
layout: schema
name: ActivationRequest
properties_list:
- description: Visitor ID
  name: vid
  type: string
- description: Anonymous ID (for experience continuity)
  name: aid
  type: string
- description: Environment ID
  name: cid
  type: string
- description: Variation group ID
  name: caid
  type: string
- description: Variation ID
  name: vaid
  type: string
provider_name: AB Tasty
provider_slug: ab-tasty
schema_file: json-schema/decision-api-activation-request-schema.json
slug: decision-api-activation-request
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
title: ActivationRequest
---
