---
description: ''
layout: schema
name: AccessLogSettings
properties_list:
- description: A single line format of the access logs of data using CLF, JSON, XML, or CSV format.
  name: format
  type: string
- description: The Amazon Resource Name (ARN) of the CloudWatch Logs log group or Kinesis Data Firehose delivery stream.
  name: destinationArn
  type: string
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-accesslogsettings-schema.json
slug: amazon-api-gateway-accesslogsettings
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: AccessLogSettings
---
