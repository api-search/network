---
aid: microsoft-graph:microsoft-graph-data-policy-operations
name: Microsoft Graph Data Policy Operations
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/datapolicyoperations-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Data Policy Operations is the mechanism Microsoft Graph uses
  to represent and track long-running, privacy- and compliance-related tasks,
  most commonly exporting a users personal data. When you start an action like
  exportPersonalData, Graph creates a dataPolicyOperation resource that you can
  poll to monitor status and progress, inspect errors, and, when finished,
  obtain the storage location link to download the results. You can also list
  operations across the tenant to monitor and audit requests. This enables
  organizations to automate subject-rights workflows (such as GDPR/CCPA data
  export) across Microsoft 365 services through a consistent, asynchronous API.

---