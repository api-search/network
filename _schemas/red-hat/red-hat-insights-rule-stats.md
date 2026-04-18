---
description: Aggregate statistics about Advisor rules.
layout: schema
name: RuleStats
properties_list:
- description: The total number of active rules.
  name: total
  type: integer
- description: Rule counts by category.
  name: by_category
  type: object
- description: Rule counts by total risk severity.
  name: by_severity
  type: object
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-insights-rule-stats-schema.json
slug: red-hat-insights-rule-stats
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: RuleStats
---
