---
description: KYCLegalArrangementCheckResult schema from Adyen API
layout: schema
name: KYCLegalArrangementCheckResult
properties_list:
- description: A list of the checks and their statuses.
  name: checks
  type: array
- description: The unique ID of the legal arrangement to which the check applies.
  name: legalArrangementCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-kyc-legal-arrangement-check-result-schema.json
slug: accounts-kyc-legal-arrangement-check-result
tags:
- Payments
- Financial Services
- Fintech
title: KYCLegalArrangementCheckResult
---
