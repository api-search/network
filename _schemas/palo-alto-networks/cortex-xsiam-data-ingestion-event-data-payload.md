---
description: The payload structure for pre-normalized event data ingestion directly into the XSIAM data lake. Contains all required routing metadata plus the normalized event content for direct dataset indexing.
layout: schema
name: EventDataPayload
properties_list:
- description: The target XSIAM dataset name for direct indexing. Must match an existing dataset schema in the XSIAM data lake.
  name: dataset
  type: string
- description: The vendor that produced the source event data.
  name: vendor
  type: string
- description: The product that generated the source event.
  name: product
  type: string
- description: The log type or event category identifier for schema selection during indexing.
  name: log_type
  type: string
- description: The original raw event content from the source system, preserved alongside normalized fields for audit and reprocessing purposes.
  name: raw_log
  type: string
- description: The ISO 8601 date-time string indicating when the original event occurred at the source system.
  name: timestamp
  type: string
- description: The XSIAM tenant identifier for multi-tenant data routing.
  name: tenant_id
  type: string
- description: A unique identifier for this event record used for deduplication and correlation reference.
  name: event_id
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsiam-data-ingestion-event-data-payload-schema.json
slug: cortex-xsiam-data-ingestion-event-data-payload
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: EventDataPayload
---
