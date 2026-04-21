---
consumed_apis:
- workday-compensation
- workday-payroll
- workday-benefits
description: Unified compensation and payroll management combining Compensation, Payroll, and Benefits APIs for payroll administrators to manage pay plans, benefits enrollment, and payroll processing.
layout: capability
name: Workday Compensation and Payroll
operations:
- description: List compensation plans
  method: GET
  name: list-plans
  path: /v1/compensation-plans
- description: List pay groups
  method: GET
  name: list-pay-groups
  path: /v1/pay-groups
- description: List benefit plans
  method: GET
  name: list-benefit-plans
  path: /v1/benefit-plans
personas: []
provider_name: Workday
provider_slug: workday
search_terms:
- list benefit elections
- submit a benefits change request
- compensation
- list dependents
- list compensation grades
- get eligible benefit plans for a worker
- list compensation scorecards
- benefits list dependents
- list plans
- list all pay groups
- payroll list inputs
- benefits change
- payroll get pay group
- get pay group details
- comp list grades
- financial management
- list payroll inputs
- benefits list elections
- request a one-time payment
- pay groups
- submit a compensation change request
- comp request one time payment
- payroll get pay group details
- benefits get eligible plans
- benefits
- benefit plans
- workday
- saas
- list pay groups
- get a pay group by id
- list pay slips
- comp list scorecards
- enterprise software
- cloud computing
- compensation plans
- payroll list pay slips
- list compensation plans
- payroll list pay groups
- hcm
- list all benefit plans
- comp list plans
- payroll
- list benefit plans
- comp request change
- benefits list plans
slug: compensation-and-payroll
tags:
- Workday
- Compensation
- Payroll
- Benefits
tools:
- description: List compensation plans
  hints:
    readOnly: true
  name: comp-list-plans
- description: Submit a compensation change request
  hints:
    readOnly: false
  name: comp-request-change
- description: List compensation scorecards
  hints:
    readOnly: true
  name: comp-list-scorecards
- description: List compensation grades
  hints:
    readOnly: true
  name: comp-list-grades
- description: Request a one-time payment
  hints:
    readOnly: false
  name: comp-request-one-time-payment
- description: List all pay groups
  hints:
    readOnly: true
  name: payroll-list-pay-groups
- description: Get a pay group by ID
  hints:
    readOnly: true
  name: payroll-get-pay-group
- description: Get pay group details
  hints:
    readOnly: true
  name: payroll-get-pay-group-details
- description: List payroll inputs
  hints:
    readOnly: true
  name: payroll-list-inputs
- description: List pay slips
  hints:
    readOnly: true
  name: payroll-list-pay-slips
- description: List benefit elections
  hints:
    readOnly: true
  name: benefits-list-elections
- description: Get eligible benefit plans for a worker
  hints:
    readOnly: true
  name: benefits-get-eligible-plans
- description: List dependents
  hints:
    readOnly: true
  name: benefits-list-dependents
- description: Submit a benefits change request
  hints:
    readOnly: false
  name: benefits-change
- description: List all benefit plans
  hints:
    readOnly: true
  name: benefits-list-plans
---
