---
description: ''
layout: schema
name: CompanyEnrichment
properties_list:
- description: Unique identifier for the company record.
  name: id
  type: string
- description: Company name.
  name: name
  type: '[''string'', ''null'']'
- description: Legal name of the company.
  name: legalName
  type: '[''string'', ''null'']'
- description: Company domain name.
  name: domain
  type: string
- description: Alternate domain names.
  name: domainAliases
  type: array
- description: ''
  name: site
  type: object
- description: Industry classification.
  name: category
  type: object
- description: Tags associated with the company.
  name: tags
  type: array
- description: Company description.
  name: description
  type: '[''string'', ''null'']'
- description: Year the company was founded.
  name: foundedYear
  type: '[''integer'', ''null'']'
- description: Location description.
  name: location
  type: '[''string'', ''null'']'
- description: Time zone name.
  name: timeZone
  type: '[''string'', ''null'']'
- description: UTC offset in hours.
  name: utcOffset
  type: '[''number'', ''null'']'
- description: Company logo URL.
  name: logo
  type: '[''string'', ''null'']'
- description: ''
  name: facebook
  type: object
- description: ''
  name: linkedin
  type: object
- description: ''
  name: twitter
  type: object
- description: ''
  name: crunchbase
  type: object
- description: Email service provider.
  name: emailProvider
  type: '[''string'', ''null'']'
- description: Company type.
  name: type
  type: '[''string'', ''null'']'
- description: Entity type classification.
  name: company_type
  type: '[''string'', ''null'']'
- description: Stock ticker symbol.
  name: ticker
  type: '[''string'', ''null'']'
- description: ''
  name: identifiers
  type: object
- description: Primary phone number.
  name: phone
  type: '[''string'', ''null'']'
- description: ''
  name: metrics
  type: object
- description: Date when the record was last indexed.
  name: indexedAt
  type: '[''string'', ''null'']'
- description: Technologies used by the company.
  name: tech
  type: array
- description: Categories of technologies used.
  name: techCategories
  type: array
- description: ''
  name: parent
  type: object
- description: ''
  name: ultimateParent
  type: object
provider_name: Hunter
provider_slug: hunter
schema_file: json-schema/hunter-company-enrichment-schema.json
slug: hunter-company-enrichment
tags:
- Contact Discovery
- Email
- Email Verification
- Lead Generation
- Prospecting
- Sales Intelligence
title: CompanyEnrichment
---
