---
description: An insurance claim filed under an AIG policy
layout: schema
name: InsuranceClaim
properties_list:
- description: Unique claim identifier
  name: claim_number
  type: string
- description: Associated policy number
  name: policy_number
  type: string
- description: Date of loss occurrence
  name: loss_date
  type: string
- description: Date claim was reported
  name: reported_date
  type: string
- description: Description of the loss or damage
  name: loss_description
  type: string
- description: Estimated loss amount in USD
  name: loss_amount
  type: number
- description: Current claim status
  name: claim_status
  type: string
- description: Name of assigned claims adjuster
  name: adjuster_name
  type: string
provider_name: AIG
provider_slug: aig
schema_file: json-schema/aig-insurance-claim-schema.json
slug: aig-insurance-claim
tags:
- Insurance
- Financial Services
- Property Casualty
- Cyber Insurance
- Enterprise
title: InsuranceClaim
---
