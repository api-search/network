---
description: ''
layout: schema
name: TransferRequest
properties_list:
- description: Transfer destination (phone number, SIP URI, or agent extension)
  name: destination
  type: string
- description: Type of transfer
  name: transferType
  type: string
- description: ICM label for the transfer destination. Used when routing through ICM/UCCE.
  name: label
  type: string
- description: ECC variables to pass with the transfer
  name: eccVariables
  type: object
provider_name: Cisco Voice Portal
provider_slug: cisco-voice-portal
schema_file: json-schema/cisco-voice-portal-call-control-transfer-request-schema.json
slug: cisco-voice-portal-call-control-transfer-request
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
title: TransferRequest
---
