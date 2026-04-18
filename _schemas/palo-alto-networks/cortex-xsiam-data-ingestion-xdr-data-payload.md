---
description: The payload structure for XDR data forwarding from integrated Palo Alto Networks products. Contains product identification, tenant context, event identification, and the forwarded telemetry content for correlation in the XSIAM unified data lake.
layout: schema
name: XdrDataPayload
properties_list:
- description: The target XSIAM dataset name for the forwarded XDR data.
  name: dataset
  type: string
- description: The Palo Alto Networks product vendor designation for the forwarding source. Typically 'Palo Alto Networks'.
  name: vendor
  type: string
- description: The specific Palo Alto Networks product forwarding XDR data, such as Cortex XDR Agent, PAN-OS, Prisma Access, or Strata Logging Service.
  name: product
  type: string
- description: The XDR data type or telemetry category being forwarded (e.g., xdr_data, endpoint_event, network_event).
  name: log_type
  type: string
- description: The raw XDR telemetry content as serialized JSON from the forwarding product. Contains all available event fields from the source product's data model.
  name: raw_log
  type: string
- description: The ISO 8601 date-time string indicating when the XDR event was captured by the source product.
  name: timestamp
  type: string
- description: The XSIAM tenant identifier to which this XDR data belongs. Ensures forwarded data is routed to the correct tenant environment in multi-tenant deployments.
  name: tenant_id
  type: string
- description: A unique identifier for this forwarded XDR event, used for deduplication, correlation, and audit trail tracking.
  name: event_id
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsiam-data-ingestion-xdr-data-payload-schema.json
slug: cortex-xsiam-data-ingestion-xdr-data-payload
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: XdrDataPayload
---
