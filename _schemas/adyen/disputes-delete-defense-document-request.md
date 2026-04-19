---
description: DeleteDefenseDocumentRequest schema from Adyen API
layout: schema
name: DeleteDefenseDocumentRequest
properties_list:
- description: The document type code of the defense document.
  name: defenseDocumentType
  type: string
- description: The PSP reference assigned to the dispute.
  name: disputePspReference
  type: string
- description: The merchant account identifier, for which you want to process the dispute transaction.
  name: merchantAccountCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/disputes-delete-defense-document-request-schema.json
slug: disputes-delete-defense-document-request
tags:
- Payments
- Financial Services
- Fintech
title: DeleteDefenseDocumentRequest
---
