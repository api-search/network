---
description: KYCCheckSummary schema from Adyen API
layout: schema
name: KYCCheckSummary
properties_list:
- description: The code of the check. For possible values, refer to [Verification codes](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/verification-codes).
  name: kycCheckCode
  type: integer
- description: A description of the check.
  name: kycCheckDescription
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-kyc-check-summary-schema.json
slug: accounts-kyc-check-summary
tags:
- Payments
- Financial Services
- Fintech
title: KYCCheckSummary
---
