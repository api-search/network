---
aid: microsoft-graph:microsoft-graph-subscribed-skus
name: Microsoft Graph Subscribed SKUs
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/subscribedskus-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Subscribed SKUs is the API/resource that lists the Microsoft
  365/Azure AD license subscriptions your tenant owns. When you call GET
  /subscribedSkus, it returns each license plan (SKU) with its identifiers
  (skuId, skuPartNumber), seat counts (prepaidUnits and consumedUnits),
  subscription status (enabled, suspended, warning), and the included service
  plans. This lets apps and admins inventory licenses, map SKU IDs to
  human-readable plans, check capacity before assigning licenses, spot suspended
  or trial subscriptions, and build usage or compliance reports. In practice,
  you read subscribed SKUs to choose the right skuId, then use Graphs license
  assignment endpoints to add or remove that license for users or groups.

---