---
description: It conveys Information related to the target POI for which the diagnosis is requested. Content of the Diagnosis Request message.
layout: schema
name: DiagnosisRequest
properties_list:
- description: MessageHeader.POIID.
  name: POIID
  type: string
- description: Indicates if Host Diagnosis are required.
  name: HostDiagnosisFlag
  type: boolean
- description: ''
  name: AcquirerID
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-diagnosis-request-schema.json
slug: terminal-diagnosis-request
tags:
- Payments
- Financial Services
- Fintech
title: DiagnosisRequest
---
