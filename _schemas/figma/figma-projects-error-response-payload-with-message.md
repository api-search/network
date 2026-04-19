---
description: A response indicating an error occurred.
layout: schema
name: ErrorResponsePayloadWithMessage
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
schema_file: json-schema/figma-projects-error-response-payload-with-message-schema.json
slug: figma-projects-error-response-payload-with-message
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: ErrorResponsePayloadWithMessage
---
