---
consumed_apis:
- liquid-data
description: Unified market intelligence workflow combining POS data, market share analytics, consumer panel insights, brand performance, and reporting capabilities for brand managers, category managers, and market researchers.
layout: capability
name: Circana Market Intelligence
operations:
- description: Retrieve POS data by category and time period
  method: GET
  name: get-pos-data
  path: /v1/pos-data
- description: Retrieve market share data
  method: GET
  name: get-market-share
  path: /v1/market-share
- description: Retrieve consumer purchase data
  method: GET
  name: get-consumer-purchases
  path: /v1/consumer-purchases
- description: Retrieve consumer segments
  method: GET
  name: get-consumer-segments
  path: /v1/consumer-segments
- description: List product categories
  method: GET
  name: list-categories
  path: /v1/categories
- description: List brands in a category
  method: GET
  name: list-brands
  path: /v1/brands
- description: List retailers
  method: GET
  name: list-retailers
  path: /v1/retailers
- description: List reports
  method: GET
  name: list-reports
  path: /v1/reports
- description: Create a new report
  method: POST
  name: create-report
  path: /v1/reports
- description: Create a data export
  method: POST
  name: create-export
  path: /v1/exports
personas: []
provider_name: Circana
provider_slug: circana
search_terms:
- list reports
- get pos data
- retail
- retrieve pos data by category and time period
- create export
- create a data export
- Brand Manager
- market intelligence
- retailer coverage data
- analytics
- consumer purchase behavior data
- retrieve aggregated consumer purchase data from panel surveys
- business intelligence
- monitors retailer performance, distribution, and channel dynamics
- get report status and details
- data export
- point-of-sale data access
- manages brand performance, market share, and competitive positioning
- get report
- consumer insights
- get detailed brand information including market presence
- brand analytics
- Category Manager
- retrieve market share data for brands in a product category
- categories, brands, and retailers
- consumer data
- cpg
- retrieve market share data
- circana
- product category taxonomy
- list brands
- list retailers
- manages product category performance, assortment, and shopper insights
- list brands in a category
- retrieve consumer purchase data
- report management
- list product categories
- get market share
- get brand
- get detailed information about a specific product category
- consumer segmentation data
- consumer panel data, purchase behavior, and segmentation
- check data export status and get download url
- list categories
- list available analytics reports
- get consumer segments
- retrieve consumer segmentation data based on purchase behavior
- get category
- pos data, market share, and sales performance analytics
- list brands within a specific product category
- report generation, management, and data export
- point of sale
- get consumer purchases
- market research
- retrieve consumer segments
- market share analytics
- create report
- create a new report
- retrieve point-of-sale data for a product category and time period
- list retailers covered in circana measurement universe
- create a new analytics report for a category and time period
- create a data export job in csv, excel, json, or parquet format
- get export
- analyzes consumer behavior, market trends, and competitive dynamics
- list all available product categories in circana taxonomy
- unified market intelligence combining pos, share, consumer, and reporting data
slug: market-intelligence
tags:
- Circana
- Market Intelligence
- Analytics
- Consumer Insights
- Retail
tools:
- description: Retrieve point-of-sale data for a product category and time period
  hints:
    openWorld: true
    readOnly: true
  name: get-pos-data
- description: Retrieve market share data for brands in a product category
  hints:
    openWorld: true
    readOnly: true
  name: get-market-share
- description: Retrieve aggregated consumer purchase data from panel surveys
  hints:
    openWorld: true
    readOnly: true
  name: get-consumer-purchases
- description: Retrieve consumer segmentation data based on purchase behavior
  hints:
    openWorld: true
    readOnly: true
  name: get-consumer-segments
- description: List all available product categories in Circana taxonomy
  hints:
    openWorld: true
    readOnly: true
  name: list-categories
- description: Get detailed information about a specific product category
  hints:
    openWorld: true
    readOnly: true
  name: get-category
- description: List brands within a specific product category
  hints:
    openWorld: true
    readOnly: true
  name: list-brands
- description: Get detailed brand information including market presence
  hints:
    openWorld: true
    readOnly: true
  name: get-brand
- description: List retailers covered in Circana measurement universe
  hints:
    openWorld: true
    readOnly: true
  name: list-retailers
- description: List available analytics reports
  hints:
    openWorld: true
    readOnly: true
  name: list-reports
- description: Create a new analytics report for a category and time period
  hints:
    readOnly: false
  name: create-report
- description: Get report status and details
  hints:
    openWorld: true
    readOnly: true
  name: get-report
- description: Create a data export job in CSV, Excel, JSON, or Parquet format
  hints:
    readOnly: false
  name: create-export
- description: Check data export status and get download URL
  hints:
    openWorld: true
    readOnly: true
  name: get-export
---
