---
description: A supplemental insurance claim record.
layout: schema
name: Claim
properties_list:
- description: Unique claim identifier.
  name: claim_id
  type: string
- description: Policy associated with the claim.
  name: policy_id
  type: string
- description: Claimant employee identifier.
  name: employee_id
  type: string
- description: Type of claim event.
  name: claim_type
  type: string
- description: Current claim processing status.
  name: status
  type: string
- description: Date of the qualifying event.
  name: incident_date
  type: string
- description: Timestamp when the claim was submitted.
  name: submission_date
  type: string
- description: Approved benefit payment amount in USD.
  name: benefit_amount
  type: number
- description: Reason for denial if the claim was denied.
  name: denial_reason
  type: string
provider_name: aflac
provider_slug: aflac
schema_file: json-schema/enterprise-connect-claim-schema.json
slug: enterprise-connect-claim
tags: []
title: Claim
---
