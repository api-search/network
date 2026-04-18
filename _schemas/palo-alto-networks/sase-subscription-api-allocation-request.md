---
description: AllocationRequest schema from Palo Alto Networks SASE Subscription Service API
layout: schema
name: AllocationRequest
properties_list:
- description: Array of TSG allocations to set. Each entry specifies a child TSG and the quantity to allocate to it. Existing allocations for TSGs not included in the array are unchanged.
  name: allocations
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-subscription-api-allocation-request-schema.json
slug: sase-subscription-api-allocation-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AllocationRequest
---
