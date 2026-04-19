---
description: A single disease or pest identification result.
layout: schema
name: Diagnosis Result
properties_list:
- description: Unique identifier for the disease or pest.
  name: id
  type: string
- description: Confidence score for this diagnosis (0.0 to 1.0).
  name: confidence
  type: number
- description: Common name of the disease or pest.
  name: commonName
  type: string
- description: Scientific name of the disease or pest.
  name: scientificName
  type: string
provider_name: agrio
provider_slug: agrio
schema_file: json-schema/agrio-diagnosis-result-schema.json
slug: agrio-diagnosis-result
tags:
- Agriculture
- Plant Disease
- Pest Detection
- AI
- Crop Advisory
title: Diagnosis Result
---
