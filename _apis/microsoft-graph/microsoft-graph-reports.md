---
aid: microsoft-graph:microsoft-graph-reports
name: Microsoft Graph Reports
tags:
  - Tag
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://developer.github.com/
properties:
  - url: https://developer.github.com/
    type: Documentation
  - url: properties/reports-openapi-original.yml
    type: OpenAPI
description: >-
  Microsoft Graph Reports is the reporting surface of Microsoft 365 exposed via
  Microsoft Graph, enabling administrators to programmatically retrieve usage,
  adoption, and certain identity and print analytics across their tenant.
  Through the /reports endpoints, you can pull tenant- and user-level metrics
  for services like Teams, SharePoint, OneDrive, Exchange, Yammer/Viva Engage,
  Microsoft 365 Apps, and Universal Printcovering activity (active users,
  messages, meetings, file actions), storage and mailbox usage, app activations,
  and device usageas well as Azure AD registration and MFA usage details.
  Reports are available for defined periods (for example, the last 7, 30, 90, or
  180 days) and can be exported for automation and BI workflows, typically as
  CSV and, for some endpoints, as JSON. With the appropriate permissions (such
  as Reports.Read.All), you can schedule extractions, integrate them with other
  Graph data, and build dashboards to track adoption, capacity, and trends.

---