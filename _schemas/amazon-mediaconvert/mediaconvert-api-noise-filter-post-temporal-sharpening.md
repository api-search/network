---
description: When you set Noise reducer (noiseReducer) to Temporal (TEMPORAL), the bandwidth and sharpness of your output is reduced. You can optionally use Post temporal sharpening (postTemporalSharpening) to apply sharpening to the edges of your output. Note that Post temporal sharpening will also make the bandwidth reduction from the Noise reducer smaller. The default behavior, Auto (AUTO), allows the transcoder to determine whether to apply sharpening, depending on your input type and quality. When you set Post temporal sharpening to Enabled (ENABLED), specify how much sharpening is applied using Post temporal sharpening strength (postTemporalSharpeningStrength). Set Post temporal sharpening to Disabled (DISABLED) to not apply sharpening.
layout: schema
name: NoiseFilterPostTemporalSharpening
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-noise-filter-post-temporal-sharpening-schema.json
slug: mediaconvert-api-noise-filter-post-temporal-sharpening
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: NoiseFilterPostTemporalSharpening
---
