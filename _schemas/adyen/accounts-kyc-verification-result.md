---
description: KYCVerificationResult schema from Adyen API
layout: schema
name: KYCVerificationResult
properties_list:
- description: The results of the checks on the account holder.
  name: accountHolder
  type: object
- description: The results of the checks on the legal arrangements.
  name: legalArrangements
  type: array
- description: The results of the checks on the legal arrangement entities.
  name: legalArrangementsEntities
  type: array
- description: The results of the checks on the payout methods.
  name: payoutMethods
  type: array
- description: The results of the checks on the shareholders.
  name: shareholders
  type: array
- description: The results of the checks on the signatories.
  name: signatories
  type: array
- description: The result of the check on the Ultimate Parent Company.
  name: ultimateParentCompany
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-kyc-verification-result-schema.json
slug: accounts-kyc-verification-result
tags:
- Payments
- Financial Services
- Fintech
title: KYCVerificationResult
---
