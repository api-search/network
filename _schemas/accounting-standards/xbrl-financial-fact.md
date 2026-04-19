---
description: A single XBRL financial fact from an SEC EDGAR filing, representing one tagged data point from a company's financial statements.
layout: schema
name: XbrlFinancialFact
properties_list:
- description: The SEC Central Index Key (CIK) of the filing entity, zero-padded to 10 digits
  name: cik
  type: string
- description: The XBRL taxonomy namespace prefix used for this fact
  name: taxonomy
  type: string
- description: The XBRL taxonomy element (tag) name for this fact
  name: concept
  type: string
- description: Human-readable label for the concept
  name: label
  type: string
- description: Definition of the taxonomy concept
  name: description
  type: string
- description: Legal name of the filing entity
  name: entityName
  type: string
- description: Array of unit groupings for this fact
  name: units
  type: array
provider_name: Accounting Standards
provider_slug: accounting-standards
schema_file: json-schema/xbrl-financial-fact-schema.json
slug: xbrl-financial-fact
tags:
- Accounting Standards
- Finance
- GAAP
- IFRS
- XBRL
- Financial Reporting
- SEC
- FASB
title: XbrlFinancialFact
---
