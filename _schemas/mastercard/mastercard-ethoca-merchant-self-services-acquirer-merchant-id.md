---
description: Acquirer reference ID & card acceptor ID pair
layout: schema
name: AcquirerMerchantId
properties_list:
- description: Marks the ARID/CAID pair as relevant for the FPT engine. When false, the FPT engine won't use the ARID/CAID pair for identifying transactions.
  name: firstPartyTrustEnabled
  type: boolean
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-ethoca-merchant-self-services-acquirer-merchant-id-schema.json
slug: mastercard-ethoca-merchant-self-services-acquirer-merchant-id
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: AcquirerMerchantId
---
