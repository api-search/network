---
description: Image and crop context for plant disease diagnosis.
layout: schema
name: Diagnose Request
properties_list:
- description: Crop identifier from the supported crops list.
  name: crop_id
  type: string
- description: Plant image file for diagnosis (JPEG or PNG).
  name: image
  type: string
provider_name: agrio
provider_slug: agrio
schema_file: json-schema/agrio-diagnose-request-schema.json
slug: agrio-diagnose-request
tags:
- Agriculture
- Plant Disease
- Pest Detection
- AI
- Crop Advisory
title: Diagnose Request
---
