---
description: A filter object specifying a dimension and its accepted values for cost data queries.
layout: schema
name: Filter
properties_list:
- description: The dimension to filter by (e.g., service, region, account, team).
  name: filter_by
  type: string
- description: The list of values to include for the specified filter dimension.
  name: values
  type: array
provider_name: Amnic
provider_slug: amnic
schema_file: json-schema/amnic-api-filter-schema.json
slug: amnic-api-filter
tags:
- Cloud Cost Observability
- FinOps
- Cloud Cost Management
- Cost Optimization
- Kubernetes
- AWS
- Azure
- Google Cloud
title: Filter
---
