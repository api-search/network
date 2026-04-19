---
description: AvsAddress schema from Adyen API
layout: schema
name: AvsAddress
properties_list:
- description: 'The street and house number of the address. Example: 1 Infinite Loop, Cupertino.'
  name: streetAddress
  type: string
- description: 'The zip or post code of the address. Example: CA 95014'
  name: zip
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/test-cards-avs-address-schema.json
slug: test-cards-avs-address
tags:
- Payments
- Financial Services
- Fintech
title: AvsAddress
---
