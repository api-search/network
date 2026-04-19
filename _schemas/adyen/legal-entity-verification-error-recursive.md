---
description: VerificationError-recursive schema from Adyen API
layout: schema
name: VerificationError-recursive
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
- description: The type of error.
  name: type
  type: string
- description: An object containing possible solutions to fix a verification error.
  name: remediatingActions
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-verification-error-recursive-schema.json
slug: legal-entity-verification-error-recursive
tags:
- Payments
- Financial Services
- Fintech
title: VerificationError-recursive
---
