---
description: Promotional messaging content including ALA text and modal content.
layout: schema
name: PromoContent
properties_list:
- description: Plain text "as low as" monthly payment message, suitable for inline display on product and cart pages.
  name: ala
  type: string
- description: HTML-formatted "as low as" monthly payment message with appropriate markup for web display.
  name: html_ala
  type: string
- description: Modal headline text displayed at the top of the Affirm educational modal.
  name: headline
  type: string
- description: Modal tagline or subheading text.
  name: tagline
  type: string
- description: Call-to-action button label text for the modal.
  name: button
  type: string
- description: HTML-formatted legal disclosure footer for the modal.
  name: html_footer
  type: string
- description: Full description text for the educational modal explaining Affirm financing.
  name: description
  type: string
- description: ''
  name: config
  type: object
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/promos-promo-content-schema.json
slug: promos-promo-content
tags: []
title: PromoContent
---
