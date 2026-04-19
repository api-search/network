---
class_count: 1
classes:
- InputData
context_file: json-ld/adyen-terminal-input-data-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-input-data-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Input Data from Adyen.
layout: jsonld
name: Adyen Terminal Input Data Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Device
  type: string
- container: ''
  name: InfoQualify
  type: string
- container: ''
  name: InputCommand
  type: string
- container: ''
  name: NotifyCardInputFlag
  type: boolean
- container: ''
  name: MaxInputTime
  type: integer
- container: ''
  name: ImmediateResponseFlag
  type: boolean
- container: ''
  name: MinLength
  type: integer
- container: ''
  name: MaxLength
  type: integer
- container: ''
  name: MaxDecimalLength
  type: integer
- container: ''
  name: WaitUserValidationFlag
  type: boolean
- container: ''
  name: DefaultInputString
  type: string
- container: ''
  name: DefaultLayoutString
  type: string
- container: ''
  name: StringMask
  type: string
- container: ''
  name: FromRightToLeftFlag
  type: boolean
- container: ''
  name: MaskCharactersFlag
  type: boolean
- container: ''
  name: BeepKeyFlag
  type: boolean
- container: ''
  name: GlobalCorrectionFlag
  type: boolean
- container: ''
  name: DisableCancelFlag
  type: boolean
- container: ''
  name: DisableCorrectFlag
  type: boolean
- container: ''
  name: DisableValidFlag
  type: boolean
- container: ''
  name: MenuBackFlag
  type: boolean
property_count: 21
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-input-data-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
