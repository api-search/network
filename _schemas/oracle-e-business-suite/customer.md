---
description: Schema representing a customer record in Oracle E-Business Suite Trading Community Architecture (TCA). Maps to HZ_PARTIES, HZ_CUST_ACCOUNTS, HZ_PARTY_SITES, HZ_CUST_ACCT_SITES_ALL, and HZ_CUST_SITE_USES_ALL tables. TCA provides a unified model for managing customer, supplier, and partner data.
layout: schema
name: Oracle EBS Customer
properties_list:
- description: Party identifier (HZ_PARTIES.PARTY_ID)
  name: partyId
  type: integer
- description: Party number (system-generated unique identifier)
  name: partyNumber
  type: string
- description: Party name (organization name or person full name)
  name: partyName
  type: string
- description: Party type
  name: partyType
  type: string
- description: Customer category code
  name: category
  type:
  - string
  - 'null'
- description: Party status
  name: status
  type: string
- description: Organization profile (when partyType is ORGANIZATION)
  name: organizationProfile
  type: object
- description: Person profile (when partyType is PERSON)
  name: personProfile
  type: object
- description: Customer accounts associated with this party
  name: customerAccounts
  type: array
- description: Party site/address records
  name: partySites
  type: array
- description: Contact points (phone, email, web, etc.)
  name: contactPoints
  type: array
- description: Party relationships (contacts, hierarchies)
  name: relationships
  type: array
- description: DUNS number
  name: dunsBNumber
  type:
  - string
  - 'null'
- description: Tax identification number
  name: taxPayerIdentificationNumber
  type:
  - string
  - 'null'
- description: Fiscal code (localization)
  name: jgzzFiscalCode
  type:
  - string
  - 'null'
- description: Website URL
  name: url
  type:
  - string
  - 'null'
- description: Primary email address
  name: emailAddress
  type:
  - string
  - 'null'
- description: Primary phone number
  name: primaryPhoneNumber
  type:
  - string
  - 'null'
- description: ''
  name: createdBy
  type: integer
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdatedBy
  type: integer
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/customer.json
slug: customer
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Oracle EBS Customer
---
