---
consumed_apis:
- quickbooks-accounting
description: Unified workflow for small business accounting automation combining QuickBooks Online invoice, customer, item, and payment management. Used by accountants, bookkeepers, and business owners to automate financial workflows.
layout: capability
name: Intuit Accounting and Payments
operations:
- description: Create a new invoice.
  method: POST
  name: create-invoice
  path: /v1/invoices
- description: Retrieve an invoice by ID.
  method: GET
  name: read-invoice
  path: /v1/invoices/{invoiceId}
- description: Email an invoice to the customer.
  method: POST
  name: send-invoice
  path: /v1/invoices/{invoiceId}/send
- description: Void an existing invoice.
  method: POST
  name: void-invoice
  path: /v1/invoices/{invoiceId}/void
- description: Retrieve invoice as PDF.
  method: GET
  name: get-invoice-pdf
  path: /v1/invoices/{invoiceId}/pdf
- description: Create a new customer.
  method: POST
  name: create-customer
  path: /v1/customers
- description: Retrieve a customer by ID.
  method: GET
  name: read-customer
  path: /v1/customers/{customerId}
- description: Create a new item.
  method: POST
  name: create-item
  path: /v1/items
- description: Retrieve an item by ID.
  method: GET
  name: read-item
  path: /v1/items/{itemId}
- description: Record a new payment.
  method: POST
  name: create-payment
  path: /v1/payments
- description: Retrieve a payment by ID.
  method: GET
  name: read-payment
  path: /v1/payments/{paymentId}
- description: Query QuickBooks entities.
  method: GET
  name: query-entities
  path: /v1/query
personas: []
provider_name: Intuit
provider_slug: intuit
search_terms:
- single customer operations.
- retrieve invoice as pdf.
- send a quickbooks invoice via email.
- read payment
- update a quickbooks customer record.
- create customer
- customer management.
- retrieve a quickbooks invoice by id.
- void payment
- create a new customer.
- get invoice pdf.
- single invoice operations.
- create a new invoice.
- void a quickbooks invoice.
- product and service catalog.
- retrieve a payment by id.
- create a new quickbooks invoice.
- create a new item.
- create payment
- update an existing quickbooks invoice.
- small business
- record a customer payment in quickbooks.
- void a quickbooks payment.
- financial services
- read item
- query entities
- get pdf of a quickbooks invoice.
- query quickbooks entities using sql-like syntax.
- payroll
- send invoice
- taxes
- sales tax
- custom fields
- invoice lifecycle management.
- update an existing quickbooks payment.
- financial
- update an existing quickbooks item.
- get invoice pdf
- payments
- record a new payment.
- tax preparation
- create invoice
- accounting
- retrieve an item by id.
- retrieve a quickbooks payment by id.
- retrieve an invoice by id.
- query quickbooks entities.
- intuit
- create a new customer in quickbooks.
- create a new product or service item.
- time tracking
- email an invoice to the customer.
- entity query endpoint.
- retrieve a quickbooks customer by id.
- update invoice
- single item operations.
- retrieve a quickbooks item by id.
- read customer
- tax
- create item
- update item
- send an invoice via email.
- payment management.
- void an invoice.
- read invoice
- retrieve a customer by id.
- single payment operations.
- project management
- void an existing invoice.
- update payment
- void invoice
- invoicing
- update customer
slug: accounting-and-payments
tags:
- Intuit
- Accounting
- Invoicing
- Payments
- Small Business
tools:
- description: Create a new QuickBooks invoice.
  hints:
    readOnly: false
  name: create-invoice
- description: Retrieve a QuickBooks invoice by ID.
  hints:
    idempotent: true
    readOnly: true
  name: read-invoice
- description: Update an existing QuickBooks invoice.
  hints:
    idempotent: true
    readOnly: false
  name: update-invoice
- description: Send a QuickBooks invoice via email.
  hints:
    readOnly: false
  name: send-invoice
- description: Void a QuickBooks invoice.
  hints:
    destructive: true
    readOnly: false
  name: void-invoice
- description: Get PDF of a QuickBooks invoice.
  hints:
    idempotent: true
    readOnly: true
  name: get-invoice-pdf
- description: Query QuickBooks entities using SQL-like syntax.
  hints:
    idempotent: true
    openWorld: true
    readOnly: true
  name: query-entities
- description: Create a new customer in QuickBooks.
  hints:
    readOnly: false
  name: create-customer
- description: Retrieve a QuickBooks customer by ID.
  hints:
    idempotent: true
    readOnly: true
  name: read-customer
- description: Update a QuickBooks customer record.
  hints:
    idempotent: true
    readOnly: false
  name: update-customer
- description: Create a new product or service item.
  hints:
    readOnly: false
  name: create-item
- description: Retrieve a QuickBooks item by ID.
  hints:
    idempotent: true
    readOnly: true
  name: read-item
- description: Update an existing QuickBooks item.
  hints:
    idempotent: true
    readOnly: false
  name: update-item
- description: Record a customer payment in QuickBooks.
  hints:
    readOnly: false
  name: create-payment
- description: Retrieve a QuickBooks payment by ID.
  hints:
    idempotent: true
    readOnly: true
  name: read-payment
- description: Update an existing QuickBooks payment.
  hints:
    idempotent: true
    readOnly: false
  name: update-payment
- description: Void a QuickBooks payment.
  hints:
    destructive: true
    readOnly: false
  name: void-payment
---
