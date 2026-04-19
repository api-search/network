---
description: StoredDetails schema from Adyen API
layout: schema
name: StoredDetails
properties_list:
- description: The stored bank account.
  name: bank
  type: object
- description: The stored card information.
  name: card
  type: object
- description: The email associated with stored payment details.
  name: emailAddress
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-stored-details-schema.json
slug: checkout-stored-details
tags:
- Payments
- Financial Services
- Fintech
title: StoredDetails
---
