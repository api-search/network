---
description: TermsOfServiceAcceptanceInfo schema from Adyen API
layout: schema
name: TermsOfServiceAcceptanceInfo
properties_list:
- description: The unique identifier of the user that accepted the Terms of Service.
  name: acceptedBy
  type: string
- description: The unique identifier of the legal entity for which the Terms of Service are accepted.
  name: acceptedFor
  type: string
- description: The date when the Terms of Service were accepted.
  name: createdAt
  type: string
- description: An Adyen-generated reference for the accepted Terms of Service.
  name: id
  type: string
- description: 'The type of Terms of Service. Possible values: * **adyenForPlatformsManage** * **adyenIssuing** * **adyenForPlatformsAdvanced** * **adyenCapital** * **adyenAccount** * **adyenCard** * **adyenFranchise'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-terms-of-service-acceptance-info-schema.json
slug: legal-entity-terms-of-service-acceptance-info
tags:
- Payments
- Financial Services
- Fintech
title: TermsOfServiceAcceptanceInfo
---
