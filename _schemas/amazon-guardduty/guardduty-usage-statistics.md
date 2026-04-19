---
description: Contains the result of GuardDuty usage. If a UsageStatisticType is provided the result for other types will be null.
layout: schema
name: UsageStatistics
properties_list:
- description: ''
  name: SumByAccount
  type: object
- description: ''
  name: SumByDataSource
  type: object
- description: ''
  name: SumByResource
  type: object
- description: ''
  name: TopResources
  type: object
- description: ''
  name: SumByFeature
  type: object
provider_name: Amazon GuardDuty
provider_slug: amazon-guardduty
schema_file: json-schema/guardduty-usage-statistics-schema.json
slug: guardduty-usage-statistics
tags:
- Anomaly Detection
- AWS
- Compliance
- Machine Learning
- Monitoring
- Security
- Threat Detection
title: UsageStatistics
---
