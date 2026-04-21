---
consumed_apis:
- amazon-service-catalog
description: Unified capability for IT service governance including portfolio management, product catalog curation, and self-service product provisioning. Used by IT Administrators and End Users.
layout: capability
name: Amazon Service Catalog IT Service Governance
operations:
- description: List all IT service portfolios
  method: GET
  name: list-portfolios
  path: /v1/portfolios
- description: Create an IT service portfolio
  method: POST
  name: create-portfolio
  path: /v1/portfolios
- description: Browse approved products
  method: GET
  name: search-products
  path: /v1/products
- description: Add a product to the catalog
  method: POST
  name: create-product
  path: /v1/products
- description: Provision an approved product
  method: POST
  name: provision-product
  path: /v1/provisioned-products
personas: []
provider_name: Amazon Service Catalog
provider_slug: amazon-service-catalog
search_terms:
- self-service provision an approved it product
- list all it service catalog portfolios
- compliance
- list portfolios
- create product
- describe portfolio
- provision product
- terminate and decommission a provisioned product
- service catalog
- self-service product provisioning
- create an it service portfolio
- provision an approved product
- get details about an it service portfolio
- amazon service catalog
- check the status of a provisioned product
- it service portfolio management
- add a new product to the it service catalog
- browse and search approved it products
- create portfolio
- browse approved products
- cloud governance
- approved product catalog
- it governance
- self-service
- list all it service portfolios
- aws
- describe provisioned product
- terminate provisioned product
- add a product to the catalog
- search products
- create a new it service catalog portfolio
slug: it-service-governance
tags:
- Amazon Service Catalog
- IT Governance
- Cloud Governance
- Self-Service
- Compliance
tools:
- description: List all IT service catalog portfolios
  hints:
    idempotent: true
    readOnly: true
  name: list-portfolios
- description: Create a new IT service catalog portfolio
  hints:
    idempotent: false
    readOnly: false
  name: create-portfolio
- description: Get details about an IT service portfolio
  hints:
    idempotent: true
    readOnly: true
  name: describe-portfolio
- description: Browse and search approved IT products
  hints:
    idempotent: true
    readOnly: true
  name: search-products
- description: Add a new product to the IT service catalog
  hints:
    idempotent: false
    readOnly: false
  name: create-product
- description: Self-service provision an approved IT product
  hints:
    idempotent: false
    readOnly: false
  name: provision-product
- description: Check the status of a provisioned product
  hints:
    idempotent: true
    readOnly: true
  name: describe-provisioned-product
- description: Terminate and decommission a provisioned product
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: terminate-provisioned-product
---
