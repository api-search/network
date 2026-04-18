---
description: DomainDetail schema from Palo Alto Networks DNS Security API
layout: schema
name: DomainDetail
properties_list:
- description: Fully qualified domain name queried.
  name: domain
  type: string
- description: URL filtering category assigned to the domain (e.g., malware, phishing, command-and-control, business-and-economy).
  name: category
  type: string
- description: Risk level assessment for the domain.
  name: risk_level
  type: string
- description: Numeric risk score from 0.0 (no risk) to 100.0 (critical risk).
  name: risk_score
  type: number
- description: DNS Security category classification used for policy enforcement.
  name: dns_security_category
  type: string
- description: Timestamp when the domain was first observed by DNS Security.
  name: first_seen
  type: string
- description: Timestamp when the domain was most recently observed.
  name: last_seen
  type: string
- description: Domain registrar name.
  name: registrar
  type: string
- description: Date the domain was registered.
  name: registration_date
  type: string
- description: Current IP addresses the domain resolves to.
  name: ip_addresses
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/dns-security-api-domain-detail-schema.json
slug: dns-security-api-domain-detail
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DomainDetail
---
