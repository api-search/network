---
description: Request payload for submitting a new claim.
layout: schema
name: ClaimRequest
properties_list:
- description: Policy against which to file the claim.
  name: policy_id
  type: string
- description: Type of claim event.
  name: claim_type
  type: string
- description: Date of the qualifying event.
  name: incident_date
  type: string
- description: Description of the incident or diagnosis.
  name: description
  type: string
provider_name: aflac
provider_slug: aflac
schema_file: json-schema/enterprise-connect-claim-request-schema.json
slug: enterprise-connect-claim-request
tags: []
title: ClaimRequest
---
