---
consumed_apis:
- acuity-brands
description: Workflow for distributor integration with Acuity Brands covering inventory lookup, order status tracking, product catalog search, and shipment tracking. Used by electrical distributors integrating Acuity Brands data into ERP and e-commerce systems.
layout: capability
name: Acuity Brands Distributor Integration
operations:
- description: List inventory with optional filters
  method: GET
  name: list-inventory
  path: /v1/inventory
- description: List orders
  method: GET
  name: list-orders
  path: /v1/orders
- description: Search product catalog
  method: GET
  name: list-catalog
  path: /v1/catalog
personas: []
provider_name: acuity-brands
provider_slug: acuity-brands
search_terms:
- search the acuity brands product catalog by keyword, brand, or product category
- electrical distributors who carry acuity brands products and need real-time inventory and order data
- commercial, industrial, and residential lighting products and controls
- distributor
- check inventory
- list inventory
- get full product details including specifications, certifications, list price, and data sheet
- get product
- list inventory with optional filters
- get detailed inventory including warehouse locations and estimated ship dates for a specific product
- check inventory availability for an acuity brands product by product number or brand
- product inventory availability
- get shipment records for an order including carrier name and pro number for freight tracking
- order status and tracking
- order management
- Electrical Distributor
- lighting
- list catalog
- b2b distributor ordering, inventory management, and shipment tracking
- developers integrating acuity brands data into erp systems for automated ordering and inventory sync
- inventory lookup, order tracking, product catalog search, and shipment tracking for distributors
- inventory
- get product inventory
- track shipment
- list recent orders filtered by status or date range
- E Commerce Developer
- get full order status and details including estimated and actual ship dates
- search product catalog
- acuity brands
- product catalog search
- search products
- b2b
- developers building e-commerce sites that display acuity brands product data, pricing, and availability
- ERP Integration Developer
- list orders
- track order
slug: distributor-integration
tags:
- Acuity Brands
- Lighting
- B2B
- Distributor
- Inventory
- Order Management
tools:
- description: Check inventory availability for an Acuity Brands product by product number or brand
  hints:
    openWorld: true
    readOnly: true
  name: check-inventory
- description: Get detailed inventory including warehouse locations and estimated ship dates for a specific product
  hints:
    openWorld: false
    readOnly: true
  name: get-product-inventory
- description: Get full order status and details including estimated and actual ship dates
  hints:
    openWorld: false
    readOnly: true
  name: track-order
- description: Get shipment records for an order including carrier name and pro number for freight tracking
  hints:
    openWorld: false
    readOnly: true
  name: track-shipment
- description: Search the Acuity Brands product catalog by keyword, brand, or product category
  hints:
    openWorld: true
    readOnly: true
  name: search-products
- description: Get full product details including specifications, certifications, list price, and data sheet
  hints:
    openWorld: false
    readOnly: true
  name: get-product
- description: List recent orders filtered by status or date range
  hints:
    openWorld: true
    readOnly: true
  name: list-orders
---
