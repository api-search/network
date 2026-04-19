---
description: Complete plant diagnosis result including crop identification and ranked disease list.
layout: schema
name: Diagnosis
properties_list:
- description: Identified or confirmed crop type.
  name: crop
  type: string
- description: Confidence level for crop identification (high, medium, low).
  name: cropConfidence
  type: string
- description: Ranked list of disease/pest diagnoses sorted by confidence descending.
  name: idArray
  type: array
provider_name: agrio
provider_slug: agrio
schema_file: json-schema/agrio-diagnosis-schema.json
slug: agrio-diagnosis
tags:
- Agriculture
- Plant Disease
- Pest Detection
- AI
- Crop Advisory
title: Diagnosis
---
