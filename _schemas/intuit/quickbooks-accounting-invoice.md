---
description: An Invoice represents a sales form where the customer pays for a product or service later. It creates an accounts receivable transaction.
layout: schema
name: Invoice
properties_list:
- description: Unique identifier for the invoice (assigned by QuickBooks)
  name: Id
  type: string
- description: Version number of the entity, used for optimistic locking. Required for updates.
  name: SyncToken
  type: string
- description: Reference number for the transaction. If not provided, QuickBooks auto-generates one.
  name: DocNumber
  type: string
- description: The date of the transaction. Defaults to the current date.
  name: TxnDate
  type: string
- description: Date when the payment of the transaction is due
  name: DueDate
  type: string
- description: A private note that is not displayed to the customer
  name: PrivateNote
  type: string
- description: A note to the customer displayed on the invoice
  name: CustomerMemo
  type: object
- description: Individual line items of the transaction. At least one line is required.
  name: Line
  type: array
- description: Total amount of the transaction including tax
  name: TotalAmt
  type: number
- description: The balance remaining on the invoice. A value of 0 indicates the invoice is fully paid.
  name: Balance
  type: number
- description: Deposit amount applied to the invoice
  name: Deposit
  type: number
- description: Currency exchange rate (multicurrency enabled companies)
  name: ExchangeRate
  type: number
- description: Date for delivery of goods or services
  name: ShipDate
  type: string
- description: Shipping tracking number
  name: TrackingNum
  type: string
- description: Whether to apply tax after discount
  name: ApplyTaxAfterDiscount
  type: boolean
- description: Printing status of the invoice
  name: PrintStatus
  type: string
- description: Email delivery status of the invoice
  name: EmailStatus
  type: string
- description: Method in which tax is applied
  name: GlobalTaxCalculation
  type: string
- description: Whether online payment is allowed
  name: AllowOnlinePayment
  type: boolean
- description: Whether online credit card payment is allowed
  name: AllowOnlineCreditCardPayment
  type: boolean
- description: Whether online ACH (bank) payment is allowed
  name: AllowOnlineACHPayment
  type: boolean
- description: ''
  name: CustomField
  type: array
- description: ''
  name: LinkedTxn
  type: array
- description: Domain (e.g., QBO)
  name: domain
  type: string
- description: Whether this is a sparse (partial) representation
  name: sparse
  type: boolean
provider_name: Intuit
provider_slug: intuit
schema_file: json-schema/quickbooks-accounting-invoice-schema.json
slug: quickbooks-accounting-invoice
tags:
- Accounting
- Custom Fields
- Financial
- Financial Services
- Invoicing
- Payments
- Payroll
- Project Management
- Sales Tax
- Small Business
- Tax
- Tax Preparation
- Taxes
- Time Tracking
title: Invoice
---
