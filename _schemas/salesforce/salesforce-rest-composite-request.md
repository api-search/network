---
description: A composite request containing an ordered series of subrequests where later requests can reference the results of earlier ones using reference IDs.
layout: schema
name: CompositeRequest
properties_list:
- description: If true, all subrequests must succeed or all changes are rolled back. If false, subrequests are processed independently.
  name: allOrNone
  type: boolean
- description: If true, similar subrequests are grouped for more efficient processing.
  name: collateSubrequests
  type: boolean
- description: Ordered array of subrequests. Later subrequests can reference results from earlier ones using @{referenceId.field} syntax.
  name: compositeRequest
  type: array
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-rest-composite-request-schema.json
slug: salesforce-rest-composite-request
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
title: CompositeRequest
---
