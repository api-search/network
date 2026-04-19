---
description: LegalArrangementDetail schema from Adyen API
layout: schema
name: LegalArrangementDetail
properties_list:
- description: The address of the legal arrangement.
  name: address
  type: object
- description: Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement. Use only when updating an account holder. If you include this field w
  name: legalArrangementCode
  type: string
- description: An array containing information about other entities that are part of the legal arrangement.
  name: legalArrangementEntities
  type: array
- description: Your reference for the legal arrangement. Must be between 3 to 128 characters.
  name: legalArrangementReference
  type: string
- description: 'The form of legal arrangement. Required if `type` is **Trust** or **Partnership**. The possible values depend on the `type`. - For `type` **Trust**: **CashManagementTrust**, **CorporateUnitTrust**, **'
  name: legalForm
  type: string
- description: 'The legal name of the legal arrangement. Minimum length: 3 characters.'
  name: name
  type: string
- description: The registration number of the legal arrangement.
  name: registrationNumber
  type: string
- description: The tax identification number of the legal arrangement.
  name: taxNumber
  type: string
- description: 'The [type of legal arrangement](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/legal-arrangements#types-of-legal-arrangements). Possible values: - **Association** - **P'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-legal-arrangement-detail-schema.json
slug: notifications-legal-arrangement-detail
tags:
- Payments
- Financial Services
- Fintech
title: LegalArrangementDetail
---
