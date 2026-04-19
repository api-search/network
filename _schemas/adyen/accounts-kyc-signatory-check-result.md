---
description: KYCSignatoryCheckResult schema from Adyen API
layout: schema
name: KYCSignatoryCheckResult
properties_list:
- description: A list of the checks and their statuses.
  name: checks
  type: array
- description: The code of the signatory to which the check applies.
  name: signatoryCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-kyc-signatory-check-result-schema.json
slug: accounts-kyc-signatory-check-result
tags:
- Payments
- Financial Services
- Fintech
title: KYCSignatoryCheckResult
---
