---
description: SupplyDefenseDocumentRequest schema from Adyen API
layout: schema
name: SupplyDefenseDocumentRequest
properties_list:
- description: An array containing a list of the defense documents.
  name: defenseDocuments
  type: array
- description: The PSP reference assigned to the dispute.
  name: disputePspReference
  type: string
- description: The merchant account identifier, for which you want to process the dispute transaction.
  name: merchantAccountCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/disputes-supply-defense-document-request-schema.json
slug: disputes-supply-defense-document-request
tags:
- Payments
- Financial Services
- Fintech
title: SupplyDefenseDocumentRequest
---
