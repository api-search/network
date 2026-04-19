---
description: A sampling rule that services use to decide whether to instrument a request. Rule fields can match properties of the service, or properties of a request. The service can ignore rules that don't match its properties.
layout: schema
name: SamplingRule
properties_list:
- description: ''
  name: RuleName
  type: object
- description: ''
  name: RuleARN
  type: object
- description: ''
  name: ResourceARN
  type: object
- description: ''
  name: Priority
  type: object
- description: ''
  name: FixedRate
  type: object
- description: ''
  name: ReservoirSize
  type: object
- description: ''
  name: ServiceName
  type: object
- description: ''
  name: ServiceType
  type: object
- description: ''
  name: Host
  type: object
- description: ''
  name: HTTPMethod
  type: object
- description: ''
  name: URLPath
  type: object
- description: ''
  name: Version
  type: object
- description: ''
  name: Attributes
  type: object
provider_name: Amazon X-Ray
provider_slug: amazon-xray
schema_file: json-schema/xray-sampling-rule-schema.json
slug: xray-sampling-rule
tags:
- Application Performance
- AWS
- Debugging
- Distributed Tracing
- Monitoring
- Observability
title: SamplingRule
---
