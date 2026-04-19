---
description: AccountCapabilityData schema from Adyen API
layout: schema
name: AccountCapabilityData
properties_list:
- description: Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful.
  name: allowed
  type: boolean
- description: 'The allowed level of the capability. Some capabilities have different levels which correspond to thresholds. Higher levels may require additional checks and increased monitoring.Possible values: **not'
  name: allowedLevel
  type: string
- description: The name of the capability. For example, **sendToTransferInstrument**.
  name: capability
  type: string
- description: List of entities that has problems with verification. The information includes the details of the errors and the actions that you can take to resolve them.
  name: problems
  type: array
- description: Indicates whether you requested the capability.
  name: requested
  type: boolean
- description: The level that you requested for the capability. Some capabilities have different levels which correspond to thresholds. Higher levels may require additional checks and increased monitoring.Possible v
  name: requestedLevel
  type: string
- description: The verification deadline for the capability that will be disallowed if verification errors are not resolved.
  name: verificationDeadline
  type: string
- description: 'The status of the verification checks for the capability. Possible values: * **pending**: Adyen is running the verification. * **invalid**: The verification failed. Check if the `errors` array contain'
  name: verificationStatus
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-webhooks-account-capability-data-schema.json
slug: management-webhooks-account-capability-data
tags:
- Payments
- Financial Services
- Fintech
title: AccountCapabilityData
---
