---
description: ''
layout: schema
name: score
properties_list:
- description: A score type for which score is retrieved, Possible value - DELINQUENCY.
  name: scoreType
  type: string
- description: A product type for which score is retrieved, Possible value - CREDIT_CARD.
  name: productType
  type: string
- description: The score retrieved for the card number.
  name: score
  type: integer
- description: The decile is any of the values in a series that divides the distribution of individuals in that series into ten groups of equal frequency.
  name: decile
  type: integer
- description: Name of the model used for scoring against customerPANs.
  name: modelName
  type: string
- description: Optional parameter embeddings is intermediate machine readable output from score calculation.
  name: embeddingFeatures
  type: string
- description: Indicates whether the change in score has resulted in a change in decile classification compared to the previous week. For new prospects, this value is always set to 'false' based on the underlying mo
  name: hasScoreChangedFromLastWeek
  type: boolean
- description: Indicates whether the card is not issued by the bank requesting the score.
  name: isNewProspect
  type: boolean
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-consumer-credit-analytics-score-schema.json
slug: mastercard-consumer-credit-analytics-score
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: score
---
