---
description: VerificationError schema from Adyen API
layout: schema
name: VerificationError
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
- description: Contains the actions that you can take to resolve the verification error.
  name: remediatingActions
  type: array
- description: Contains more granular information about the verification error.
  name: subErrors
  type: array
- description: 'The type of error. Possible values: **invalidInput**, **dataMissing**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-verification-error-schema.json
slug: configuration-verification-error
tags:
- Payments
- Financial Services
- Fintech
title: VerificationError
---
