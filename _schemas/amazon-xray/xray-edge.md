---
description: Information about a connection between two services. An edge can be a synchronous connection, such as typical call between client and service, or an asynchronous link, such as a Lambda function which retrieves an event from an SNS queue.
layout: schema
name: Edge
properties_list:
- description: ''
  name: ReferenceId
  type: object
- description: ''
  name: StartTime
  type: object
- description: ''
  name: EndTime
  type: object
- description: ''
  name: SummaryStatistics
  type: object
- description: ''
  name: ResponseTimeHistogram
  type: object
- description: ''
  name: Aliases
  type: object
- description: ''
  name: EdgeType
  type: object
- description: ''
  name: ReceivedEventAgeHistogram
  type: object
provider_name: Amazon X-Ray
provider_slug: amazon-xray
schema_file: json-schema/xray-edge-schema.json
slug: xray-edge
tags:
- Application Performance
- AWS
- Debugging
- Distributed Tracing
- Monitoring
- Observability
title: Edge
---
