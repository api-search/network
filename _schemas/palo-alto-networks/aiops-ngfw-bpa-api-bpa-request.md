---
description: BPARequest schema from Palo Alto Networks AIOps for NGFW BPA API
layout: schema
name: BPARequest
properties_list:
- description: Device serial number of the NGFW to assess.
  name: serial_number
  type: string
- description: PAN-OS software version running on the device (e.g., 11.1.2).
  name: version
  type: string
- description: Optional supplementary device information.
  name: device_info
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/aiops-ngfw-bpa-api-bpa-request-schema.json
slug: aiops-ngfw-bpa-api-bpa-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BPARequest
---
