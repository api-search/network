---
description: IssuedCard schema from Adyen API
layout: schema
name: IssuedCard
properties_list:
- description: The authorisation type. For example, **defaultAuthorisation**, **preAuthorisation**, **finalAuthorisation**
  name: authorisationType
  type: string
- description: 'Indicates the method used for entering the PAN to initiate a transaction. Possible values: **manual**, **chip**, **magstripe**, **contactless**, **cof**, **ecommerce**, **token**.'
  name: panEntryMode
  type: string
- description: Contains information about how the payment was processed. For example, **ecommerce** for online or **pos** for in-person payments.
  name: processingType
  type: string
- description: If you are using relayed authorisation, this object contains information from the relayed authorisation response from your server.
  name: relayedAuthorisationData
  type: object
- description: The identifier of the original payment provided by the scheme. The Id could be alphanumeric or numeric depending on the scheme. The schemeTraceID should be referring to an original schemeUniqueTransac
  name: schemeTraceId
  type: string
- description: The unique identifier created by the scheme. The ID could be alphanumeric or numeric depending on the scheme.
  name: schemeUniqueTransactionId
  type: string
- description: '**issuedCard**'
  name: type
  type: string
- description: The evaluation of the validation facts. See [validation checks](https://docs.adyen.com/issuing/validation-checks) for more information.
  name: validationFacts
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-issued-card-schema.json
slug: transfer-webhooks-issued-card
tags:
- Payments
- Financial Services
- Fintech
title: IssuedCard
---
