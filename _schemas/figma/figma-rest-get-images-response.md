---
description: Response from the Get Images endpoint.
layout: schema
name: GetImagesResponse
properties_list:
- description: If present, indicates an error rendering the images.
  name: err
  type: '[''string'', ''null'']'
- description: A mapping from node IDs to URLs of the rendered images. Image URLs expire after 14 days.
  name: images
  type: object
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-get-images-response-schema.json
slug: figma-rest-get-images-response
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: GetImagesResponse
---
