---
description: LegalEntityCapability schema from Adyen API
layout: schema
name: LegalEntityCapability
properties_list:
- description: Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful.
  name: allowed
  type: boolean
- description: 'The capability level that is allowed for the legal entity. Possible values: **notApplicable**, **low**, **medium**, **high**.'
  name: allowedLevel
  type: string
- description: The settings that are allowed for the legal entity.
  name: allowedSettings
  type: object
- description: Indicates whether the capability is requested. To check whether the legal entity is permitted to use the capability, refer to the `allowed` field.
  name: requested
  type: boolean
- description: The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increas
  name: requestedLevel
  type: string
- description: The settings that are requested for the legal entity.
  name: requestedSettings
  type: object
- description: The capability status of transfer instruments associated with the legal entity.
  name: transferInstruments
  type: array
- description: 'The status of the verification checks for the capability. Possible values: * **pending**: Adyen is running the verification. * **invalid**: The verification failed. Check if the `errors` array contain'
  name: verificationStatus
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-legal-entity-capability-schema.json
slug: legal-entity-legal-entity-capability
tags:
- Payments
- Financial Services
- Fintech
title: LegalEntityCapability
---
