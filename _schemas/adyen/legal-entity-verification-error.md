---
description: VerificationError schema from Adyen API
layout: schema
name: VerificationError
properties_list:
- description: Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing.The value
  name: capabilities
  type: array
- description: The general error code.
  name: code
  type: string
- description: The general error message.
  name: message
  type: string
- description: An object containing possible solutions to fix a verification error.
  name: remediatingActions
  type: array
- description: An array containing more granular information about the cause of the verification error.
  name: subErrors
  type: array
- description: The type of error.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-verification-error-schema.json
slug: legal-entity-verification-error
tags:
- Payments
- Financial Services
- Fintech
title: VerificationError
---
