---
consumed_apis:
- scm
- approval-workflow
description: Unified workflow for supply chain managers combining procurement, inventory, order fulfillment, and approval workflows across PeopleSoft Supply Chain Management and Approval Workflow Engine APIs.
layout: capability
name: PeopleSoft Supply Chain And Procurement
operations:
- description: Retrieve procurement requisitions.
  method: GET
  name: list-requisitions
  path: /v1/requisitions
- description: Retrieve purchase orders.
  method: GET
  name: list-purchase-orders
  path: /v1/purchase-orders
- description: Retrieve inventory items and stock levels.
  method: GET
  name: list-inventory-items
  path: /v1/inventory-items
- description: Retrieve order fulfillment records.
  method: GET
  name: list-orders
  path: /v1/orders
- description: Retrieve pending supply chain approval requests.
  method: GET
  name: list-pending-approvals
  path: /v1/approvals
- description: Approve, deny, or push back a supply chain approval request.
  method: PUT
  name: process-approval
  path: /v1/approvals/{approvalId}
personas: []
provider_name: PeopleSoft
provider_slug: peoplesoft
search_terms:
- supply chain approval requests
- peopletools platform services.
- purchase orders
- supply chain management
- inventory items and stock levels
- supply chain
- order fulfillment
- campus solutions.
- list requisitions
- financial and supply chain management.
- financial management
- human capital management.
- retrieve inventory items and stock levels.
- order fulfillment records
- inventory
- list pending approvals
- retrieve pending supply chain approval requests.
- campus solutions
- retrieve purchase orders.
- retrieve order fulfillment records.
- crm
- erp
- retrieve procurement requisitions.
- approve, deny, or push back a supply chain approval request.
- procurement
- list purchase orders
- list inventory items
- list orders
- process approval
- individual approval operations
- procurement requisitions
- enterprise software
- hcm
- peoplesoft
slug: supply-chain-and-procurement
tags:
- PeopleSoft
- Supply Chain
- Procurement
- Inventory
- Order Fulfillment
tools:
- description: Retrieve procurement requisitions.
  hints:
    openWorld: true
    readOnly: true
  name: list-requisitions
- description: Retrieve purchase orders.
  hints:
    openWorld: true
    readOnly: true
  name: list-purchase-orders
- description: Retrieve inventory items and stock levels.
  hints:
    openWorld: true
    readOnly: true
  name: list-inventory-items
- description: Retrieve order fulfillment records.
  hints:
    openWorld: true
    readOnly: true
  name: list-orders
- description: Retrieve pending supply chain approval requests.
  hints:
    openWorld: true
    readOnly: true
  name: list-pending-approvals
- description: Approve, deny, or push back a supply chain approval request.
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: process-approval
---
