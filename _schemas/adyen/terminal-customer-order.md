---
description: Customer order attached to a customer, recorded in the POI system. Allows the management of customer orders by the POI, for instance in a multi-channel or a click and collect sale transaction.
layout: schema
name: CustomerOrder
properties_list:
- description: Additional and optional identification of a customer order.
  name: CustomerOrderID
  type: string
- description: ''
  name: SaleReferenceID
  type: string
- description: ''
  name: OpenOrderState
  type: boolean
- description: Date time of the beginning of an operation.
  name: StartDate
  type: string
- description: Date time of the end of an operation.
  name: EndDate
  type: string
- description: ''
  name: ForecastedAmount
  type: number
- description: Total amount of all completed transactions of a customer order.
  name: CurrentAmount
  type: number
- description: Currency of a monetary amount.
  name: Currency
  type: string
- description: ''
  name: AccessedBy
  type: string
- description: Unqualified information.
  name: AdditionalInformation
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-customer-order-schema.json
slug: terminal-customer-order
tags:
- Payments
- Financial Services
- Fintech
title: CustomerOrder
---
