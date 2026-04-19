---
description: CreateTestCardRangesRequest schema from Adyen API
layout: schema
name: CreateTestCardRangesRequest
properties_list:
- description: The code of the account, for which the test card ranges should be created.
  name: accountCode
  type: string
- description: 'The type of the account, for which the test card ranges should be created. Permitted values: * Company * MerchantAccount > These values are case-sensitive.'
  name: accountTypeCode
  type: string
- description: A list of test card ranges to create.
  name: testCardRanges
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/test-cards-create-test-card-ranges-request-schema.json
slug: test-cards-create-test-card-ranges-request
tags:
- Payments
- Financial Services
- Fintech
title: CreateTestCardRangesRequest
---
