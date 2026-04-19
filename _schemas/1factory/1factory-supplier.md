---
description: Supplier schema from 1Factory API
layout: schema
name: Supplier
properties_list:
- description: ''
  name: ID
  type: object
- description: ''
  name: name
  type: object
- description: ''
  name: vendor_code
  type: object
- description: ''
  name: address
  type: object
- description: ''
  name: supply_chain_manager
  type: object
- description: ''
  name: supplier_quality_manager
  type: object
- description: ''
  name: purchasing
  type: object
- description: Indicates if the supplier provides direct materials or services.
  name: direct
  type: boolean
- description: Indicates if the supplier provides indirect materials or services.
  name: indirect
  type: boolean
- description: Indicates if the supplier is considered strategic to the organization.
  name: strategic
  type: boolean
- description: Indicates if the supplier is classified as a small business.
  name: small_business
  type: boolean
- description: List of organization codes associated with the supplier.
  name: organization_codes
  type: array
- description: List of commodity codes that the supplier provides.
  name: commodity_codes
  type: array
- description: List of supplier qualifications and their status history.
  name: qualifications
  type: array
- description: List of supplier certifications and their expiration dates.
  name: certifications
  type: array
- description: Current qualification status derived from the most recent qualification entry.
  name: qualification_status
  type: string
- description: Date and time of the most recent qualification assessment.
  name: last_qualification_date
  type: string
- description: Calculated date when the supplier needs to be re-qualified, based on the last qualification date plus frequency in months.
  name: re_qualification_date
  type: string
provider_name: 1Factory
provider_slug: 1factory
schema_file: json-schema/1factory-supplier-schema.json
slug: 1factory-supplier
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
title: Supplier
---
