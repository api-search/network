---
description: ContactDetails schema from Adyen API
layout: schema
name: ContactDetails
properties_list:
- description: The address of the account holder.
  name: address
  type: object
- description: The email address of the account holder.
  name: email
  type: string
- description: The phone number of the account holder.
  name: phone
  type: object
- description: The URL of the account holder's website.
  name: webAddress
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-contact-details-schema.json
slug: notification-webhooks-contact-details
tags:
- Payments
- Financial Services
- Fintech
title: ContactDetails
---
