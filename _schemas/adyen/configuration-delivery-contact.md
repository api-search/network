---
description: DeliveryContact schema from Adyen API
layout: schema
name: DeliveryContact
properties_list:
- description: The address of the contact.
  name: address
  type: object
- description: The email address of the contact.
  name: email
  type: string
- description: The full phone number of the contact provided as a single string. It will be handled as a landline phone. **Examples:** "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344"
  name: fullPhoneNumber
  type: string
- description: The name of the contact.
  name: name
  type: object
- description: The phone number of the contact.
  name: phoneNumber
  type: object
- description: The URL of the contact's website.
  name: webAddress
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-delivery-contact-schema.json
slug: configuration-delivery-contact
tags:
- Payments
- Financial Services
- Fintech
title: DeliveryContact
---
