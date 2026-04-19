---
description: Complete supplier profile on the SAP Ariba Network including company information, classifications, and qualification details
layout: schema
name: Supplier
properties_list:
- description: Unique supplier identifier (AN-ID)
  name: supplierId
  type: string
- description: Legal company name
  name: name
  type: string
- description: Trade name or DBA name
  name: doingBusinessAs
  type: string
- description: Dun and Bradstreet DUNS number
  name: dunsNumber
  type: string
- description: Tax identification number
  name: taxId
  type: string
- description: Year the company was established
  name: yearEstablished
  type: integer
- description: Employee count range
  name: numberOfEmployees
  type: string
- description: Registration status on the Ariba Network
  name: registrationStatus
  type: string
- description: UNSPSC commodity codes the supplier serves
  name: commodityCodes
  type: array
- description: Supplier certifications and compliance credentials
  name: certifications
  type: array
- description: Supplier diversity classifications
  name: diversityClassifications
  type: array
- description: Company website URL
  name: website
  type: string
- description: Company description
  name: description
  type: string
- description: Date the supplier profile was created
  name: createdDate
  type: string
- description: Date of last profile update
  name: lastModifiedDate
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-supplier-schema.json
slug: sap-ariba-procurement-supplier
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: Supplier
---
