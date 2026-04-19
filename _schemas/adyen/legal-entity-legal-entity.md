---
description: LegalEntity schema from Adyen API
layout: schema
name: LegalEntity
properties_list:
- description: 'Contains key-value pairs that specify the actions that the legal entity can do in your platform.The key is a capability required for your integration. For example, **issueCard** for Issuing.The value '
  name: capabilities
  type: object
- description: List of documents uploaded for the legal entity.
  name: documentDetails
  type: array
- description: List of documents uploaded for the legal entity.
  name: documents
  type: array
- description: List of legal entities associated with the current legal entity. For example, ultimate beneficial owners associated with an organization through ownership or control, or as signatories.
  name: entityAssociations
  type: array
- description: The unique identifier of the legal entity.
  name: id
  type: string
- description: Information about the individual. Required if `type` is **individual**.
  name: individual
  type: object
- description: Information about the organization. Required if `type` is **organization**.
  name: organization
  type: object
- description: List of verification errors related to capabilities for the legal entity.
  name: problems
  type: array
- description: Your reference for the legal entity, maximum 150 characters.
  name: reference
  type: string
- description: Information about the sole proprietorship. Required if `type` is **soleProprietorship**.
  name: soleProprietorship
  type: object
- description: List of transfer instruments that the legal entity owns.
  name: transferInstruments
  type: array
- description: Information about the trust. Required if `type` is **trust**.
  name: trust
  type: object
- description: 'The type of legal entity. Possible values: **individual**, **organization**, **soleProprietorship**, or **trust**.'
  name: type
  type: string
- description: Information about the unincorporated partnership. Required if `type` is **unincorporatedPartnership**.
  name: unincorporatedPartnership
  type: object
- description: List of verification deadlines and the capabilities that will be disallowed if verification errors are not resolved.
  name: verificationDeadlines
  type: array
- description: A key-value pair that specifies the [verification process](https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details/) for a legal entity. Set to **upfront** for [upfront verifica
  name: verificationPlan
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-legal-entity-schema.json
slug: legal-entity-legal-entity
tags:
- Payments
- Financial Services
- Fintech
title: LegalEntity
---
