---
description: Schema for a financial instrument entity in the SimCorp Integration Model (SIM). Instruments represent securities and financial products managed within SimCorp Dimension, covering equities, fixed income, derivatives, alternatives, funds, and structured products. Each instrument entity can have well over 100 data fields. Based on the SimCorp Dimension data model documented at thesim.dev and simcorp.com.
layout: schema
name: SimCorp Dimension Instrument
properties_list:
- description: Unique internal identifier for the instrument within SimCorp Dimension
  name: instrumentId
  type: integer
- description: Short alphanumeric code uniquely identifying the instrument in the system
  name: instrumentCode
  type: string
- description: Full descriptive name of the instrument
  name: instrumentName
  type: string
- description: Primary classification of the instrument by asset type
  name: instrumentType
  type: string
- description: Current lifecycle status of the instrument
  name: instrumentStatus
  type: string
- description: Broad asset class categorization
  name: assetClass
  type: string
- description: Standard market identifiers for the instrument
  name: identifiers
  type: object
- description: ISO 4217 currency code of the instrument denomination
  name: currency
  type: string
- description: ISO 3166-1 alpha-2 country code of the instrument domicile or issuer country
  name: country
  type: string
- description: Information about the entity that issued the instrument
  name: issuer
  type: object
- description: Primary exchange or trading venue information
  name: exchange
  type: object
- description: Additional attributes specific to equity instruments (common shares, preferred shares, depository receipts)
  name: equityDetails
  type: object
- description: Additional attributes specific to fixed income instruments (bonds, notes, bills)
  name: fixedIncomeDetails
  type: object
- description: Additional attributes specific to derivative instruments, managed through the XpressInstruments module in SimCorp Dimension
  name: derivativeDetails
  type: object
- description: Additional attributes specific to fund instruments (mutual funds, ETFs, hedge funds)
  name: fundDetails
  type: object
- description: Current and historical pricing data
  name: pricing
  type: object
- description: Credit ratings from recognized rating agencies
  name: ratings
  type: array
- description: Classification codes and categories applied to the instrument for grouping, filtering, and regulatory reporting
  name: classifications
  type: object
- description: Environmental, Social, and Governance data associated with the instrument
  name: esgData
  type: object
- description: Standard settlement information for the instrument
  name: settlementDetails
  type: object
- description: User-defined custom fields extending the standard instrument attributes. SimCorp Dimension supports extensive user-defined fields for custom calculations and classifications.
  name: customProperties
  type: object
- description: Timestamp when the instrument record was created in SimCorp Dimension
  name: createdDate
  type: string
- description: Timestamp when the instrument record was last modified
  name: modifiedDate
  type: string
provider_name: SimCorp Dimension
provider_slug: simcorp-dimension
schema_file: json-schema/simcorp-dimension-instrument-schema.json
slug: simcorp-dimension-instrument
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
title: SimCorp Dimension Instrument
---
