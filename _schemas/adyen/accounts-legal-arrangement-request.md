---
description: LegalArrangementRequest schema from Adyen API
layout: schema
name: LegalArrangementRequest
properties_list:
- description: The code of the legal arrangement to be deleted. If you also send `legalArrangementEntityCodes`, only the entities listed will be deleted.
  name: legalArrangementCode
  type: string
- description: List of legal arrangement entities to be deleted.
  name: legalArrangementEntityCodes
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-legal-arrangement-request-schema.json
slug: accounts-legal-arrangement-request
tags:
- Payments
- Financial Services
- Fintech
title: LegalArrangementRequest
---
