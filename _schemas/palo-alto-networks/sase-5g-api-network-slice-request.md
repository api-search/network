---
description: NetworkSliceRequest schema from Palo Alto Networks SASE 5G Managed Services API
layout: schema
name: NetworkSliceRequest
properties_list:
- description: Display name for the network slice.
  name: name
  type: string
- description: Optional description.
  name: description
  type: string
- description: 5G slice type.
  name: slice_type
  type: string
- description: Slice Differentiator hex string.
  name: sd
  type: string
- description: Security policy ID to apply to this slice.
  name: security_policy_id
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-5g-api-network-slice-request-schema.json
slug: sase-5g-api-network-slice-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: NetworkSliceRequest
---
