---
description: A paginated collection of metric descriptors returned by the list metrics endpoint.
layout: schema
name: MetricDescriptorCollection
properties_list:
- description: The cursor for the next page of results. Include this value as the nextPageKey query parameter in the next request. Null if there are no more results.
  name: nextPageKey
  type: string
- description: The total number of metrics available matching the query.
  name: totalCount
  type: integer
- description: The resolution of the data if applicable.
  name: resolution
  type: string
- description: The list of metric descriptors on this page.
  name: metrics
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/metrics-api-v2-metric-descriptor-collection-schema.json
slug: metrics-api-v2-metric-descriptor-collection
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: MetricDescriptorCollection
---
