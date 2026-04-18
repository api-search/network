---
class_count: 49
classes:
- Application
- AppSummary
- AppDetails
- UsageEvent
- SpendData
- ProvisionedUser
- OrgChartUser
- ProvisioningWorkflow
- AuditEvent
- appId
- ApplicationId
- AppName
- AppStatus
- VendorName
- AppCategory
- email
- firstName
- lastName
- role
- department
- title
- managerEmail
- eventName
- eventType
- eventId
- userEmail
- amount
- currency
- date
- description
- workflowId
- workflowName
- applicationId
- status
- executionId
- startTime
- endTime
- totalUsers
- activeUsers
- lastActivityDate
- totalSpend
- totalValue
- contractId
- startDate
- endDate
- instanceId
- instanceName
- suggestedOutcome
- actionedOutcome
context_file: json-ld/productiv-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/productiv/refs/heads/main/json-ld/productiv-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Productiv from Productiv.
layout: jsonld
name: Productiv Context
namespaces:
- prefix: productiv
  uri: https://public-api.productiv.com/schema/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: appName
  type: string
- container: ''
  name: appDescription
  type: string
- container: ''
  name: appCategory
  type: string
- container: ''
  name: appUrl
  type: reference
- container: ''
  name: timestamp
  type: dateTime
property_count: 5
provider_name: Productiv
provider_slug: productiv
slug: productiv-context
tags:
- Application Portfolio
- Provisioning
- SaaS Management
- Spend Management
- Usage Analytics
- JSON-LD
- Linked Data
- Semantic Web
---
