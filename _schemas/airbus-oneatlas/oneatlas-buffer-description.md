---
description: ''
layout: schema
name: bufferDescription
properties_list:
- description: Ordered list of requested bands. Bands can be retrieve with `metadata` link given in `_links` property of a feature.
  name: bands
  type: array
- description: ''
  name: bbox
  type: object
- description: ''
  name: step
  type: object
- description: specification of the output buffer
  name: target-model
  type: object
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-buffer-description-schema.json
slug: oneatlas-buffer-description
tags:
- Imagery
- Satellites
title: bufferDescription
---
