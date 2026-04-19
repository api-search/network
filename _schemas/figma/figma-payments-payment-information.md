---
description: An object describing a user's payment information for a plugin, widget, or Community file.
layout: schema
name: PaymentInformation
properties_list:
- description: The ID of the user whose payment information was queried. Can be used to verify the validity of a response.
  name: user_id
  type: string
- description: The ID of the plugin, widget, or Community file that was queried. Can be used to verify the validity of a response.
  name: resource_id
  type: string
- description: The type of the resource.
  name: resource_type
  type: string
- description: The UTC ISO 8601 timestamp indicating when the user purchased the resource. No value is given if the user has never purchased the resource.
  name: date_of_purchase
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-payments-payment-information-schema.json
slug: figma-payments-payment-information
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: PaymentInformation
---
