---
description: VerificationError-recursive schema from Adyen API
layout: schema
name: VerificationError-recursive
properties_list:
- description: Contains the capabilities that the verification error applies to.
  name: capabilities
  type: array
- description: The verification error code.
  name: code
  type: string
- description: A description of the error.
  name: message
  type: string
- description: 'The type of error. Possible values: **invalidInput**, **dataMissing**.'
  name: type
  type: string
- description: Contains the actions that you can take to resolve the verification error.
  name: remediatingActions
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-verification-error-recursive-schema.json
slug: configuration-verification-error-recursive
tags:
- Payments
- Financial Services
- Fintech
title: VerificationError-recursive
---
