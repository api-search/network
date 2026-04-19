---
description: ShippingLocation schema from Adyen API
layout: schema
name: ShippingLocation
properties_list:
- description: The address details of the shipping location.
  name: address
  type: object
- description: The contact details for the shipping location.
  name: contact
  type: object
- description: The unique identifier of the shipping location, for use as `shippingLocationId` when creating an order.
  name: id
  type: string
- description: The unique name of the shipping location.
  name: name
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-shipping-location-schema.json
slug: management-shipping-location
tags:
- Payments
- Financial Services
- Fintech
title: ShippingLocation
---
