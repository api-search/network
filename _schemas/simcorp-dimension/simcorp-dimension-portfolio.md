---
description: Schema for a portfolio entity in the SimCorp Integration Model (SIM). Portfolios represent investment portfolios managed within SimCorp Dimension, supporting multi-asset class holdings across the Investment Book of Record (IBOR). Based on the SimCorp Dimension data model documented at thesim.dev and simcorp.com.
layout: schema
name: SimCorp Dimension Portfolio
properties_list:
- description: Unique internal identifier for the portfolio within SimCorp Dimension
  name: portfolioId
  type: integer
- description: Short alphanumeric code uniquely identifying the portfolio
  name: portfolioCode
  type: string
- description: Full descriptive name of the portfolio
  name: portfolioName
  type: string
- description: Classification of the portfolio by its operational role
  name: portfolioType
  type: string
- description: Current lifecycle status of the portfolio
  name: portfolioStatus
  type: string
- description: ISO 4217 currency code for the portfolio base currency used for valuation and reporting
  name: baseCurrency
  type: string
- description: Date the portfolio was established and began tracking positions
  name: inceptionDate
  type: string
- description: Date the portfolio was closed or terminated, null if still active
  name: terminationDate
  type:
  - string
  - 'null'
- description: The legal entity or organization that owns the portfolio
  name: legalEntity
  type: string
- description: Name or identifier of the portfolio manager or management team responsible
  name: investmentManager
  type: string
- description: The custodian bank or institution holding the portfolio assets
  name: custodian
  type: string
- description: The benchmark portfolio or index used for performance comparison
  name: benchmark
  type: object
- description: Description of the investment strategy or mandate governing the portfolio
  name: investmentStrategy
  type: string
- description: Asset classes that the portfolio is authorized to hold
  name: assetClasses
  type: array
- description: Hierarchical structure placing this portfolio within a portfolio tree or organizational grouping
  name: portfolioHierarchy
  type: object
- description: Current holdings or positions within the portfolio from the Investment Book of Record (IBOR)
  name: positions
  type: array
- description: Investment compliance rules and constraints applied to the portfolio
  name: complianceRules
  type: array
- description: Summary valuation data for the portfolio as of the last valuation date
  name: valuationSummary
  type: object
- description: The accounting method used for the portfolio in the Accounting Book of Record (ABOR)
  name: accountingMethod
  type: string
- description: Currency used for client reporting if different from base currency
  name: reportingCurrency
  type: string
- description: User-defined and system classification attributes for the portfolio
  name: classifications
  type: object
- description: User-defined custom fields extending the standard portfolio attributes
  name: customProperties
  type: object
- description: Timestamp when the portfolio record was created in SimCorp Dimension
  name: createdDate
  type: string
- description: Timestamp when the portfolio record was last modified
  name: modifiedDate
  type: string
provider_name: SimCorp Dimension
provider_slug: simcorp-dimension
schema_file: json-schema/simcorp-dimension-portfolio-schema.json
slug: simcorp-dimension-portfolio
tags:
- Accounting
- Asset Management
- Compliance
- Data Distribution
- Enterprise Software
- Financial Data
- Financial Technology
- Investment Management
- Portfolio Management
- Risk Management
- SimCorp One
- Streaming
- Trading
title: SimCorp Dimension Portfolio
---
