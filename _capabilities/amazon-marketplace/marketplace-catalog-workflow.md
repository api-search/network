---
consumed_apis:
- marketplace-catalog
description: Workflow capability for ISV sellers and marketplace operators to publish, update, and manage software products and offers on AWS Marketplace using the Catalog API.
layout: capability
name: Amazon Marketplace - Catalog Management Workflow
operations:
- description: List entities available in the marketplace catalog.
  method: POST
  name: list-entities
  path: /v1/entities
- description: Get details of a specific marketplace entity.
  method: GET
  name: describe-entity
  path: /v1/entities
- description: List change sets in the marketplace catalog.
  method: POST
  name: list-change-sets
  path: /v1/change-sets
- description: Get details of a specific change set.
  method: GET
  name: describe-change-set
  path: /v1/change-sets
- description: Start a change set to publish or update a marketplace entity.
  method: POST
  name: start-change-set
  path: /v1/publish
personas: []
provider_name: Amazon Marketplace
provider_slug: amazon-marketplace
search_terms:
- manage change sets for publishing and updating marketplace entities.
- list change sets
- retrieve the resource-based policy attached to a marketplace entity.
- commerce
- manage marketplace entities (products, offers).
- get details of a specific change set.
- platform operator managing marketplace listings, policies, and change sets at scale.
- marketplace
- managing resource policies for marketplace entities.
- describe marketplace entity
- get the status and details of a specific marketplace change set.
- describe entity
- get detailed information about a specific aws marketplace entity including its attributes and status.
- software catalog
- get resource policy
- publish and update marketplace listings.
- list change sets in the marketplace catalog.
- start change set
- aws
- list marketplace entities
- amazon
- workflow for isv sellers to publish, update, and manage products on aws marketplace.
- list entities available in the marketplace catalog.
- publishing and updating software products and offers on aws marketplace.
- isv
- list software products, offers, and data products available in the aws marketplace catalog.
- cancel change set
- list change sets for tracking publishing and update operations on marketplace entities.
- ISV Seller
- start a change set to publish or update a marketplace entity.
- Marketplace Operator
- independent software vendor publishing and managing products on aws marketplace.
- list entities
- describe change set
- cancel an active change set that has not yet completed.
- initiate a change set to publish a new product or update an existing marketplace listing.
- get details of a specific marketplace entity.
slug: marketplace-catalog-workflow
tags:
- Amazon
- Marketplace
- Commerce
- Software Catalog
- ISV
tools:
- description: List software products, offers, and data products available in the AWS Marketplace catalog.
  hints:
    openWorld: true
    readOnly: true
  name: list-marketplace-entities
- description: Get detailed information about a specific AWS Marketplace entity including its attributes and status.
  hints:
    readOnly: true
  name: describe-marketplace-entity
- description: List change sets for tracking publishing and update operations on marketplace entities.
  hints:
    readOnly: true
  name: list-change-sets
- description: Get the status and details of a specific marketplace change set.
  hints:
    readOnly: true
  name: describe-change-set
- description: Initiate a change set to publish a new product or update an existing marketplace listing.
  hints:
    readOnly: false
  name: start-change-set
- description: Cancel an active change set that has not yet completed.
  hints:
    destructive: false
    readOnly: false
  name: cancel-change-set
- description: Retrieve the resource-based policy attached to a marketplace entity.
  hints:
    readOnly: true
  name: get-resource-policy
---
