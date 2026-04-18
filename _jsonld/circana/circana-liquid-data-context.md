---
class_count: 16
classes:
- POSRecord
- MarketShareRecord
- ConsumerPurchaseRecord
- ConsumerSegment
- CategoryDetail
- CategorySummary
- BrandDetail
- BrandSummary
- RetailerSummary
- ReportDetail
- ExportDetail
- DataCoverage
- MarketPresence
- name
- description
- url
context_file: json-ld/circana-liquid-data-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/circana/refs/heads/main/json-ld/circana-liquid-data-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Circana Liquid Data from Circana.
layout: jsonld
name: Circana Liquid Data Context
namespaces:
- prefix: circana
  uri: https://www.circana.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: period
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: brand
  type: string
- container: ''
  name: upc
  type: string
- container: ''
  name: dollarSales
  type: double
- container: ''
  name: unitSales
  type: integer
- container: ''
  name: volumeSales
  type: double
- container: ''
  name: avgPrice
  type: double
- container: ''
  name: distributionPct
  type: double
- container: ''
  name: dollarShare
  type: double
- container: ''
  name: unitShare
  type: double
- container: ''
  name: shareChange
  type: double
- container: ''
  name: segment
  type: string
- container: ''
  name: penetrationPct
  type: double
- container: ''
  name: buyRate
  type: double
- container: ''
  name: avgSpend
  type: double
- container: ''
  name: tripsPerBuyer
  type: double
- container: ''
  name: channel
  type: string
- container: ''
  name: segmentId
  type: string
- container: ''
  name: sizePct
  type: double
- container: ''
  name: avgBasketSize
  type: double
- container: set
  name: preferredChannels
  type: string
- container: set
  name: keyCategories
  type: string
- container: ''
  name: categoryId
  type: string
- container: ''
  name: parentId
  type: string
- container: ''
  name: industry
  type: string
- container: ''
  name: level
  type: integer
- container: ''
  name: subcategoryCount
  type: integer
- container: ''
  name: brandId
  type: string
- container: ''
  name: manufacturer
  type: string
- container: ''
  name: upcCount
  type: integer
- container: set
  name: categories
  type: string
- container: ''
  name: retailerId
  type: string
- container: ''
  name: storeCount
  type: integer
- container: ''
  name: geographicCoverage
  type: string
- container: ''
  name: reportId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: reportType
  type: string
- container: ''
  name: rowCount
  type: integer
- container: ''
  name: exportId
  type: string
- container: ''
  name: format
  type: string
- container: ''
  name: downloadUrl
  type: reference
- container: ''
  name: fileSizeBytes
  type: integer
- container: ''
  name: posAvailable
  type: boolean
- container: ''
  name: panelAvailable
  type: boolean
- container: ''
  name: earliestDate
  type: date
- container: ''
  name: latestDate
  type: date
- container: ''
  name: channels
  type: integer
- container: ''
  name: retailers
  type: integer
property_count: 51
provider_name: Circana
provider_slug: circana
slug: circana-liquid-data-context
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
- JSON-LD
- Linked Data
- Semantic Web
---
