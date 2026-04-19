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
- payroll get pay group details
- benefits list elections
- list pay groups
- benefits change
- benefits list dependents
- list compensation plans
- comp list grades
- payroll list pay groups
- cloud computing
- list plans
- get a pay group by id
- list pay slips
- get eligible benefit plans for a worker
- list benefit elections
- benefits
- list all benefit plans
- payroll
- financial management
- enterprise software
- payroll list pay slips
- benefits list plans
- list all pay groups
- compensation
- request a one-time payment
- submit a compensation change request
- payroll get pay group
- workday
- get pay group details
- comp list scorecards
- compensation plans
- submit a benefits change request
- comp request one time payment
- pay groups
- list compensation grades
- list benefit plans
- benefit plans
- payroll list inputs
- hcm
- saas
- list compensation scorecards
- list dependents
- benefits get eligible plans
- comp request change
- list payroll inputs
- comp list plans
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
