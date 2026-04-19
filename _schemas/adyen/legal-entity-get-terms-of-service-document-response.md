---
description: GetTermsOfServiceDocumentResponse schema from Adyen API
layout: schema
name: GetTermsOfServiceDocumentResponse
properties_list:
- description: The Terms of Service document in Base64-encoded format.
  name: document
  type: string
- description: The unique identifier of the legal entity.
  name: id
  type: string
- description: 'The language used for the Terms of Service document, specified by the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. Possible value: **en** for English.'
  name: language
  type: string
- description: The unique identifier of the Terms of Service document.
  name: termsOfServiceDocumentId
  type: string
- description: 'The type of Terms of Service. Possible values: * **adyenForPlatformsManage** * **adyenIssuing** * **adyenForPlatformsAdvanced** * **adyenCapital** * **adyenAccount** * **adyenCard** * **adyenFranchise'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-get-terms-of-service-document-response-schema.json
slug: legal-entity-get-terms-of-service-document-response
tags:
- Payments
- Financial Services
- Fintech
title: GetTermsOfServiceDocumentResponse
---
