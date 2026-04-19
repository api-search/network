---
description: Enable the Noise reducer feature to remove noise from your video output if necessary. Enable or disable this feature for each output individually. This setting is disabled by default. When you enable Noise reducer, you must also select a value for Noise reducer filter. For AVC outputs, when you include Noise reducer, you cannot include the Bandwidth reduction filter.
layout: schema
name: NoiseReducer
properties_list:
- description: ''
  name: Filter
  type: object
- description: ''
  name: FilterSettings
  type: object
- description: ''
  name: SpatialFilterSettings
  type: object
- description: ''
  name: TemporalFilterSettings
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-noise-reducer-schema.json
slug: mediaconvert-api-noise-reducer
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: NoiseReducer
---
