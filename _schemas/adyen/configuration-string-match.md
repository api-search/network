---
description: StringMatch schema from Adyen API
layout: schema
name: StringMatch
properties_list:
- description: 'The type of string matching operation. Possible values: **startsWith**, **endsWith**, **isEqualTo**, **contains**,'
  name: operation
  type: string
- description: The string to be matched.
  name: value
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-string-match-schema.json
slug: configuration-string-match
tags:
- Payments
- Financial Services
- Fintech
title: StringMatch
---
