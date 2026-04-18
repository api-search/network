---
description: RemoveBackgroundRequest from Adobe Photoshop API
layout: schema
name: RemoveBackgroundRequest
properties_list:
- description: ''
  name: image
  type: object
- description: cutout removes the background, mask returns a grayscale mask.
  name: mode
  type: string
- description: ''
  name: output
  type: object
- description: Whether to trim whitespace around the subject.
  name: trim
  type: boolean
- description: Optional replacement background color.
  name: backgroundColor
  type: object
- description: Level of color decontamination to apply.
  name: colorDecontamination
  type: integer
provider_name: Adobe Photoshop
provider_slug: adobe-photoshop
schema_file: json-schema/adobe-photoshop-api-remove-background-request-schema.json
slug: adobe-photoshop-api-remove-background-request
tags:
- AI/ML
- Creative Cloud
- Image Editing
- Photoshop
- Plugins
- REST API
- Scripting
title: RemoveBackgroundRequest
---
