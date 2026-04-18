---
description: A resource (such as a host or service) associated with a metric series
layout: schema
name: MetricResource
properties_list:
- description: The name of the resource (e.g., hostname or service name)
  name: name
  type: string
- description: The type of the resource (e.g., host, service, container)
  name: type
  type: string
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-metrics-metric-resource-schema.json
slug: datadog-metrics-metric-resource
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MetricResource
---
