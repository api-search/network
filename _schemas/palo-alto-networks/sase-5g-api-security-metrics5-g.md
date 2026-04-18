---
description: SecurityMetrics5G schema from Palo Alto Networks SASE 5G Managed Services API
layout: schema
name: SecurityMetrics5G
properties_list:
- description: ''
  name: period
  type: object
- description: Total 5G sessions inspected during the period.
  name: total_sessions
  type: integer
- description: Number of threats detected in 5G traffic.
  name: threats_detected
  type: integer
- description: Number of threats blocked.
  name: threats_blocked
  type: integer
- description: Total bytes of 5G traffic inspected.
  name: bytes_inspected
  type: integer
- description: Number of active 5G subscribers.
  name: active_subscribers
  type: integer
- description: Metrics broken down by network slice.
  name: per_slice_metrics
  type: array
- description: Time-series data points for the metrics period.
  name: time_series
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-5g-api-security-metrics5-g-schema.json
slug: sase-5g-api-security-metrics5-g
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SecurityMetrics5G
---
