---
description: Indicate the availability of the POI Terminal components. The data element is absent if the component is not part of the POI Terminal. State of a POI Terminal.
layout: schema
name: POIStatus
properties_list:
- description: ''
  name: GlobalStatus
  type: object
- description: If security module present.
  name: SecurityOKFlag
  type: boolean
- description: If PED present.
  name: PEDOKFlag
  type: boolean
- description: If card reader device present.
  name: CardReaderOKFlag
  type: boolean
- description: ''
  name: PrinterStatus
  type: object
- description: If communication infrastructure present.
  name: CommunicationOKFlag
  type: boolean
- description: ''
  name: CashHandlingDevice
  type: array
- description: default False.
  name: FraudPreventionFlag
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-poi-status-schema.json
slug: terminal-poi-status
tags:
- Payments
- Financial Services
- Fintech
title: POIStatus
---
