---
description: Schema for SAP sales order documents used in S/4HANA and Business One APIs.
layout: schema
name: SAP Sales Order
properties_list:
- description: Sales order number
  name: SalesOrder
  type: string
- description: Sales document type
  name: SalesOrderType
  type: string
- description: Sales organization code
  name: SalesOrganization
  type: string
- description: Distribution channel
  name: DistributionChannel
  type: string
- description: Division
  name: OrganizationDivision
  type: string
- description: Sold-to party business partner number
  name: SoldToParty
  type: string
- description: Customer purchase order number
  name: PurchaseOrderByCustomer
  type: string
- description: Sales order date
  name: SalesOrderDate
  type: string
- description: Requested delivery date
  name: RequestedDeliveryDate
  type: string
- description: Net value of the sales order in document currency
  name: TotalNetAmount
  type: number
- description: Document currency (ISO 4217)
  name: TransactionCurrency
  type: string
- description: Overall delivery status
  name: OverallDeliveryStatus
  type: string
- description: Sales order line items
  name: Items
  type: array
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-sales-order-schema.json
slug: sap-sales-order
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: SAP Sales Order
---
