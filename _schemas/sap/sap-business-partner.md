---
description: Schema for SAP business partner master data used across S/4HANA, Business One, and SuccessFactors APIs.
layout: schema
name: SAP Business Partner
properties_list:
- description: Unique business partner number
  name: BusinessPartner
  type: string
- description: 'Category of the business partner: 1=Organization, 2=Person, 3=Group'
  name: BusinessPartnerCategory
  type: string
- description: Full name of the business partner
  name: BusinessPartnerFullName
  type: string
- description: Business partner grouping for number range assignment
  name: BusinessPartnerGrouping
  type: string
- description: First name for person-type business partners
  name: FirstName
  type: string
- description: Last name for person-type business partners
  name: LastName
  type: string
- description: Organization name (line 1) for organization-type business partners
  name: OrganizationBPName1
  type: string
- description: Organization name (line 2)
  name: OrganizationBPName2
  type: string
- description: Primary search term
  name: SearchTerm1
  type: string
- description: Correspondence language (ISO 639-1)
  name: Language
  type: string
- description: Industry sector key
  name: Industry
  type: string
- description: Legal form of the organization
  name: LegalForm
  type: string
- description: Date the business partner record was created
  name: CreationDate
  type: string
- description: Date of last modification
  name: LastChangeDate
  type: string
- description: Whether the business partner is a natural person
  name: IsNaturalPerson
  type: string
- description: Business partner addresses
  name: Addresses
  type: array
- description: Business partner bank account details
  name: BankAccounts
  type: array
- description: Tax identification numbers
  name: TaxNumbers
  type: array
- description: Business partner roles (customer, supplier, etc.)
  name: Roles
  type: array
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-business-partner-schema.json
slug: sap-business-partner
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: SAP Business Partner
---
