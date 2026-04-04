---
aid: microsoft-graph:microsoft-graph-contracts
name: Microsoft Graph Contracts
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/contracts-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Contracts is a read-only API in Microsoft Graph that lets
  Microsoft 365 partners (such as CSP/resellers) discover and list the customer
  tenants they have a relationship with. It returns each customers key directory
  identifiers and metadatalike tenant (customer) ID, default domain name,
  display name, and the relationship/contract typeso partner apps can enumerate
  customers, scope operations per tenant, and obtain tokens targeted at the
  right directory. The relationship itself is established and managed in Partner
  Center (not via the API). For newer, granular delegated admin scenarios,
  partners typically also use the
  tenantRelationships/delegatedAdminRelationships APIs alongside Contracts.

---