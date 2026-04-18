---
description: AssetReport schema from Palo Alto Networks IoT Security API
layout: schema
name: AssetReport
properties_list:
- description: Total number of discovered devices.
  name: total_devices
  type: integer
- description: Number of actively monitored devices.
  name: monitored_devices
  type: integer
- description: Device count breakdown by category.
  name: by_category
  type: object
- description: Device count breakdown by risk level.
  name: by_risk_level
  type: object
- description: Device count breakdown by network site.
  name: by_site
  type: array
- description: Most common device profiles.
  name: top_profiles
  type: array
- description: Timestamp when the report was generated.
  name: report_time
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/iot-security-api-asset-report-schema.json
slug: iot-security-api-asset-report
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AssetReport
---
