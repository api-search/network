---
description: Coupon History for a Fixed Income security.
layout: schema
name: couponHistory
properties_list:
- description: Security identifier used in the request.
  name: requestId
  type: string
- description: FactSet Permanent Security Identifier.
  name: fsymId
  type: string
- description: Coupon Accrual Date
  name: date
  type: string
- description: Coupon Basket Flag
  name: couponBasketFlag
  type: boolean
- description: Effective Payment Date
  name: couponEffPmtDate
  type: string
- description: Coupon Formula
  name: couponFormula
  type: string
- description: First Coupon Reset Date
  name: couponInitResetDate
  type: string
- description: Coupon Reset Frequency
  name: couponResetFreq
  type: string
- description: Coupon Link
  name: couponLink
  type: string
- description: Margin
  name: couponMargin
  type: number
- description: Coupon Minimum-Floating Rate
  name: couponMinFloatRate
  type: number
- description: Coupon Structure Sub Code
  name: couponStructSubCode
  type: string
- description: Coupon Type
  name: couponTypeStruct
  type: string
- description: Variable Coupon Payments
  name: couponVarPmtFlag
  type: boolean
- description: Underlying Index
  name: underlyingIndex
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-terms-and-conditions-coupon-history-schema.json
slug: factset-terms-and-conditions-coupon-history
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: couponHistory
---
