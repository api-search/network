---
description: This setting can improve the compatibility of your output with video players on obsolete devices. It applies only to DASH H.264 outputs with DRM encryption. Choose Unencrypted SEI (UNENCRYPTED_SEI) only to correct problems with playback on older devices. Otherwise, keep the default setting CENC v1 (CENC_V1). If you choose Unencrypted SEI, for that output, the service will exclude the access unit delimiter and will leave the SEI NAL units unencrypted.
layout: schema
name: DashIsoPlaybackDeviceCompatibility
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-dash-iso-playback-device-compatibility-schema.json
slug: mediaconvert-api-dash-iso-playback-device-compatibility
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: DashIsoPlaybackDeviceCompatibility
---
