---
description: Sales order header pricing element entity (A_SalesOrderHeaderPrcgElmnt) representing a pricing condition at the header level, such as overall discounts, surcharges, or freight.
layout: schema
name: SalesOrderHeaderPrcgElmnt
properties_list:
- description: Sales order number
  name: SalesOrder
  type: string
- description: Step number in the pricing procedure
  name: PricingProcedureStep
  type: string
- description: Counter for condition within a step
  name: PricingProcedureCounter
  type: string
- description: Condition type (e.g., PR00 for price, K004 for discount, MWST for tax)
  name: ConditionType
  type: string
- description: Condition rate or amount per pricing unit
  name: ConditionRateValue
  type: string
- description: Currency for the condition
  name: ConditionCurrency
  type: string
- description: Condition pricing quantity
  name: ConditionQuantity
  type: string
- description: Condition quantity unit
  name: ConditionQuantityUnit
  type: string
- description: Condition category
  name: ConditionCategory
  type: string
- description: Statistical condition indicator
  name: ConditionIsForStatistics
  type: boolean
- description: Scale type
  name: PricingScaleType
  type: string
- description: Accrual indicator
  name: IsRelevantForAccrual
  type: boolean
- description: Origin of the condition
  name: ConditionOrigin
  type: string
- description: Group condition indicator
  name: IsGroupCondition
  type: string
- description: Condition value (total amount for the condition)
  name: ConditionAmount
  type: string
- description: Document currency
  name: TransactionCurrency
  type: string
- description: Condition control
  name: ConditionControl
  type: string
- description: Reason the condition is inactive
  name: ConditionInactiveReason
  type: string
- description: Condition class (A=discount, B=surcharge)
  name: ConditionClass
  type: string
- description: Procedure counter for header conditions
  name: PrcgProcedureCounterForHeader
  type: string
- description: Factor for condition basis value
  name: FactorForConditionBasisValue
  type: string
- description: Structure condition
  name: StructureCondition
  type: string
- description: Period factor for condition basis value
  name: PeriodFactorForCndnBasisValue
  type: string
- description: Scale basis indicator
  name: PricingScaleBasis
  type: string
- description: Scale basis value
  name: ConditionScaleBasisValue
  type: string
- description: Condition scale basis unit
  name: ConditionScaleBasisUnit
  type: string
- description: Scale basis currency
  name: ConditionScaleBasisCurrency
  type: string
- description: Relevant for intercompany billing
  name: CndnIsRelevantForIntcoBilling
  type: boolean
- description: Indicator that the condition was manually changed
  name: ConditionIsManuallyChanged
  type: boolean
provider_name: SAP S/4HANA
provider_slug: sap-s4hana
schema_file: json-schema/sap-s4hana-sales-order-sales-order-header-prcg-elmnt-schema.json
slug: sap-s4hana-sales-order-sales-order-header-prcg-elmnt
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
title: SalesOrderHeaderPrcgElmnt
---
