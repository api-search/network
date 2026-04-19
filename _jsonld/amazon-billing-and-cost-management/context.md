---
class_count: 19
classes:
- Budget
- BudgetName
- BudgetType
- BudgetLimit
- TimeUnit
- TimePeriod
- CalculatedSpend
- ActualSpend
- ForecastedSpend
- AnomalyMonitor
- MonitorArn
- MonitorName
- MonitorType
- CostCategory
- CostCategoryArn
- Amount
- Unit
- name
- description
context_file: json-ld/context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-billing-and-cost-management/refs/heads/main/json-ld/context.jsonld
description: JSON-LD context defining the semantic vocabulary for context from Amazon Billing And Cost Management.
layout: jsonld
name: context Context
namespaces:
- prefix: schema
  uri: https://schema.org/
- prefix: aws-billing
  uri: https://aws.amazon.com/billing/vocab#
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
property_count: 2
provider_name: Amazon Billing And Cost Management
provider_slug: amazon-billing-and-cost-management
slug: context
tags:
- Billing
- Cost Management
- Cost Explorer
- Budgets
- Cost Optimization
- FinOps
- Amazon Web Services
- AWS
- JSON-LD
- Linked Data
- Semantic Web
---
