---
description: Schema representing an AWS X-Ray trace resource for distributed tracing.
layout: schema
name: AWS X-Ray Trace
properties_list:
- description: The unique identifier for the request trace.
  name: Id
  type: string
- description: The length of time in seconds between the start and end of the trace.
  name: Duration
  type: number
- description: Whether the trace exceeded the segment document size limit.
  name: LimitExceeded
  type: boolean
- description: The segment documents associated with the trace.
  name: Segments
  type: array
provider_name: Amazon X-Ray
provider_slug: amazon-xray
schema_file: json-schema/amazon-xray-trace-schema.json
slug: amazon-xray-trace
tags:
- Application Performance
- AWS
- Debugging
- Distributed Tracing
- Monitoring
- Observability
title: AWS X-Ray Trace
---
