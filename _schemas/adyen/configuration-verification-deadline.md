---
description: VerificationDeadline schema from Adyen API
layout: schema
name: VerificationDeadline
properties_list:
- description: The names of the capabilities to be disallowed.
  name: capabilities
  type: array
- description: The unique identifiers of the bank account(s) that the deadline applies to
  name: entityIds
  type: array
- description: The date that verification is due by before capabilities are disallowed.
  name: expiresAt
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-verification-deadline-schema.json
slug: configuration-verification-deadline
tags:
- Payments
- Financial Services
- Fintech
title: VerificationDeadline
---
