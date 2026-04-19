---
description: CostEstimateAssumptions schema from Adyen API
layout: schema
name: CostEstimateAssumptions
properties_list:
- description: If true, the cardholder is expected to successfully authorise via 3D Secure.
  name: assume3DSecureAuthenticated
  type: boolean
- description: If true, the transaction is expected to have valid Level 3 data.
  name: assumeLevel3Data
  type: boolean
- description: If not zero, the number of installments.
  name: installments
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/binlookup-cost-estimate-assumptions-schema.json
slug: binlookup-cost-estimate-assumptions
tags:
- Payments
- Financial Services
- Fintech
title: CostEstimateAssumptions
---
