---
description: Request sampling results for a single rule from a service. Results are for the last 10 seconds unless the service has been assigned a longer reporting interval after a previous call to <a href="https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html">GetSamplingTargets</a>.
layout: schema
name: SamplingStatisticsDocument
properties_list:
- description: ''
  name: RuleName
  type: object
- description: ''
  name: ClientID
  type: object
- description: ''
  name: Timestamp
  type: object
- description: ''
  name: RequestCount
  type: object
- description: ''
  name: SampledCount
  type: object
- description: ''
  name: BorrowCount
  type: object
provider_name: Amazon X-Ray
provider_slug: amazon-xray
schema_file: json-schema/xray-sampling-statistics-document-schema.json
slug: xray-sampling-statistics-document
tags:
- Application Performance
- AWS
- Debugging
- Distributed Tracing
- Monitoring
- Observability
title: SamplingStatisticsDocument
---
