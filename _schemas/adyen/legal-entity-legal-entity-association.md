---
description: LegalEntityAssociation schema from Adyen API
layout: schema
name: LegalEntityAssociation
properties_list:
- description: The unique identifier of another legal entity with which the `legalEntityId` is associated. When the `legalEntityId` is associated to legal entities other than the current one, the response returns al
  name: associatorId
  type: string
- description: The legal entity type of associated legal entity. For example, **organization**, **soleProprietorship** or **individual**.
  name: entityType
  type: string
- description: The individual's job title if the `type` is **uboThroughControl** or **signatory**.
  name: jobTitle
  type: string
- description: The unique identifier of the associated [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id).
  name: legalEntityId
  type: string
- description: The name of the associated [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id). - For **individual**, `name.firstName` and `name.lastName`. - For
  name: name
  type: string
- description: Defines the Kyc Exemption Reason for a Settlor associated with a trust. For example, **professionalServiceProvider**, **deceased**, or **contributionBelowThreshold**.
  name: settlorExemptionReason
  type: array
- description: 'Defines the relationship of the legal entity to the current legal entity. Possible values for organizations: **uboThroughOwnership**, **uboThroughControl**, **director**, **signatory**, or **ultimateP'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-legal-entity-association-schema.json
slug: legal-entity-legal-entity-association
tags:
- Payments
- Financial Services
- Fintech
title: LegalEntityAssociation
---
