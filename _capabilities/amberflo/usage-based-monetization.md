---
consumed_apis:
- amberflo-metering
- amberflo-billing
description: Unified workflow for API monetization teams combining metering and billing APIs. Enables end-to-end usage tracking, customer management, and billing automation for product and finance teams.
layout: capability
name: Amberflo Usage-Based Monetization
operations:
- description: List all meter definitions
  method: GET
  name: list-meter-definitions
  path: /v1/meter-definitions
- description: Create a new meter definition
  method: POST
  name: create-meter-definition
  path: /v1/meter-definitions
- description: Ingest usage events for metering
  method: POST
  name: ingest-events
  path: /v1/events
- description: Query aggregated usage data
  method: POST
  name: query-usage
  path: /v1/usage
- description: List all customers
  method: GET
  name: list-customers
  path: /v1/customers
- description: Create a new customer account
  method: POST
  name: create-customer
  path: /v1/customers
- description: List invoices for a customer
  method: GET
  name: list-invoices
  path: /v1/invoices
- description: Create a prepaid order for a customer
  method: POST
  name: create-prepaid-order
  path: /v1/prepaid-orders
personas: []
provider_name: Amberflo
provider_slug: amberflo
search_terms:
- customer billing and subscription management
- integrates metering sdk and ingests usage events
- finops
- manage customer accounts
- list meter definitions
- ingest meter events to track usage
- list invoices for a specific customer
- manage meter definitions for tracking usage
- create prepaid order
- list customers
- create a new meter definition
- ingest events
- list invoices
- query usage data
- list all meter definitions
- ingest meter events
- create meter definition
- query usage
- monetization
- manage prepaid credit orders
- create a new customer account
- query aggregated usage data for a meter
- monitors revenue, invoices, and billing analytics
- ai and cloud cost governance
- amberflo
- ingest usage events for metering
- list invoices for a customer
- billing
- create a new customer account in amberflo
- manages pricing models and billing configuration
- usage event tracking and aggregation
- end-to-end workflow combining metering and billing apis
- ai cost management
- metering
- Product Manager
- list all customer accounts in amberflo
- Finance Team
- create a new meter definition to track usage events
- list all customers
- create a prepaid order for a customer
- usage-based billing
- create a prepaid credit order for a customer
- create customer
- list all meter definitions for usage tracking
- API Developer
- retrieve customer invoices
- query aggregated usage data
slug: usage-based-monetization
tags:
- Amberflo
- Usage-Based Billing
- Metering
- Monetization
- FinOps
tools:
- description: List all meter definitions for usage tracking
  hints:
    openWorld: true
    readOnly: true
  name: list-meter-definitions
- description: Create a new meter definition to track usage events
  hints:
    readOnly: false
  name: create-meter-definition
- description: Ingest meter events to track usage
  hints:
    readOnly: false
  name: ingest-events
- description: Query aggregated usage data for a meter
  hints:
    openWorld: true
    readOnly: true
  name: query-usage
- description: List all customer accounts in Amberflo
  hints:
    openWorld: true
    readOnly: true
  name: list-customers
- description: Create a new customer account in Amberflo
  hints:
    readOnly: false
  name: create-customer
- description: List invoices for a specific customer
  hints:
    openWorld: true
    readOnly: true
  name: list-invoices
- description: Create a prepaid credit order for a customer
  hints:
    readOnly: false
  name: create-prepaid-order
---
