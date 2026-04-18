---
description: Aggregate statistics about registered systems.
layout: schema
name: SystemStats
properties_list:
- description: The total number of registered systems.
  name: total
  type: integer
- description: The number of stale systems.
  name: stale
  type: integer
- description: Systems with at least one active recommendation.
  name: with_hits
  type: integer
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-insights-system-stats-schema.json
slug: red-hat-insights-system-stats
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: SystemStats
---
