---
description: AcceptDisputeRequest schema from Adyen API
layout: schema
name: AcceptDisputeRequest
properties_list:
- description: The PSP reference assigned to the dispute.
  name: disputePspReference
  type: string
- description: The merchant account identifier, for which you want to process the dispute transaction.
  name: merchantAccountCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/disputes-accept-dispute-request-schema.json
slug: disputes-accept-dispute-request
tags:
- Payments
- Financial Services
- Fintech
title: AcceptDisputeRequest
---
