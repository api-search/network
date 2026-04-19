---
description: Specify the video sample composition time offset mode in the output fMP4 TRUN box. For wider player compatibility, set Video composition offsets to Unsigned or leave blank. The earliest presentation time may be greater than zero, and sample composition time offsets will increment using unsigned integers. For strict fMP4 video and audio timing, set Video composition offsets to Signed. The earliest presentation time will be equal to zero, and sample composition time offsets will increment using signed integers.
layout: schema
name: DashIsoVideoCompositionOffsets
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-dash-iso-video-composition-offsets-schema.json
slug: mediaconvert-api-dash-iso-video-composition-offsets
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: DashIsoVideoCompositionOffsets
---
