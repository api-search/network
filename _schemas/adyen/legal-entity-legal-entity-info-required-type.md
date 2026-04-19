---
description: LegalEntityInfoRequiredType schema from Adyen API
layout: schema
name: LegalEntityInfoRequiredType
properties_list:
- description: 'Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example, **issueCard** for Issuing.The value '
  name: capabilities
  type: object
- description: List of legal entities associated with the current legal entity. For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories.
  name: entityAssociations
  type: array
- description: Information about the individual. Required if `type` is **individual**.
  name: individual
  type: object
- description: Information about the organization. Required if `type` is **organization**.
  name: organization
  type: object
- description: Your reference for the legal entity, maximum 150 characters.
  name: reference
  type: string
- description: Information about the sole proprietorship. Required if `type` is **soleProprietorship**.
  name: soleProprietorship
  type: object
- description: Information about the trust. Required if `type` is **trust**.
  name: trust
  type: object
- description: 'The type of legal entity. Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**.'
  name: type
  type: string
- description: Information about the unincorporated partnership. Required if `type` is **unincorporatedPartnership**.
  name: unincorporatedPartnership
  type: object
- description: A key-value pair that specifies the [verification process](https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details/) for a legal entity. Set to **upfront** for [upfront verifica
  name: verificationPlan
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-legal-entity-info-required-type-schema.json
slug: legal-entity-legal-entity-info-required-type
tags:
- Payments
- Financial Services
- Fintech
title: LegalEntityInfoRequiredType
---
