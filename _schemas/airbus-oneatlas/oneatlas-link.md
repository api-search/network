---
description: Link object
layout: schema
name: Link
properties_list:
- description: The absolute web link
  name: href
  type: string
- description: HTTP verb to distinguish between several possible actions on the same ressource.
  name: method
  type: string
- description: The name of the link
  name: name
  type: string
- description: ''
  name: resourceId
  type: object
- description: The mime-type when deferencing the link
  name: type
  type: string
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-link-schema.json
slug: oneatlas-link
tags:
- Imagery
- Satellites
title: Link
---
