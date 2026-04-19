---
description: KYCShareholderCheckResult schema from Adyen API
layout: schema
name: KYCShareholderCheckResult
properties_list:
- description: A list of the checks and their statuses.
  name: checks
  type: array
- description: The unique ID of the legal arrangement to which the shareholder belongs, if applicable.
  name: legalArrangementCode
  type: string
- description: The unique ID of the legal arrangement entity to which the shareholder belongs, if applicable.
  name: legalArrangementEntityCode
  type: string
- description: The code of the shareholder to which the check applies.
  name: shareholderCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-kyc-shareholder-check-result-schema.json
slug: accounts-kyc-shareholder-check-result
tags:
- Payments
- Financial Services
- Fintech
title: KYCShareholderCheckResult
---
