---
description: Response containing a paginated list of incidents
layout: schema
name: IncidentsResponse
properties_list:
- description: List of incident objects
  name: data
  type: array
- description: Related resources included in the response based on the include query parameter
  name: included
  type: array
- description: Metadata about the incidents list response
  name: meta
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-incidents-incidents-response-schema.json
slug: datadog-incidents-incidents-response
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: IncidentsResponse
---
