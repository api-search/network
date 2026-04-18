---
description: Schema representing an Accounts Payable invoice in Oracle E-Business Suite. Maps to AP_INVOICES_ALL and AP_INVOICE_LINES_ALL tables. Covers standard invoices, credit memos, debit memos, and prepayments.
layout: schema
name: Oracle EBS Invoice
properties_list:
- description: Unique identifier for the invoice (AP_INVOICES_ALL.INVOICE_ID)
  name: invoiceId
  type: integer
- description: Supplier invoice number (AP_INVOICES_ALL.INVOICE_NUM)
  name: invoiceNum
  type: string
- description: Invoice date
  name: invoiceDate
  type: string
- description: Date the invoice was received
  name: invoiceReceivedDate
  type:
  - string
  - 'null'
- description: Invoice type lookup code
  name: invoiceType
  type: string
- description: Supplier/vendor identifier (AP_SUPPLIERS.VENDOR_ID)
  name: vendorId
  type: integer
- description: Supplier/vendor name
  name: vendorName
  type: string
- description: Vendor number
  name: vendorNum
  type: string
- description: Vendor site identifier (AP_SUPPLIER_SITES_ALL.VENDOR_SITE_ID)
  name: vendorSiteId
  type: integer
- description: Vendor site code
  name: vendorSiteCode
  type: string
- description: Total invoice amount in invoice currency
  name: invoiceAmount
  type: number
- description: Invoice currency code (ISO 4217)
  name: invoiceCurrencyCode
  type: string
- description: Payment currency code (ISO 4217)
  name: paymentCurrencyCode
  type: string
- description: Currency exchange rate
  name: exchangeRate
  type:
  - number
  - 'null'
- description: Exchange rate type (Corporate, Spot, User)
  name: exchangeRateType
  type:
  - string
  - 'null'
- description: Exchange rate date
  name: exchangeDate
  type:
  - string
  - 'null'
- description: Invoice amount in functional/base currency
  name: baseAmount
  type:
  - number
  - 'null'
- description: Payment terms identifier (AP_TERMS.TERM_ID)
  name: termsId
  type: integer
- description: Payment terms name
  name: termsName
  type: string
- description: Payment terms date
  name: termsDate
  type:
  - string
  - 'null'
- description: Invoice description
  name: description
  type:
  - string
  - 'null'
- description: Invoice source (Manual, EDI, ERS, etc.)
  name: source
  type: string
- description: 'Payment status: Y=Fully Paid, N=Not Paid, P=Partially Paid'
  name: paymentStatusFlag
  type: string
- description: Payment method lookup code
  name: paymentMethodCode
  type:
  - string
  - 'null'
- description: Approval status
  name: approvalStatus
  type: string
- description: Workflow approval status
  name: wfapprovalStatus
  type:
  - string
  - 'null'
- description: Total amount paid against this invoice
  name: amountPaid
  type: number
- description: Total discount amount taken
  name: discountAmountTaken
  type:
  - number
  - 'null'
- description: Amount applicable to discount
  name: amountApplicableToDiscount
  type:
  - number
  - 'null'
- description: Total tax amount
  name: taxAmount
  type:
  - number
  - 'null'
- description: Matched purchase order header ID
  name: poHeaderId
  type:
  - integer
  - 'null'
- description: Date goods were received
  name: goodsReceivedDate
  type:
  - string
  - 'null'
- description: General Ledger accounting date
  name: glDate
  type: string
- description: Pay group
  name: payGroupLookupCode
  type:
  - string
  - 'null'
- description: Date the invoice was cancelled
  name: cancelledDate
  type:
  - string
  - 'null'
- description: Cancelled amount
  name: cancelledAmount
  type:
  - number
  - 'null'
- description: Invoice lines
  name: lines
  type: array
- description: Payment records associated with this invoice
  name: payments
  type: array
- description: Active holds on this invoice
  name: holds
  type: array
- description: Operating unit identifier
  name: orgId
  type: integer
- description: User who created the record
  name: createdBy
  type: integer
- description: Record creation date
  name: creationDate
  type: string
- description: User who last updated the record
  name: lastUpdatedBy
  type: integer
- description: Record last update date
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/invoice.json
slug: invoice
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Oracle EBS Invoice
---
