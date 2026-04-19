---
description: Request payload for creating a new sales order with optional deep insert
layout: schema
name: SalesOrderCreate
properties_list:
- description: Sales document type
  name: SalesOrderType
  type: string
- description: Sales organization
  name: SalesOrganization
  type: string
- description: Distribution channel
  name: DistributionChannel
  type: string
- description: Organization division
  name: OrganizationDivision
  type: string
- description: Sold-to party customer number
  name: SoldToParty
  type: string
- description: Customer purchase order number
  name: PurchaseOrderByCustomer
  type: string
- description: Document date
  name: SalesOrderDate
  type: string
- description: Requested delivery date
  name: RequestedDeliveryDate
  type: string
- description: Payment terms key
  name: CustomerPaymentTerms
  type: string
- description: Currency key (ISO 4217)
  name: TransactionCurrency
  type: string
- description: Pricing date
  name: PricingDate
  type: string
- description: Incoterms classification
  name: IncotermsClassification
  type: string
- description: Incoterms location
  name: IncotermsTransferLocation
  type: string
- description: Shipping condition
  name: ShippingCondition
  type: string
- description: Complete delivery indicator
  name: CompleteDeliveryIsDefined
  type: boolean
- description: Order reason
  name: SDDocumentReason
  type: string
- description: Items to create (deep insert)
  name: to_Item
  type: array
- description: Partners to create (deep insert)
  name: to_Partner
  type: array
- description: Pricing elements to create (deep insert)
  name: to_PricingElement
  type: array
- description: Text records to create (deep insert)
  name: to_Text
  type: array
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
schema_file: json-schema/sap-s4hana-sales-order-sales-order-create-schema.json
slug: sap-s4hana-sales-order-sales-order-create
tags:
- Business Applications
- Cloud
- Enterprise Resource Planning
- ERP
- Finance
- Human Resources
- Inventory
- Logistics
- Manufacturing
- Plant Maintenance
- Procurement
- S/4HANA
- Sales
- SAP
title: SalesOrderCreate
---
