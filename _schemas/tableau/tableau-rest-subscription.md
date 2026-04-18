---
description: ''
layout: schema
name: Subscription
properties_list:
- description: The unique identifier for the subscription.
  name: id
  type: string
- description: The subject line of the subscription email.
  name: subject
  type: string
- description: Whether to attach an image of the view.
  name: attachImage
  type: boolean
- description: Whether to attach a PDF of the view.
  name: attachPdf
  type: boolean
- description: Custom message for the subscription.
  name: message
  type: string
- description: ''
  name: pageOrientation
  type: string
- description: ''
  name: pageSizeOption
  type: string
- description: Whether the subscription is suspended.
  name: suspended
  type: boolean
- description: ''
  name: content
  type: object
- description: ''
  name: schedule
  type: object
- description: ''
  name: user
  type: object
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-subscription-schema.json
slug: tableau-rest-subscription
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: Subscription
---
