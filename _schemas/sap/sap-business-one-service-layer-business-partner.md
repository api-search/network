---
description: ''
layout: schema
name: BusinessPartner
properties_list:
- description: Unique identifier for the business partner
  name: CardCode
  type: string
- description: Name of the business partner
  name: CardName
  type: string
- description: Type of business partner
  name: CardType
  type: string
- description: Business partner group code
  name: GroupCode
  type: integer
- description: Primary phone number
  name: Phone1
  type: string
- description: Email address
  name: EmailAddress
  type: string
- description: Tax identification number
  name: FederalTaxID
  type: string
- description: Default currency code
  name: Currency
  type: string
- description: Whether the business partner is active
  name: Valid
  type: string
provider_name: SAP
provider_slug: sap
schema_file: json-schema/sap-business-one-service-layer-business-partner-schema.json
slug: sap-business-one-service-layer-business-partner
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
title: BusinessPartner
---
