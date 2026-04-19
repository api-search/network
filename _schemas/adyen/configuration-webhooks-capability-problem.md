---
description: CapabilityProblem schema from Adyen API
layout: schema
name: CapabilityProblem
properties_list:
- description: Contains the type of the entity and the corresponding ID.
  name: entity
  type: object
- description: Contains information about the verification error.
  name: verificationErrors
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-capability-problem-schema.json
slug: configuration-webhooks-capability-problem
tags:
- Payments
- Financial Services
- Fintech
title: CapabilityProblem
---
