---
description: InputData schema from Adyen API
layout: schema
name: InputData
properties_list:
- description: ''
  name: Device
  type: object
- description: ''
  name: InfoQualify
  type: object
- description: ''
  name: InputCommand
  type: object
- description: ''
  name: NotifyCardInputFlag
  type: boolean
- description: ''
  name: MaxInputTime
  type: integer
- description: ''
  name: ImmediateResponseFlag
  type: boolean
- description: ''
  name: MinLength
  type: integer
- description: ''
  name: MaxLength
  type: integer
- description: ''
  name: MaxDecimalLength
  type: integer
- description: ''
  name: WaitUserValidationFlag
  type: boolean
- description: ''
  name: DefaultInputString
  type: string
- description: ''
  name: DefaultLayoutString
  type: string
- description: ''
  name: StringMask
  type: string
- description: ''
  name: FromRightToLeftFlag
  type: boolean
- description: ''
  name: MaskCharactersFlag
  type: boolean
- description: ''
  name: BeepKeyFlag
  type: boolean
- description: ''
  name: GlobalCorrectionFlag
  type: boolean
- description: ''
  name: DisableCancelFlag
  type: boolean
- description: ''
  name: DisableCorrectFlag
  type: boolean
- description: ''
  name: DisableValidFlag
  type: boolean
- description: ''
  name: MenuBackFlag
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-input-data-schema.json
slug: terminal-input-data
tags:
- Payments
- Financial Services
- Fintech
title: InputData
---
