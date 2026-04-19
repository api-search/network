---
description: DefendDisputeRequest schema from Adyen API
layout: schema
name: DefendDisputeRequest
properties_list:
- description: The defense reason code that was selected to defend this dispute.
  name: defenseReasonCode
  type: string
- description: The PSP reference assigned to the dispute.
  name: disputePspReference
  type: string
- description: The merchant account identifier, for which you want to process the dispute transaction.
  name: merchantAccountCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/disputes-defend-dispute-request-schema.json
slug: disputes-defend-dispute-request
tags:
- Payments
- Financial Services
- Fintech
title: DefendDisputeRequest
---
