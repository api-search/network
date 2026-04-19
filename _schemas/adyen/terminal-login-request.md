---
description: It conveys Information related to the session (period between a Login and the following Logout) to process. Content of the Login Request message.
layout: schema
name: LoginRequest
properties_list:
- description: Date and Time.
  name: DateTime
  type: string
- description: ''
  name: SaleSoftware
  type: object
- description: ''
  name: SaleTerminalData
  type: object
- description: The POI does not realise the transaction with the Acquirer.
  name: TrainingModeFlag
  type: boolean
- description: Default value for Device type displays.
  name: OperatorLanguage
  type: string
- description: '4 conditions to send it: a) the Sale System wants the POI log it in the transaction log b) because of reconciliation.'
  name: OperatorID
  type: string
- description: Same as OperatorID.
  name: ShiftNumber
  type: string
- description: ''
  name: TokenRequestedType
  type: object
- description: ''
  name: CustomerOrderReq
  type: object
- description: If the login involve a POI Terminal and not the first Login to the POI System.
  name: POISerialNumber
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-login-request-schema.json
slug: terminal-login-request
tags:
- Payments
- Financial Services
- Fintech
title: LoginRequest
---
