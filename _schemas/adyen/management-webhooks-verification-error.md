---
description: VerificationError schema from Adyen API
layout: schema
name: VerificationError
properties_list:
- description: The verification error code.
  name: code
  type: string
- description: The verification error message.
  name: message
  type: string
- description: The actions that you can take to resolve the verification error.
  name: remediatingActions
  type: array
- description: More granular information about the verification error.
  name: subErrors
  type: array
- description: 'The type of verification error. Possible values: **invalidInput**, **dataMissing**, and **pendingStatus**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-webhooks-verification-error-schema.json
slug: management-webhooks-verification-error
tags:
- Payments
- Financial Services
- Fintech
title: VerificationError
---
