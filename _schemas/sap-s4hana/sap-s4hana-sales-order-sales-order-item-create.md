---
description: Request payload for creating a new sales order item
layout: schema
name: SalesOrderItemCreate
properties_list:
- description: Material number
  name: Material
  type: string
- description: Requested quantity
  name: RequestedQuantity
  type: string
- description: Unit of measure
  name: RequestedQuantityUnit
  type: string
- description: Plant
  name: Plant
  type: string
- description: Item category
  name: SalesOrderItemCategory
  type: string
- description: Item description
  name: SalesOrderItemText
  type: string
- description: Customer PO number at item level
  name: PurchaseOrderByCustomer
  type: string
- description: Pricing date
  name: PricingDate
  type: string
- description: Payment terms
  name: CustomerPaymentTerms
  type: string
- description: Customer material number
  name: MaterialByCustomer
  type: string
- description: Batch number
  name: Batch
  type: string
- description: Production plant
  name: ProductionPlant
  type: string
- description: Storage location
  name: StorageLocation
  type: string
- description: Delivery priority
  name: DeliveryPriority
  type: string
- description: Incoterms classification
  name: IncotermsClassification
  type: string
- description: Incoterms location
  name: IncotermsTransferLocation
  type: string
- description: Pricing elements (deep insert)
  name: to_PricingElement
  type: array
- description: Schedule lines (deep insert)
  name: to_ScheduleLine
  type: array
- description: Partners (deep insert)
  name: to_Partner
  type: array
- description: Text records (deep insert)
  name: to_Text
  type: array
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
schema_file: json-schema/sap-s4hana-sales-order-sales-order-item-create-schema.json
slug: sap-s4hana-sales-order-sales-order-item-create
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
title: SalesOrderItemCreate
---
