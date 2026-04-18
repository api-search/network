---
description: ''
layout: schema
name: UntagResourceInput
properties_list:
- description: The ARN of the CloudWatch resource that you're removing tags from.
  name: ResourceARN
  type: string
- description: The list of tag keys to remove from the resource.
  name: TagKeys
  type: array
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-untag-resource-input-schema.json
slug: cloudwatch-untag-resource-input
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: UntagResourceInput
---
