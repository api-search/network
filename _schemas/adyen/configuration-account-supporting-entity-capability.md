---
description: AccountSupportingEntityCapability schema from Adyen API
layout: schema
name: AccountSupportingEntityCapability
properties_list:
- description: Indicates whether the supporting entity capability is allowed. Adyen sets this to **true** if the verification is successful and the account holder is permitted to use the capability.
  name: allowed
  type: boolean
- description: 'The capability level that is allowed for the account holder. Possible values: **notApplicable**, **low**, **medium**, **high**.'
  name: allowedLevel
  type: string
- description: Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account holder.
  name: enabled
  type: boolean
- description: The ID of the supporting entity.
  name: id
  type: string
- description: Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to the `allowed` field.
  name: requested
  type: boolean
- description: The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increas
  name: requestedLevel
  type: string
- description: 'The status of the verification checks for the supporting entity capability. Possible values: * **pending**: Adyen is running the verification. * **invalid**: The verification failed. Check if the `err'
  name: verificationStatus
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-account-supporting-entity-capability-schema.json
slug: configuration-account-supporting-entity-capability
tags:
- Payments
- Financial Services
- Fintech
title: AccountSupportingEntityCapability
---
