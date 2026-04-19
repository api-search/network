---
description: Sales order item entity (A_SalesOrderItem) representing a line item in a sales order. Contains material, quantity, pricing, plant assignment, and item-level processing status.
layout: schema
name: SalesOrderItem
properties_list:
- description: Sales order number the item belongs to
  name: SalesOrder
  type: string
- description: Sales order item number (e.g., '000010')
  name: SalesOrderItem
  type: string
- description: Higher-level item number in a BOM structure
  name: HigherLevelItem
  type: string
- description: Item category (e.g., TAN for standard item, TANN for free-of-charge)
  name: SalesOrderItemCategory
  type: string
- description: Short text description of the item
  name: SalesOrderItemText
  type: string
- description: Customer purchase order number at item level
  name: PurchaseOrderByCustomer
  type: string
- description: Material number
  name: Material
  type: string
- description: Material number used by the customer
  name: MaterialByCustomer
  type: string
- description: Pricing date at item level
  name: PricingDate
  type: string
- description: Billing plan number
  name: BillingPlan
  type: string
- description: Requested quantity
  name: RequestedQuantity
  type: string
- description: Unit of measure for the requested quantity (ISO unit code)
  name: RequestedQuantityUnit
  type: string
- description: SAP internal unit of measure
  name: RequestedQuantitySAPUnit
  type: string
- description: Indicator that the requested quantity is fixed
  name: RequestedQuantityIsFixed
  type: boolean
- description: Gross weight of the item
  name: ItemGrossWeight
  type: string
- description: Net weight of the item
  name: ItemNetWeight
  type: string
- description: Weight unit (e.g., KG, LB)
  name: ItemWeightUnit
  type: string
- description: Volume of the item
  name: ItemVolume
  type: string
- description: Volume unit
  name: ItemVolumeUnit
  type: string
- description: Transaction currency (ISO 4217)
  name: TransactionCurrency
  type: string
- description: Net value of the item in document currency
  name: NetAmount
  type: string
- description: Total SD amount
  name: TotalSDAmount
  type: string
- description: Material group
  name: MaterialGroup
  type: string
- description: Material pricing group
  name: MaterialPricingGroup
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
- description: Delivery group
  name: DeliveryGroup
  type: string
- description: Shipping point or receiving point
  name: ShippingPoint
  type: string
- description: Shipping type
  name: ShippingType
  type: string
- description: Delivery priority
  name: DeliveryPriority
  type: string
- description: Incoterms at item level
  name: IncotermsClassification
  type: string
- description: Incoterms location at item level
  name: IncotermsTransferLocation
  type: string
- description: Payment terms at item level
  name: CustomerPaymentTerms
  type: string
- description: Tax classification for material
  name: ProductTaxClassification1
  type: string
- description: Reason for rejection of the item
  name: SalesDocumentRjcnReason
  type: string
- description: Billing block at item level
  name: ItemBillingBlockReason
  type: string
- description: WBS element for project assignment
  name: WBSElement
  type: string
- description: Profit center
  name: ProfitCenter
  type: string
- description: Internal order number
  name: OrderID
  type: string
- description: Cost center
  name: CostCenter
  type: string
- description: Reference document number
  name: ReferenceSDDocument
  type: string
- description: Reference document item
  name: ReferenceSDDocumentItem
  type: string
- description: Processing status at item level
  name: SDProcessStatus
  type: string
- description: Delivery status
  name: DeliveryStatus
  type: string
- description: Order-related billing status
  name: OrderRelatedBillingStatus
  type: string
- description: Plant (delivering plant)
  name: Plant
  type: string
- description: Warehouse number
  name: WarehouseNumber
  type: string
- description: Customer group
  name: CustomerGroup
  type: string
- description: Sales district
  name: SalesDistrict
  type: string
- description: Item usage
  name: CustomerMaterialItemUsage
  type: string
- description: Navigation to item pricing elements
  name: to_PricingElement
  type: array
- description: Navigation to item schedule lines
  name: to_ScheduleLine
  type: array
- description: Navigation to item partner functions
  name: to_Partner
  type: array
- description: Navigation to item text records
  name: to_Text
  type: array
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
schema_file: json-schema/sap-s4hana-sales-order-sales-order-item-schema.json
slug: sap-s4hana-sales-order-sales-order-item
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
title: SalesOrderItem
---
