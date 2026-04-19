---
description: AcceptTermsOfServiceResponse schema from Adyen API
layout: schema
name: AcceptTermsOfServiceResponse
properties_list:
- description: The unique identifier of the user that accepted the Terms of Service.
  name: acceptedBy
  type: string
- description: The unique identifier of the Terms of Service acceptance.
  name: id
  type: string
- description: The IP address of the user that accepted the Terms of Service.
  name: ipAddress
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
schema_file: json-schema/legal-entity-accept-terms-of-service-response-schema.json
slug: legal-entity-accept-terms-of-service-response
tags:
- Payments
- Financial Services
- Fintech
title: AcceptTermsOfServiceResponse
---
