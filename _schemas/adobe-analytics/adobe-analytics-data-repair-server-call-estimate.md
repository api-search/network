---
description: Estimate of server calls for a proposed data repair job
layout: schema
name: ServerCallEstimate
properties_list:
- description: The report suite ID for the estimate
  name: reportSuiteId
  type: string
- description: Start date of the repair range
  name: dateRangeStart
  type: string
- description: End date of the repair range
  name: dateRangeEnd
  type: string
- description: Estimated number of server calls (rows) that will be scanned
  name: serverCallEstimate
  type: integer
- description: Token required when creating the repair job
  name: validationToken
  type: string
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-data-repair-server-call-estimate-schema.json
slug: adobe-analytics-data-repair-server-call-estimate
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: ServerCallEstimate
---
