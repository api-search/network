---
description: In the Payment or the Loyalty Request message, it allows using the card of a previous CardAcquisition or Payment/Loyalty request. Identification of a previous POI transaction.
layout: schema
name: OriginalPOITransaction
properties_list:
- description: Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.
  name: SaleID
  type: string
- description: If original transaction is coming from another POI.
  name: POIID
  type: string
- description: ''
  name: POITransactionID
  type: object
- description: Indicate if the card data has to be got from a previous transaction.
  name: ReuseCardDataFlag
  type: boolean
- description: If referral.
  name: ApprovalCode
  type: string
- description: If the language is selected by the Sale System before the request to the POI.
  name: CustomerLanguage
  type: string
- description: Restrict to these Acquirer if present.
  name: AcquirerID
  type: integer
- description: ''
  name: AmountValue
  type: number
- description: ''
  name: HostTransactionID
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-original-poi-transaction-schema.json
slug: terminal-original-poi-transaction
tags:
- Payments
- Financial Services
- Fintech
title: OriginalPOITransaction
---
