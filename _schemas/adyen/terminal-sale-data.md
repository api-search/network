---
description: Data associated to the Sale System, with a particular value during the processing of the payment by the POI, including the cards acquisition. Data related to the Sale System.
layout: schema
name: SaleData
properties_list:
- description: ''
  name: OperatorID
  type: string
- description: if different from the Login.
  name: OperatorLanguage
  type: string
- description: if different from the Login and see Login .SaleData.
  name: ShiftNumber
  type: string
- description: ''
  name: SaleTransactionID
  type: object
- description: If payment reservation.
  name: SaleReferenceID
  type: string
- description: ''
  name: SaleTerminalData
  type: object
- description: ''
  name: TokenRequestedType
  type: object
- description: Additional and optional identification of a customer order.
  name: CustomerOrderID
  type: string
- description: ''
  name: CustomerOrderReq
  type: object
- description: Stored with the transaction.
  name: SaleToPOIData
  type: string
- description: Send to the Acquirer if present.
  name: SaleToAcquirerData
  type: string
- description: ''
  name: SaleToIssuerData
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-sale-data-schema.json
slug: terminal-sale-data
tags:
- Payments
- Financial Services
- Fintech
title: SaleData
---
