---
description: CapabilityProblem schema from Adyen API
layout: schema
name: CapabilityProblem
properties_list:
- description: The ID and the type of entity that has verification errors.
  name: entity
  type: object
- description: List of verification errors.
  name: verificationErrors
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-webhooks-capability-problem-schema.json
slug: management-webhooks-capability-problem
tags:
- Payments
- Financial Services
- Fintech
title: CapabilityProblem
---
