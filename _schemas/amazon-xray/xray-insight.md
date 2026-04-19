---
description: When fault rates go outside of the expected range, X-Ray creates an insight. Insights tracks emergent issues within your applications.
layout: schema
name: Insight
properties_list:
- description: ''
  name: InsightId
  type: object
- description: ''
  name: GroupARN
  type: object
- description: ''
  name: GroupName
  type: object
- description: ''
  name: RootCauseServiceId
  type: object
- description: ''
  name: Categories
  type: object
- description: ''
  name: State
  type: object
- description: ''
  name: StartTime
  type: object
- description: ''
  name: EndTime
  type: object
- description: ''
  name: Summary
  type: object
- description: ''
  name: ClientRequestImpactStatistics
  type: object
- description: ''
  name: RootCauseServiceRequestImpactStatistics
  type: object
- description: ''
  name: TopAnomalousServices
  type: object
provider_name: Amazon X-Ray
provider_slug: amazon-xray
schema_file: json-schema/xray-insight-schema.json
slug: xray-insight
tags:
- Application Performance
- AWS
- Debugging
- Distributed Tracing
- Monitoring
- Observability
title: Insight
---
