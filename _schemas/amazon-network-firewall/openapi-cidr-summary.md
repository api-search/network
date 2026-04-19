---
description: Summarizes the CIDR blocks used by the IP set references in a firewall. Network Firewall calculates the number of CIDRs by taking an aggregated count of all CIDRs used by the IP sets you are referencing.
layout: schema
name: CIDRSummary
properties_list:
- description: ''
  name: AvailableCIDRCount
  type: object
- description: ''
  name: UtilizedCIDRCount
  type: object
- description: ''
  name: IPSetReferences
  type: object
provider_name: Amazon Network Firewall
provider_slug: amazon-network-firewall
schema_file: json-schema/openapi-cidr-summary-schema.json
slug: openapi-cidr-summary
tags:
- AWS
- Firewall
- Intrusion Detection
- Network Security
- VPC
title: CIDRSummary
---
