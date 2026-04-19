---
description: Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag (FLAG), MediaConvert includes the parameter CHARACTERISTICS="public.accessibility.describes-video" in the EXT-X-MEDIA entry for this track. When you keep the default choice, Don't flag (DONT_FLAG), MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation.
layout: schema
name: HlsDescriptiveVideoServiceFlag
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-hls-descriptive-video-service-flag-schema.json
slug: mediaconvert-api-hls-descriptive-video-service-flag
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: HlsDescriptiveVideoServiceFlag
---
