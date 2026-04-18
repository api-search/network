---
description: A RHEL system registered with Red Hat Insights for monitoring and recommendations.
layout: schema
name: System
properties_list:
- description: The unique identifier of the system.
  name: system_uuid
  type: string
- description: The display name of the system.
  name: display_name
  type: string
- description: The last time the system checked in with Insights.
  name: last_seen
  type: string
- description: The date when the system will be considered stale.
  name: stale_at
  type: string
- description: The number of active Advisor recommendations.
  name: hits
  type: integer
- description: The number of critical severity recommendations.
  name: critical_hits
  type: integer
- description: The number of important severity recommendations.
  name: important_hits
  type: integer
- description: The number of moderate severity recommendations.
  name: moderate_hits
  type: integer
- description: The number of low severity recommendations.
  name: low_hits
  type: integer
- description: The RHEL version running on the system.
  name: rhel_version
  type: string
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-insights-system-schema.json
slug: red-hat-insights-system
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: System
---
