---
consumed_apis:
- business-central-v2
description: Unified workflow for day-to-day business operations in Dynamics 365 Business Central combining the Business Central API v2.0 for managing customers, vendors, items, orders, invoices, and financials. Used by accountants, sales teams, and operations managers.
layout: capability
name: Dynamics NAV Business Operations
operations:
- description: List available companies
  method: GET
  name: list-companies
  path: /v1/companies
- description: List all customers
  method: GET
  name: list-customers
  path: /v1/customers
- description: Create a customer
  method: POST
  name: create-customer
  path: /v1/customers
- description: Get a customer
  method: GET
  name: get-customer
  path: /v1/customers/{customer_id}
- description: List all vendors
  method: GET
  name: list-vendors
  path: /v1/vendors
- description: List all items
  method: GET
  name: list-items
  path: /v1/items
- description: List sales orders
  method: GET
  name: list-sales-orders
  path: /v1/sales-orders
- description: Create a sales order
  method: POST
  name: create-sales-order
  path: /v1/sales-orders
- description: List purchase orders
  method: GET
  name: list-purchase-orders
  path: /v1/purchase-orders
- description: List accounts
  method: GET
  name: list-accounts
  path: /v1/accounts
- description: List journals
  method: GET
  name: list-journals
  path: /v1/journals
- description: List sales invoices
  method: GET
  name: list-sales-invoices
  path: /v1/sales-invoices
personas: []
provider_name: Microsoft Dynamics NAV
provider_slug: navision
search_terms:
- erp
- purchase orders
- finance
- list purchase invoices
- list available companies
- microsoft
- create a new customer
- navision
- list all sales orders
- sales
- list sales invoices
- inventory items
- list inventory items
- list employees
- create a new inventory item
- list companies
- sales invoices
- list accounts
- create purchase order
- general ledger accounts
- create a new sales order
- get a customer
- general journals
- single customer
- create vendor
- create a new vendor
- create sales order
- inventory
- list purchase orders
- list all customers
- create a customer
- list items
- sales orders
- get a customer by id
- create customer
- business management
- list general journals
- create a sales order
- list all vendors
- list sales orders
- list customers
- list all items
- list journals
- list all employees
- dynamics 365
- create a new purchase order
- business central
- purchasing
- list vendors
- create item
- list all purchase orders
- customer management
- vendor management
- list general ledger accounts
- company information
- dynamics nav
- get customer
slug: business-operations
tags:
- Business Central
- Dynamics 365
- ERP
- Finance
- Sales
- Purchasing
tools:
- description: List available companies
  hints:
    idempotent: true
    readOnly: true
  name: list-companies
- description: List all customers
  hints:
    idempotent: true
    readOnly: true
  name: list-customers
- description: Create a new customer
  hints:
    readOnly: false
  name: create-customer
- description: Get a customer by ID
  hints:
    idempotent: true
    readOnly: true
  name: get-customer
- description: List all vendors
  hints:
    idempotent: true
    readOnly: true
  name: list-vendors
- description: Create a new vendor
  hints:
    readOnly: false
  name: create-vendor
- description: List inventory items
  hints:
    idempotent: true
    readOnly: true
  name: list-items
- description: Create a new inventory item
  hints:
    readOnly: false
  name: create-item
- description: List all sales orders
  hints:
    idempotent: true
    readOnly: true
  name: list-sales-orders
- description: Create a new sales order
  hints:
    readOnly: false
  name: create-sales-order
- description: List all purchase orders
  hints:
    idempotent: true
    readOnly: true
  name: list-purchase-orders
- description: Create a new purchase order
  hints:
    readOnly: false
  name: create-purchase-order
- description: List general ledger accounts
  hints:
    idempotent: true
    readOnly: true
  name: list-accounts
- description: List general journals
  hints:
    idempotent: true
    readOnly: true
  name: list-journals
- description: List sales invoices
  hints:
    idempotent: true
    readOnly: true
  name: list-sales-invoices
- description: List purchase invoices
  hints:
    idempotent: true
    readOnly: true
  name: list-purchase-invoices
- description: List all employees
  hints:
    idempotent: true
    readOnly: true
  name: list-employees
---
