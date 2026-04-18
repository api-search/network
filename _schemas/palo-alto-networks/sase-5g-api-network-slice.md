---
description: NetworkSlice schema from Palo Alto Networks SASE 5G Managed Services API
layout: schema
name: NetworkSlice
properties_list:
- description: Unique identifier of the network slice.
  name: slice_id
  type: string
- description: Display name of the network slice.
  name: name
  type: string
- description: Description of the slice's purpose or use case.
  name: description
  type: string
- description: 5G slice type based on 3GPP SST values. eMBB for enhanced mobile broadband, URLLC for ultra-reliable low-latency, mMTC for massive machine-type communications.
  name: slice_type
  type: string
- description: Slice/Service Type numeric value (1=eMBB, 2=URLLC, 3=mMTC).
  name: sst
  type: integer
- description: Slice Differentiator hex string for distinguishing slices of the same type.
  name: sd
  type: string
- description: Current slice status.
  name: status
  type: string
- description: ID of the security policy applied to this slice.
  name: security_policy_id
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-5g-api-network-slice-schema.json
slug: sase-5g-api-network-slice
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: NetworkSlice
---
