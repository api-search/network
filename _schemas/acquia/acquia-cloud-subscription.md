---
description: A subscription is the product that allows for applications to be hosted with Acquia. In addition, a subscription grants access to various additional services.
layout: schema
name: Subscription
properties_list:
- description: The subscription ID.
  name: id
  type: integer
- description: The subscription UUID.
  name: uuid
  type: string
- description: The subscription name.
  name: name
  type: string
- description: The time when the service defined by the subscription becomes available.
  name: start_at
  type: string
- description: The time when the service expires.
  name: expire_at
  type: string
- description: Defines the type of service this subscription is entitled to.
  name: product
  type: object
- description: The number of applications this subscription is entitled to.
  name: applications_total
  type: integer
- description: The number of applications used.
  name: applications_used
  type: integer
- description: ''
  name: organization
  type: object
- description: ''
  name: flags
  type: object
- description: ''
  name: _links
  type: object
- description: A collection of resources related to the subscription.
  name: _embedded
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-subscription-schema.json
slug: acquia-cloud-subscription
tags:
- Content
- Experience
title: Subscription
---
