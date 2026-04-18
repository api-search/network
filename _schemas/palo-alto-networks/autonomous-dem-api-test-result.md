---
description: TestResult schema from Palo Alto Networks Autonomous DEM API
layout: schema
name: TestResult
properties_list:
- description: Timestamp of the test execution.
  name: timestamp
  type: string
- description: Synthetic test identifier.
  name: test_id
  type: string
- description: Agent that ran the test.
  name: agent_id
  type: string
- description: User associated with the agent.
  name: user_id
  type: string
- description: Test execution result status.
  name: status
  type: string
- description: Total response latency in milliseconds.
  name: latency_ms
  type: number
- description: DNS resolution time in milliseconds.
  name: dns_time_ms
  type: number
- description: TCP connection establishment time in milliseconds.
  name: tcp_connect_ms
  type: number
- description: Time to first byte for HTTP tests in milliseconds.
  name: ttfb_ms
  type: number
- description: HTTP response status code for HTTP type tests.
  name: http_status_code
  type: integer
- description: Error message if the test failed.
  name: error_message
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/autonomous-dem-api-test-result-schema.json
slug: autonomous-dem-api-test-result
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: TestResult
---
