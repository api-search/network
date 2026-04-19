---
description: SupportingEntityCapability schema from Adyen API
layout: schema
name: SupportingEntityCapability
properties_list:
- description: Indicates whether the capability is allowed for the supporting entity. If a capability is allowed for a supporting entity but not for the parent legal entity, this means the legal entity has other sup
  name: allowed
  type: boolean
- description: Supporting entity reference
  name: id
  type: string
- description: Indicates whether the supporting entity capability is requested.
  name: requested
  type: boolean
- description: 'The status of the verification checks for the capability of the supporting entity. Possible values: * **pending**: Adyen is running the verification. * **invalid**: The verification failed. Check if t'
  name: verificationStatus
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-supporting-entity-capability-schema.json
slug: legal-entity-supporting-entity-capability
tags:
- Payments
- Financial Services
- Fintech
title: SupportingEntityCapability
---
