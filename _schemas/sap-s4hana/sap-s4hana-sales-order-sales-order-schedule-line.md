---
description: Sales order schedule line entity (A_SalesOrderScheduleLine) representing a delivery schedule for a sales order item with confirmed quantities and dates from availability check (ATP).
layout: schema
name: SalesOrderScheduleLine
properties_list:
- description: Sales order number
  name: SalesOrder
  type: string
- description: Sales order item number
  name: SalesOrderItem
  type: string
- description: Schedule line number
  name: ScheduleLine
  type: string
- description: Requested delivery date
  name: RequestedDeliveryDate
  type: string
- description: Confirmed delivery date from ATP check
  name: ConfirmedDeliveryDate
  type: string
- description: Order quantity unit
  name: OrderQuantityUnit
  type: string
- description: SAP internal unit of measure
  name: OrderQuantitySAPUnit
  type: string
- description: Ordered quantity on the schedule line
  name: ScheduleLineOrderQuantity
  type: string
- description: Confirmed quantity from material availability check
  name: ConfdOrderQtyByMatlAvailCheck
  type: string
- description: Delivered quantity in order unit
  name: DeliveredQtyInOrderQtyUnit
  type: string
- description: Open confirmed delivery quantity
  name: OpenConfdDelivQtyInOrdQtyUnit
  type: string
- description: Corrected quantity
  name: CorrectedQtyInOrderQtyUnit
  type: string
- description: Delivery block for the schedule line
  name: DelivBlockReasonForSchedLine
  type: string
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
schema_file: json-schema/sap-s4hana-sales-order-sales-order-schedule-line-schema.json
slug: sap-s4hana-sales-order-sales-order-schedule-line
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
title: SalesOrderScheduleLine
---
