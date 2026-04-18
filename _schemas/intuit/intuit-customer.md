---
description: A Customer represents a consumer of the service or product that the business offers. The Customer entity supports a hierarchy where customers can have sub-customers (jobs) organized under a parent customer. DisplayName must be unique across all Customer, Employee, and Vendor objects within a QuickBooks Online company.
layout: schema
name: QuickBooks Online Customer
properties_list:
- description: Unique identifier for the customer, assigned by QuickBooks Online.
  name: Id
  type: string
- description: Version number of the entity used for optimistic concurrency control. Required for update operations.
  name: SyncToken
  type: string
- description: ''
  name: MetaData
  type: object
- description: Title of the person (e.g., Mr., Mrs., Ms., Dr.).
  name: Title
  type: string
- description: Given (first) name of the customer.
  name: GivenName
  type: string
- description: Middle name of the customer.
  name: MiddleName
  type: string
- description: Family (last) name of the customer.
  name: FamilyName
  type: string
- description: Suffix of the person (e.g., Jr., Sr., III).
  name: Suffix
  type: string
- description: The name displayed to identify the customer in the QuickBooks UI and on transaction forms. Must be unique across all Customer, Employee, and Vendor objects.
  name: DisplayName
  type: string
- description: The company name associated with the customer.
  name: CompanyName
  type: string
- description: Name to print on checks issued to this customer.
  name: PrintOnCheckName
  type: string
- description: Whether the customer is currently active. Inactive customers do not appear in transaction drop-downs but their data is retained.
  name: Active
  type: boolean
- description: Whether transactions for this customer are taxable.
  name: Taxable
  type: boolean
- description: Primary email address for the customer.
  name: PrimaryEmailAddr
  type: object
- description: Primary phone number.
  name: PrimaryPhone
  type: object
- description: Mobile phone number.
  name: Mobile
  type: object
- description: Fax number.
  name: Fax
  type: object
- description: Alternate phone number.
  name: AlternatePhone
  type: object
- description: Default billing address for the customer.
  name: BillAddr
  type: object
- description: Default shipping address for the customer.
  name: ShipAddr
  type: object
- description: Free-form text notes about the customer.
  name: Notes
  type: string
- description: Whether this customer represents a job (sub-customer) rather than a top-level customer.
  name: Job
  type: boolean
- description: Reference to the parent customer if this is a sub-customer (job).
  name: ParentRef
  type: object
- description: Depth level in the customer hierarchy. 0 indicates a top-level customer.
  name: Level
  type: integer
- description: Fully qualified name of the customer including all parent names separated by colons (e.g., 'ParentCustomer:SubCustomer').
  name: FullyQualifiedName
  type: string
- description: Reference to the currency used by this customer. Only applicable for companies with multicurrency enabled.
  name: CurrencyRef
  type: object
- description: Preferred method for delivering communications to this customer.
  name: PreferredDeliveryMethod
  type: string
- description: Open balance amount for the customer (sum of all open invoices minus payments).
  name: Balance
  type: number
- description: Open balance amount including balances of all sub-customers (jobs).
  name: BalanceWithJobs
  type: number
- description: Default sales terms for transactions with this customer.
  name: SalesTermRef
  type: object
- description: Default payment method for this customer.
  name: PaymentMethodRef
  type: object
- description: The tax exemption reason identifier if the customer is tax-exempt.
  name: TaxExemptionReasonId
  type: string
- description: The customer's website address.
  name: WebAddr
  type: object
- description: Whether this customer is a project (QuickBooks Online Plus and Advanced only).
  name: IsProject
  type: boolean
- description: Source of the customer record.
  name: Source
  type: string
- description: Primary tax identifier for the customer (e.g., ABN in Australia, GSTIN in India).
  name: PrimaryTaxIdentifier
  type: string
- description: GST registration type (applicable for India and Australia editions).
  name: GSTRegistrationType
  type: string
- description: Business number of the customer (used in certain international editions).
  name: BusinessNumber
  type: string
- description: GST Identification Number (India edition).
  name: GSTIN
  type: string
- description: Domain of the entity (e.g., QBO).
  name: domain
  type: string
- description: Indicates whether this is a sparse (partial) representation of the entity.
  name: sparse
  type: boolean
provider_name: Intuit
provider_slug: intuit
schema_file: json-schema/intuit-customer-schema.json
slug: intuit-customer
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
title: QuickBooks Online Customer
---
