---
description: Company entity metadata and recent filing history from the SEC EDGAR Submissions API.
layout: schema
name: EdgarCompanySubmission
properties_list:
- description: Central Index Key — unique 10-digit identifier assigned by the SEC
  name: cik
  type: string
- description: Type of entity registered with the SEC
  name: entityType
  type: string
- description: Standard Industrial Classification code
  name: sic
  type: string
- description: Description of the SIC code industry
  name: sicDescription
  type: string
- description: Current legal name of the entity
  name: name
  type: string
- description: Stock ticker symbols for the entity
  name: tickers
  type: array
- description: Stock exchanges where the entity is listed
  name: exchanges
  type: array
- description: US state code or country of incorporation
  name: stateOfIncorporation
  type: string
- description: Month and day of fiscal year end (MMDD)
  name: fiscalYearEnd
  type: string
- description: Official website of the entity
  name: website
  type: string
- description: Recent filing history
  name: filings
  type: object
provider_name: Accounting Standards
provider_slug: accounting-standards
schema_file: json-schema/edgar-company-submission-schema.json
slug: edgar-company-submission
tags:
- Accounting Standards
- Finance
- GAAP
- IFRS
- XBRL
- Financial Reporting
- SEC
- FASB
title: EdgarCompanySubmission
---
