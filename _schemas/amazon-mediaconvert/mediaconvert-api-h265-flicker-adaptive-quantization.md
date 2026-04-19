---
description: 'Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set adaptiveQuantization to a value other than Off (OFF).'
layout: schema
name: H265FlickerAdaptiveQuantization
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-h265-flicker-adaptive-quantization-schema.json
slug: mediaconvert-api-h265-flicker-adaptive-quantization
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: H265FlickerAdaptiveQuantization
---
