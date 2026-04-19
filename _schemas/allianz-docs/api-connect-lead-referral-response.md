---
description: Confirmation of a submitted lead referral
layout: schema
name: LeadReferralResponse
properties_list:
- description: Unique identifier for the submitted lead
  name: lead_id
  type: string
- description: Status of the lead submission
  name: status
  type: string
- description: Timestamp when the lead was submitted
  name: created_at
  type: string
- description: Team or person the lead has been assigned to
  name: assigned_to
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-lead-referral-response-schema.json
slug: api-connect-lead-referral-response
tags:
- Financial Services
- Insurance
- Asset Management
title: LeadReferralResponse
---
