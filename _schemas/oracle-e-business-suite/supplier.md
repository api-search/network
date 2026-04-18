---
description: Schema representing a supplier/vendor record in Oracle E-Business Suite Purchasing and Payables modules. Maps to AP_SUPPLIERS, AP_SUPPLIER_SITES_ALL, AP_SUPPLIER_CONTACTS, and the Trading Community Architecture (TCA) party model (HZ_PARTIES).
layout: schema
name: Oracle EBS Supplier
properties_list:
- description: Vendor identifier (AP_SUPPLIERS.VENDOR_ID)
  name: vendorId
  type: integer
- description: Vendor name
  name: vendorName
  type: string
- description: Vendor number
  name: segment1
  type: string
- description: Vendor type lookup code (e.g., CONTRACTOR, EMPLOYEE, VENDOR)
  name: vendorType
  type:
  - string
  - 'null'
- description: TCA party identifier (HZ_PARTIES.PARTY_ID)
  name: partyId
  type: integer
- description: Tax payer identification number (EIN/SSN/TIN)
  name: taxPayerId
  type:
  - string
  - 'null'
- description: Tax registration number (VAT number)
  name: taxRegistrationNumber
  type:
  - string
  - 'null'
- description: Standard Industry Classification (SIC) code
  name: standardIndustryClass
  type:
  - string
  - 'null'
- description: DUNS number
  name: dunsBNumber
  type:
  - string
  - 'null'
- description: One-time vendor flag
  name: oneTimeFlag
  type: string
- description: Our customer number at the vendor
  name: customerNum
  type:
  - string
  - 'null'
- description: Minority group classification
  name: minorityGroupLookupCode
  type:
  - string
  - 'null'
- description: Small business flag
  name: smallBusinessFlag
  type: string
- description: Women-owned business flag
  name: womenOwnedFlag
  type: string
- description: Default payment currency code (ISO 4217)
  name: paymentCurrencyCode
  type:
  - string
  - 'null'
- description: Default invoice currency code (ISO 4217)
  name: invoiceCurrencyCode
  type:
  - string
  - 'null'
- description: Default payment method lookup code
  name: paymentMethodCode
  type:
  - string
  - 'null'
- description: Pay group lookup code
  name: payGroupLookupCode
  type:
  - string
  - 'null'
- description: Default payment terms identifier (AP_TERMS.TERM_ID)
  name: termsId
  type:
  - integer
  - 'null'
- description: Default payment terms name
  name: termsName
  type:
  - string
  - 'null'
- description: ''
  name: alwaysTakePrepaymentDiscFlag
  type: string
- description: Pay date basis (DISCOUNT, DUE)
  name: payDateBasisLookupCode
  type:
  - string
  - 'null'
- description: Invoice amount limit
  name: invoiceAmountLimit
  type:
  - number
  - 'null'
- description: Whether all payments are on hold
  name: holdAllPaymentsFlag
  type: string
- description: Whether unmatched invoices are on hold
  name: holdUnmatchedInvoicesFlag
  type: string
- description: Invoice match option
  name: matchOption
  type:
  - string
  - 'null'
- description: Whether the vendor is currently active/enabled
  name: enabled
  type: boolean
- description: Date the vendor becomes active
  name: startDateActive
  type: string
- description: Date the vendor becomes inactive
  name: endDateActive
  type:
  - string
  - 'null'
- description: Vendor site records
  name: sites
  type: array
- description: Vendor contact records
  name: contacts
  type: array
- description: Vendor bank account assignments
  name: bankAccounts
  type: array
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
schema_file: json-schema/supplier.json
slug: supplier
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Oracle EBS Supplier
---
