---
description: AccountHolderCapability schema from Adyen API
layout: schema
name: AccountHolderCapability
properties_list:
- description: Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful and the account holder is permitted to use the capability.
  name: allowed
  type: boolean
- description: 'The capability level that is allowed for the account holder. Possible values: **notApplicable**, **low**, **medium**, **high**.'
  name: allowedLevel
  type: string
- description: A JSON object containing the settings that are allowed for the account holder.
  name: allowedSettings
  type: object
- description: Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account holder.
  name: enabled
  type: boolean
- description: Contains verification errors and the actions that you can take to resolve them.
  name: problems
  type: array
- description: Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to the `allowed` field.
  name: requested
  type: boolean
- description: The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increas
  name: requestedLevel
  type: string
- description: A JSON object containing the settings that were requested for the account holder.
  name: requestedSettings
  type: object
- description: Contains the status of the transfer instruments associated with this capability.
  name: transferInstruments
  type: array
- description: 'The status of the verification checks for the capability. Possible values: * **pending**: Adyen is running the verification. * **invalid**: The verification failed. Check if the `errors` array contain'
  name: verificationStatus
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-account-holder-capability-schema.json
slug: configuration-account-holder-capability
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderCapability
---
