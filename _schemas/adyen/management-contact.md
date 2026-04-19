---
description: Contact schema from Adyen API
layout: schema
name: Contact
properties_list:
- description: The individual's email address.
  name: email
  type: string
- description: The individual's first name.
  name: firstName
  type: string
- description: The infix in the individual's name, if any.
  name: infix
  type: string
- description: The individual's last name.
  name: lastName
  type: string
- description: The individual's phone number, specified as 10-14 digits with an optional `+` prefix.
  name: phoneNumber
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-contact-schema.json
slug: management-contact
tags:
- Payments
- Financial Services
- Fintech
title: Contact
---
