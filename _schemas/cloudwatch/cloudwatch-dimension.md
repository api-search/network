---
description: A dimension is a name/value pair that is part of the identity of a metric.
layout: schema
name: Dimension
properties_list:
- description: The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (:).
  name: Name
  type: string
- description: The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character.
  name: Value
  type: string
provider_name: AWS CloudWatch
provider_slug: cloudwatch
schema_file: json-schema/cloudwatch-dimension-schema.json
slug: cloudwatch-dimension
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
title: Dimension
---
