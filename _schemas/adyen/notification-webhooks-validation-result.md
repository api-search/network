---
description: ValidationResult schema from Adyen API
layout: schema
name: ValidationResult
properties_list:
- description: 'The result of the check. Possible values: - **valid**: The validation was successful. - **invalid**: The validation failed. - **notValidated**: The validation was not performed because some services w'
  name: result
  type: string
- description: Type of check.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-validation-result-schema.json
slug: notification-webhooks-validation-result
tags:
- Payments
- Financial Services
- Fintech
title: ValidationResult
---
