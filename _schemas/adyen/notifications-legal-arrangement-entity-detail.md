---
description: LegalArrangementEntityDetail schema from Adyen API
layout: schema
name: LegalArrangementEntityDetail
properties_list:
- description: The address of the entity.
  name: address
  type: object
- description: Required when creating an entity with `legalEntityType` **Business**, **NonProfit**, **PublicCompany**, or **Partnership**.
  name: businessDetails
  type: object
- description: The e-mail address of the entity.
  name: email
  type: string
- description: The phone number of the contact provided as a single string. It will be handled as a landline phone. **Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
  name: fullPhoneNumber
  type: string
- description: Required when creating an entity with `legalEntityType` **Individual**.
  name: individualDetails
  type: object
- description: 'Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement entity. Use only when updating an account holder. If you include this '
  name: legalArrangementEntityCode
  type: string
- description: Your reference for the legal arrangement entity.
  name: legalArrangementEntityReference
  type: string
- description: 'An array containing the roles of the entity in the legal arrangement. The possible values depend on the legal arrangement `type`. - For `type` **Association**: **ControllingPerson** and **Shareholder*'
  name: legalArrangementMembers
  type: array
- description: 'The legal entity type. Possible values: **Business**, **Individual**, **NonProfit**, **PublicCompany**, or **Partnership**.'
  name: legalEntityType
  type: string
- description: The phone number of the entity.
  name: phoneNumber
  type: object
- description: The URL of the website of the contact.
  name: webAddress
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-legal-arrangement-entity-detail-schema.json
slug: notifications-legal-arrangement-entity-detail
tags:
- Payments
- Financial Services
- Fintech
title: LegalArrangementEntityDetail
---
