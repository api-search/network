---
description: If Result is Success, ErrorCondition is absent or not used in the processing of the message. In the other cases, the ErrorCondition has to be present and can refine the processing of the message response. AdditionalResponse gives more information about the success or the failure of the message request processing, for logging without real time involvements. Result of a message request processing.
layout: schema
name: Response
properties_list:
- description: ''
  name: Result
  type: object
- description: ''
  name: ErrorCondition
  type: object
- description: If present, the POI logs it for further examination.
  name: AdditionalResponse
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-response-schema.json
slug: terminal-response
tags:
- Payments
- Financial Services
- Fintech
title: Response
---
