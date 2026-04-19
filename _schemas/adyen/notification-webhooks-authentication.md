---
description: Authentication schema from Adyen API
layout: schema
name: Authentication
properties_list:
- description: The email address where the one-time password (OTP) is sent.
  name: email
  type: string
- description: The password used for 3D Secure password-based authentication. The value must be between 1 to 30 characters and must only contain the following supported characters. * Characters between **a-z**, **A-
  name: password
  type: string
- description: 'The phone number where the one-time password (OTP) is sent. This object must have: * A `type` set to **mobile**. * A `number` with a valid country code. * A `number` with more than 4 digits, excluding'
  name: phone
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-authentication-schema.json
slug: notification-webhooks-authentication
tags:
- Payments
- Financial Services
- Fintech
title: Authentication
---
