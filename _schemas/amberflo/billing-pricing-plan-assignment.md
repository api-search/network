---
description: Assignment of a pricing plan to a customer
layout: schema
name: PricingPlanAssignment
properties_list:
- description: Customer identifier
  name: customerId
  type: string
- description: Product or pricing plan identifier
  name: productId
  type: string
- description: Plan start time in Unix milliseconds
  name: startTime
  type: integer
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/billing-pricing-plan-assignment-schema.json
slug: billing-pricing-plan-assignment
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: PricingPlanAssignment
---
