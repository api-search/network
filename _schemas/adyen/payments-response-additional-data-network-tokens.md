---
description: ResponseAdditionalDataNetworkTokens schema from Adyen API
layout: schema
name: ResponseAdditionalDataNetworkTokens
properties_list:
- description: Indicates whether a network token is available for the specified card.
  name: networkToken.available
  type: string
- description: The Bank Identification Number of a tokenized card, which is the first six digits of a card number.
  name: networkToken.bin
  type: string
- description: The last four digits of a network token.
  name: networkToken.tokenSummary
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-response-additional-data-network-tokens-schema.json
slug: payments-response-additional-data-network-tokens
tags:
- Payments
- Financial Services
- Fintech
title: ResponseAdditionalDataNetworkTokens
---
