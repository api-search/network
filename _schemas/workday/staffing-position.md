---
description: ''
layout: schema
name: Position
properties_list:
- description: The Workday ID of the position.
  name: id
  type: string
- description: A display descriptor for the position.
  name: descriptor
  type: string
- description: The position reference ID.
  name: positionID
  type: string
- description: Whether the position is currently filled.
  name: isFilled
  type: boolean
- description: Whether the position is available for recruiting.
  name: isAvailableForRecruit
  type: boolean
- description: Whether the position has been closed.
  name: isClosed
  type: boolean
provider_name: Workday
provider_slug: workday
schema_file: json-schema/staffing-position-schema.json
slug: staffing-position
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: Position
---
