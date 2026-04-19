---
description: Internal configuration data returned with the promo response.
layout: schema
name: PromoConfig
properties_list:
- description: Indicates whether prequalification is enabled for this merchant.
  name: promo_prequal_enabled
  type: boolean
- description: The merchant's display name.
  name: merchant_name
  type: string
- description: Affirm Resource Identifier for the merchant.
  name: merchant_ari
  type: string
- description: Affirm Resource Identifier for the current user session.
  name: user_ari
  type: string
- description: Indicates whether toast notifications are enabled for this integration.
  name: toast_enabled
  type: boolean
- description: List of enabled Affirm integration features for this merchant.
  name: enabled_integrations
  type: array
- description: Image asset URLs for use in the promotional modal.
  name: images
  type: object
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/promos-promo-config-schema.json
slug: promos-promo-config
tags: []
title: PromoConfig
---
