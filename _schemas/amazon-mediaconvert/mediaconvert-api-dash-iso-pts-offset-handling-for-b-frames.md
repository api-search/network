---
description: Use this setting only when your output video stream has B-frames, which causes the initial presentation time stamp (PTS) to be offset from the initial decode time stamp (DTS). Specify how MediaConvert handles PTS when writing time stamps in output DASH manifests. Choose Match initial PTS (MATCH_INITIAL_PTS) when you want MediaConvert to use the initial PTS as the first time stamp in the manifest. Choose Zero-based (ZERO_BASED) to have MediaConvert ignore the initial PTS in the video stream and instead write the initial time stamp as zero in the manifest. For outputs that don't have B-frames, the time stamps in your DASH manifests start at zero regardless of your choice here.
layout: schema
name: DashIsoPtsOffsetHandlingForBFrames
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-dash-iso-pts-offset-handling-for-b-frames-schema.json
slug: mediaconvert-api-dash-iso-pts-offset-handling-for-b-frames
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: DashIsoPtsOffsetHandlingForBFrames
---
