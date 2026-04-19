---
description: Temporary changes to a sampling rule configuration. To meet the global sampling target for a rule, X-Ray calculates a new reservoir for each service based on the recent sampling results of all services that called <a href="https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html">GetSamplingTargets</a>.
layout: schema
name: SamplingTargetDocument
properties_list:
- description: ''
  name: RuleName
  type: object
- description: ''
  name: FixedRate
  type: object
- description: ''
  name: ReservoirQuota
  type: object
- description: ''
  name: ReservoirQuotaTTL
  type: object
- description: ''
  name: Interval
  type: object
provider_name: Amazon X-Ray
provider_slug: amazon-xray
schema_file: json-schema/xray-sampling-target-document-schema.json
slug: xray-sampling-target-document
tags:
- Application Performance
- AWS
- Debugging
- Distributed Tracing
- Monitoring
- Observability
title: SamplingTargetDocument
---
