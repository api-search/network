---
description: KYCLegalArrangementEntityCheckResult schema from Adyen API
layout: schema
name: KYCLegalArrangementEntityCheckResult
properties_list:
- description: A list of the checks and their statuses.
  name: checks
  type: array
- description: The unique ID of the legal arrangement to which the entity belongs.
  name: legalArrangementCode
  type: string
- description: The unique ID of the legal arrangement entity to which the check applies.
  name: legalArrangementEntityCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-kyc-legal-arrangement-entity-check-result-schema.json
slug: notifications-kyc-legal-arrangement-entity-check-result
tags:
- Payments
- Financial Services
- Fintech
title: KYCLegalArrangementEntityCheckResult
---
