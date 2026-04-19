---
description: PermitRestriction schema from Adyen API
layout: schema
name: PermitRestriction
properties_list:
- description: The total sum amount of one or more payments made using this permit may not exceed this amount if set.
  name: maxAmount
  type: object
- description: The amount of any single payment using this permit may not exceed this amount if set.
  name: singleTransactionLimit
  type: object
- description: Only a single payment can be made using this permit if set to true, otherwise multiple payments are allowed.
  name: singleUse
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-permit-restriction-schema.json
slug: recurring-permit-restriction
tags:
- Payments
- Financial Services
- Fintech
title: PermitRestriction
---
