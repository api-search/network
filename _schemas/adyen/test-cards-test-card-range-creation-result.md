---
description: TestCardRangeCreationResult schema from Adyen API
layout: schema
name: TestCardRangeCreationResult
properties_list:
- description: 'The last test card number in the generated test card range. Example: 5432 1234 1234 4321'
  name: cardNumberRangeEnd
  type: string
- description: 'The first test card number in the generated test card range. Example: 5432 1234 1234 1234'
  name: cardNumberRangeStart
  type: string
- description: 'Notification message. It informs about the outcome of the operation. Possible values: * CREATED * ALREADY_EXISTS * ERROR'
  name: creationResultCode
  type: string
- description: An optional information message about the result.
  name: message
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/test-cards-test-card-range-creation-result-schema.json
slug: test-cards-test-card-range-creation-result
tags:
- Payments
- Financial Services
- Fintech
title: TestCardRangeCreationResult
---
