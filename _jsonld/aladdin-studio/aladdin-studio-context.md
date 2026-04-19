---
class_count: 18
classes:
- Security
- SecurityResearch
- Order
- Dataset
- PortfolioRisk
- OrderList
- OrderRequest
- PortfolioAnalytics
- QueryRequest
- Position
- PositionList
- QueryResult
- Portfolio
- FactorExposure
- ConnectionList
- PortfolioList
- DatasetList
- Connection
context_file: json-ld/aladdin-studio-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/aladdin-studio/refs/heads/main/json-ld/aladdin-studio-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Aladdin Studio from Aladdin Studio.
layout: jsonld
name: Aladdin Studio Context
namespaces:
- prefix: aladdin
  uri: https://blackrock.com/aladdin/schema/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: schema
  type: string
- container: ''
  name: accountName
  type: string
- container: ''
  name: analystCount
  type: integer
- container: ''
  name: asOfDate
  type: date
- container: ''
  name: assetClass
  type: string
- container: ''
  name: averagePrice
  type: decimal
- container: ''
  name: benchmarkId
  type: string
- container: ''
  name: beta
  type: decimal
- container: set
  name: columns
  type: string
- container: ''
  name: connectionId
  type: string
- container: set
  name: connections
  type: string
- container: ''
  name: consensusDate
  type: date
- container: ''
  name: contribution
  type: decimal
- container: ''
  name: country
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: currency
  type: string
- container: ''
  name: cusip
  type: string
- container: ''
  name: database
  type: string
- container: ''
  name: datasetId
  type: string
- container: set
  name: datasets
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: excessReturn
  type: decimal
- container: ''
  name: exchange
  type: string
- container: ''
  name: exposure
  type: decimal
- container: set
  name: factorExposures
  type: string
- container: ''
  name: factorName
  type: string
- container: ''
  name: filledAt
  type: dateTime
- container: ''
  name: filledQuantity
  type: decimal
- container: ''
  name: fromDate
  type: date
- container: ''
  name: inceptionDate
  type: date
- container: ''
  name: informationRatio
  type: decimal
- container: ''
  name: isin
  type: string
- container: ''
  name: lastUpdated
  type: dateTime
- container: ''
  name: limitPrice
  type: decimal
- container: ''
  name: marketValue
  type: decimal
- container: ''
  name: maxRows
  type: integer
- container: ''
  name: name
  type: string
- container: ''
  name: orderId
  type: string
- container: ''
  name: orderType
  type: string
- container: set
  name: orders
  type: string
- container: ''
  name: page
  type: integer
- container: ''
  name: pageSize
  type: integer
- container: ''
  name: portfolioId
  type: string
- container: set
  name: portfolios
  type: string
- container: set
  name: positions
  type: string
- container: ''
  name: priceTarget
  type: decimal
- container: ''
  name: quantity
  type: decimal
- container: ''
  name: queryId
  type: string
- container: ''
  name: rating
  type: string
- container: ''
  name: riskModel
  type: string
- container: ''
  name: rowCount
  type: integer
- container: set
  name: rows
  type: string
- container: ''
  name: sector
  type: string
- container: ''
  name: securityId
  type: string
- container: ''
  name: securityName
  type: string
- container: ''
  name: sharpeRatio
  type: decimal
- container: ''
  name: side
  type: string
- container: ''
  name: sql
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: strategy
  type: string
- container: ''
  name: ticker
  type: string
- container: ''
  name: timeout
  type: integer
- container: ''
  name: toDate
  type: date
- container: ''
  name: totalCount
  type: integer
- container: ''
  name: totalMarketValue
  type: decimal
- container: ''
  name: totalReturn
  type: decimal
- container: ''
  name: trackingError
  type: decimal
- container: ''
  name: type
  type: string
- container: ''
  name: var95
  type: decimal
- container: ''
  name: volatility
  type: decimal
- container: ''
  name: warehouse
  type: string
- container: ''
  name: weight
  type: decimal
property_count: 72
provider_name: Aladdin Studio
provider_slug: aladdin-studio
slug: aladdin-studio-context
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
- JSON-LD
- Linked Data
- Semantic Web
---
