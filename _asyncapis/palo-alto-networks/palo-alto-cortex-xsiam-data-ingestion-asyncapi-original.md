---
channels:
- description: Event channel for raw log data ingestion. Logs are submitted to the XSIAM HTTP collector endpoint as structured JSON batches. Each log entry must include dataset, vendor, product, log_type, and raw_log fields to route the data to the correct parsing pipeline. The XSIAM ingestion engine parses, normalizes, and indexes the log data into the appropriate dataset for analytics and correlation.
  name: log_data/ingested
  operation: subscribe
  operation_id: onLogDataIngested
  summary: Raw log data ingested into XSIAM
- description: Event channel for structured event data ingestion. Pre-parsed events with normalized field mappings are submitted directly to the XSIAM data lake, bypassing the raw log parsing pipeline. Each event must include dataset, vendor, product, log_type, and timestamp metadata along with the normalized event fields. Used when the source system has already normalized data into XSIAM-compatible field mappings.
  name: event_data/ingested
  operation: subscribe
  operation_id: onEventDataIngested
  summary: Structured event data ingested into XSIAM
- description: Event channel for XDR data forwarding from integrated Palo Alto Networks products including PAN-OS firewalls, Prisma Access, Cortex XDR agents, and other Strata products. Forwarded XDR data is automatically normalized and correlated within XSIAM for unified threat detection and investigation across the Palo Alto Networks security platform.
  name: xdr_data/forwarded
  operation: subscribe
  operation_id: onXdrDataForwarded
  summary: XDR data forwarded from a Palo Alto Networks product
description: Cortex XSIAM Data Ingestion provides streaming log and event ingestion endpoints for collecting security telemetry from external data sources into the XSIAM data lake. The ingestion service accepts data via HTTPS with streaming support, enabling high-throughput log collection for SIEM replacement and XDR-native data lake consolidation. Supported ingestion methods include Syslog forwarding over TCP/UDP/TLS, HTTPS log forwarding via REST endpoints, and XDR data forwarding from integrated Palo Alto Networks products. Ingested data is processed by the XSIAM correlation and analytics engines for threat detection, investigation, and automated response. Each ingestion event results in normalized data being indexed into the appropriate XSIAM dataset identified by vendor, product, and log type.
layout: asyncapi
messages:
- description: ''
  name: LogDataIngested
  summary: Raw log data submitted to the XSIAM HTTP log collector for parsing and ingestion into the data lake
  title: Log Data Ingested
- description: ''
  name: EventDataIngested
  summary: Structured and normalized event data submitted directly to the XSIAM data lake for indexing without additional parsing
  title: Event Data Ingested
- description: ''
  name: XdrDataForwarded
  summary: Telemetry data forwarded from a Palo Alto Networks XDR-enabled product to XSIAM for unified detection and correlation
  title: XDR Data Forwarded
name: Cortex XSIAM Data Ingestion
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
servers:
- description: 'Cortex XSIAM HTTP log collector endpoint for streaming log and event data ingestion. The FQDN is specific to the XSIAM tenant and is found in Settings > Configurations > Data Collection > HTTP Collectors. All requests require API key authentication using the x-xdr-auth-id header (key ID) and the Authorization header (API key value). Payloads may be gzip-compressed using the Content-Encoding: gzip header for improved throughput efficiency.'
  name: xsiam-collector
  protocol: https
  url: https://api-{fqdn}/logs/v1/event
- description: Syslog receiver endpoint for forwarding logs from external systems using Syslog over TCP, UDP, or TLS. Configure the source system to forward Syslog messages (RFC 3164 or RFC 5424) to this endpoint. TLS encryption is supported for secure log forwarding.
  name: syslog-receiver
  protocol: tcp
  url: '{syslogHost}:{syslogPort}'
slug: palo-alto-cortex-xsiam-data-ingestion-asyncapi-original
spec_file: asyncapi/palo-alto-cortex-xsiam-data-ingestion-asyncapi-original.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/asyncapi/palo-alto-cortex-xsiam-data-ingestion-asyncapi-original.yml
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---
