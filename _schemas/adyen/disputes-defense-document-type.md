---
description: DefenseDocumentType schema from Adyen API
layout: schema
name: DefenseDocumentType
properties_list:
- description: When **true**, you've successfully uploaded this type of defense document. When **false**, you haven't uploaded this defense document type.
  name: available
  type: boolean
- description: The document type code of the defense document.
  name: defenseDocumentTypeCode
  type: string
- description: 'Indicates to what extent the defense document is required in the defense process. Possible values: * **Required**: You must supply the document. * **OneOrMore**: You must supply at least one of the do'
  name: requirementLevel
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/disputes-defense-document-type-schema.json
slug: disputes-defense-document-type
tags:
- Payments
- Financial Services
- Fintech
title: DefenseDocumentType
---
