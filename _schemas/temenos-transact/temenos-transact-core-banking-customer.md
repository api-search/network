---
description: A customer record in Temenos Transact representing an individual or corporate entity with a banking relationship.
layout: schema
name: Customer
properties_list:
- description: Unique system-generated customer identifier
  name: customerId
  type: string
- description: Short alphanumeric code identifying the customer (3-10 characters, first character alphabetic)
  name: customerMnemonic
  type: string
- description: Short name of the customer (3-35 characters, uppercase)
  name: shortName
  type: string
- description: Full name entries for the customer
  name: customerNames
  type: array
- description: Display name entries for the customer
  name: displayNames
  type: array
- description: Customer title
  name: title
  type: string
- description: Customer gender
  name: gender
  type: string
- description: Customer date of birth
  name: dateOfBirth
  type: string
- description: Nationality code
  name: nationalityId
  type: string
- description: Country of residence code
  name: residenceId
  type: string
- description: Preferred language code
  name: language
  type: integer
- description: Customer status code (1 = active)
  name: customerStatus
  type: integer
- description: Customer sector classification (1-4 digits)
  name: sectorId
  type: integer
- description: Industry classification code
  name: industryId
  type: integer
- description: Assigned account officer identifier
  name: accountOfficerId
  type: integer
- description: Target market segment
  name: target
  type: integer
- description: Contact communication devices (phone, email)
  name: communicationDevices
  type: array
- description: Customer address records
  name: addresses
  type: array
- description: Company identifier the customer belongs to
  name: customerCompany
  type: string
- description: AML verification check status
  name: amlCheck
  type: string
- description: AML verification result
  name: amlResult
  type: string
- description: KYC compliance status
  name: kycStatus
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-customer-schema.json
slug: temenos-transact-core-banking-customer
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Customer
---
