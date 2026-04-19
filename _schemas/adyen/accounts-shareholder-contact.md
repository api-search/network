---
description: ShareholderContact schema from Adyen API
layout: schema
name: ShareholderContact
properties_list:
- description: The address of the person.
  name: address
  type: object
- description: The e-mail address of the person.
  name: email
  type: string
- description: 'The phone number of the person provided as a single string. It will be handled as a landline phone. Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"'
  name: fullPhoneNumber
  type: string
- description: 'Job title of the person. Required when the `shareholderType` is **Controller**. Example values: **Chief Executive Officer**, **Chief Financial Officer**, **Chief Operating Officer**, **President**, **'
  name: jobTitle
  type: string
- description: The name of the person.
  name: name
  type: object
- description: Contains information about the person.
  name: personalData
  type: object
- description: The phone number of the person.
  name: phoneNumber
  type: object
- description: The unique identifier (UUID) of the shareholder entry. >**If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Shareholder will be created
  name: shareholderCode
  type: string
- description: Your reference for the shareholder entry.
  name: shareholderReference
  type: string
- description: 'Specifies how the person is associated with the account holder. Possible values: * **Owner**: Individuals who directly or indirectly own 25% or more of a company. * **Controller**: Individuals who are'
  name: shareholderType
  type: string
- description: The URL of the person's website.
  name: webAddress
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-shareholder-contact-schema.json
slug: accounts-shareholder-contact
tags:
- Payments
- Financial Services
- Fintech
title: ShareholderContact
---
