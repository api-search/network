---
description: DefenseReason schema from Adyen API
layout: schema
name: DefenseReason
properties_list:
- description: Array of defense document types for a specific defense reason. Indicates the document types that you can submit to the schemes to defend this dispute, and whether they are required.
  name: defenseDocumentTypes
  type: array
- description: The defense reason code that was selected to defend this dispute.
  name: defenseReasonCode
  type: string
- description: Indicates if sufficient defense material has been supplied.
  name: satisfied
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/disputes-defense-reason-schema.json
slug: disputes-defense-reason
tags:
- Payments
- Financial Services
- Fintech
title: DefenseReason
---
