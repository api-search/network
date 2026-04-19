---
description: Sales order item pricing element entity (A_SalesOrderItemPrcgElmnt) representing a pricing condition at the item level.
layout: schema
name: SalesOrderItemPrcgElmnt
properties_list:
- description: Sales order number
  name: SalesOrder
  type: string
- description: Sales order item number
  name: SalesOrderItem
  type: string
- description: Step number in the pricing procedure
  name: PricingProcedureStep
  type: string
- description: Counter for condition within a step
  name: PricingProcedureCounter
  type: string
- description: Condition type
  name: ConditionType
  type: string
- description: Condition rate
  name: ConditionRateValue
  type: string
- description: Condition currency
  name: ConditionCurrency
  type: string
- description: Condition quantity
  name: ConditionQuantity
  type: string
- description: Condition quantity unit
  name: ConditionQuantityUnit
  type: string
- description: Condition value
  name: ConditionAmount
  type: string
- description: Document currency
  name: TransactionCurrency
  type: string
- description: Condition category
  name: ConditionCategory
  type: string
- description: Statistical condition
  name: ConditionIsForStatistics
  type: boolean
- description: Origin of the condition
  name: ConditionOrigin
  type: string
- description: Group condition indicator
  name: IsGroupCondition
  type: string
- description: Condition control
  name: ConditionControl
  type: string
- description: Reason for inactivity
  name: ConditionInactiveReason
  type: string
- description: Condition class
  name: ConditionClass
  type: string
- description: Manually changed indicator
  name: ConditionIsManuallyChanged
  type: boolean
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
schema_file: json-schema/sap-s4hana-sales-order-sales-order-item-prcg-elmnt-schema.json
slug: sap-s4hana-sales-order-sales-order-item-prcg-elmnt
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
title: SalesOrderItemPrcgElmnt
---
