---
description: AccountProcessingState schema from Adyen API
layout: schema
name: AccountProcessingState
properties_list:
- description: The reason why processing has been disabled.
  name: disableReason
  type: string
- description: Indicates whether the processing of payments is allowed.
  name: disabled
  type: boolean
- description: The lower bound of the processing tier (i.e., an account holder must have processed at least this amount of money in order to be placed into this tier).
  name: processedFrom
  type: object
- description: The upper bound of the processing tier (i.e., an account holder must have processed less than this amount of money in order to be placed into this tier).
  name: processedTo
  type: object
- description: The processing tier that the account holder occupies.
  name: tierNumber
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-account-processing-state-schema.json
slug: accounts-account-processing-state
tags:
- Payments
- Financial Services
- Fintech
title: AccountProcessingState
---
