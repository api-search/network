---
description: A response indicating an error occurred.
layout: schema
name: ErrorResponsePayloadWithError
properties_list:
- description: For erroneous requests, this value is always `true`.
  name: error
  type: boolean
- description: Status code
  name: status
  type: number
- description: A string describing the error
  name: message
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-component-sets-error-response-payload-with-error-schema.json
slug: figma-component-sets-error-response-payload-with-error
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: ErrorResponsePayloadWithError
---
