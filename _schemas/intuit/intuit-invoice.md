---
description: An Invoice represents a sales form where the customer pays for a product or service later. QuickBooks Online records an accounts receivable transaction for each invoice. This schema describes the full Invoice entity as returned by the QuickBooks Online Accounting API.
layout: schema
name: QuickBooks Online Invoice
properties_list:
- description: Unique identifier for the invoice, assigned by QuickBooks Online.
  name: Id
  type: string
- description: Version number of the entity used for optimistic concurrency control. Required for update operations. The value changes each time the entity is updated.
  name: SyncToken
  type: string
- description: ''
  name: MetaData
  type: object
- description: Reference number for the transaction. If not provided during creation, QuickBooks auto-generates a sequential number.
  name: DocNumber
  type: string
- description: The date of the transaction in YYYY-MM-DD format. Defaults to the current date if not specified.
  name: TxnDate
  type: string
- description: The date when payment is due. Calculated based on the sales terms if not explicitly set.
  name: DueDate
  type: string
- description: A private note for internal use that is not displayed to the customer.
  name: PrivateNote
  type: string
- description: A note to the customer that appears on the invoice.
  name: CustomerMemo
  type: object
- description: Reference to the customer associated with this invoice. Required for creation.
  name: CustomerRef
  type: object
- description: Bill-to address for the invoice.
  name: BillAddr
  type: object
- description: Ship-to address for the invoice.
  name: ShipAddr
  type: object
- description: Email address to which the invoice is sent.
  name: BillEmail
  type: object
- description: Individual line items of the transaction. At least one line item with a valid DetailType is required.
  name: Line
  type: array
- description: Tax details for the entire invoice transaction.
  name: TxnTaxDetail
  type: object
- description: Total amount of the transaction including tax. This is a calculated field and is read-only.
  name: TotalAmt
  type: number
- description: The balance remaining to be paid on the invoice. A value of 0 indicates the invoice is fully paid.
  name: Balance
  type: number
- description: Deposit amount previously applied to this invoice.
  name: Deposit
  type: number
- description: Account where the deposit was made.
  name: DepositToAccountRef
  type: object
- description: Reference to the sales term (e.g., Net 30, Due on Receipt).
  name: SalesTermRef
  type: object
- description: Reference to the payment method for this invoice.
  name: PaymentMethodRef
  type: object
- description: Reference to the currency used for this invoice. Only applicable for companies with multicurrency enabled.
  name: CurrencyRef
  type: object
- description: The exchange rate between the invoice currency and the home currency. Only applicable for multicurrency companies.
  name: ExchangeRate
  type: number
- description: Date for delivery of goods or services.
  name: ShipDate
  type: string
- description: Reference to the shipping method.
  name: ShipMethodRef
  type: object
- description: Shipping tracking number.
  name: TrackingNum
  type: string
- description: If true, tax is calculated after applying any discount. If false, tax is calculated before the discount.
  name: ApplyTaxAfterDiscount
  type: boolean
- description: Printing status of the invoice.
  name: PrintStatus
  type: string
- description: Email delivery status of the invoice.
  name: EmailStatus
  type: string
- description: Method in which tax is applied. TaxExcluded means line amounts are exclusive of tax. TaxInclusive means line amounts include tax.
  name: GlobalTaxCalculation
  type: string
- description: Whether online payment is allowed for this invoice.
  name: AllowOnlinePayment
  type: boolean
- description: Whether online credit card payment is allowed.
  name: AllowOnlineCreditCardPayment
  type: boolean
- description: Whether online ACH (bank transfer) payment is allowed.
  name: AllowOnlineACHPayment
  type: boolean
- description: Custom fields defined for the invoice. A maximum of 3 custom fields are supported.
  name: CustomField
  type: array
- description: Transactions linked to this invoice such as payments or credit memos.
  name: LinkedTxn
  type: array
- description: Domain of the entity (e.g., QBO).
  name: domain
  type: string
- description: Indicates whether this is a sparse (partial) representation of the entity.
  name: sparse
  type: boolean
provider_name: Intuit
provider_slug: intuit
schema_file: json-schema/intuit-invoice-schema.json
slug: intuit-invoice
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
title: QuickBooks Online Invoice
---
