---
description: VerificationDeadline schema from Adyen API
layout: schema
name: VerificationDeadline
properties_list:
- description: The list of capabilities that will be disallowed if information is not reviewed by the time of the deadline
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
schema_file: json-schema/legal-entity-verification-deadline-schema.json
slug: legal-entity-verification-deadline
tags:
- Payments
- Financial Services
- Fintech
title: VerificationDeadline
---
