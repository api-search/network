---
description: PerformVerificationRequest schema from Adyen API
layout: schema
name: PerformVerificationRequest
properties_list:
- description: The code of the account holder to verify.
  name: accountHolderCode
  type: string
- description: 'The state required for the account holder. > Permitted values: `Processing`, `Payout`.'
  name: accountStateType
  type: string
- description: The tier required for the account holder.
  name: tier
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-perform-verification-request-schema.json
slug: accounts-perform-verification-request
tags:
- Payments
- Financial Services
- Fintech
title: PerformVerificationRequest
---
