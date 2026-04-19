---
description: It conveys Information requested for identification of the message request carrying the transaction to abort. A message to display on the CustomerError Device could be sent by the Sale System (DisplayOutput). Body of the Abort Request message.
layout: schema
name: AbortRequest
properties_list:
- description: ''
  name: MessageReference
  type: object
- description: Reason of aborting a transaction.
  name: AbortReason
  type: string
- description: ''
  name: DisplayOutput
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-abort-request-schema.json
slug: terminal-abort-request
tags:
- Payments
- Financial Services
- Fintech
title: AbortRequest
---
