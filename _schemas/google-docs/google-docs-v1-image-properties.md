---
description: The properties of an image.
layout: schema
name: ImageProperties
properties_list:
- description: A URI to the image with a default lifetime of 30 minutes.
  name: contentUri
  type: string
- description: The source URI of the image.
  name: sourceUri
  type: string
- description: The brightness effect of the image, from -1.0 to 1.0.
  name: brightness
  type: number
- description: The contrast effect of the image, from -1.0 to 1.0.
  name: contrast
  type: number
- description: The transparency effect of the image, from 0.0 to 1.0.
  name: transparency
  type: number
- description: The clockwise rotation angle of the image, in radians.
  name: angle
  type: number
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-image-properties-schema.json
slug: google-docs-v1-image-properties
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: ImageProperties
---
