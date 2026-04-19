---
description: Video settings for in-stream video placements.
layout: schema
name: VideoSettings
properties_list:
- description: Companion ad settings.
  name: companionSettings
  type: object
- description: Transcode settings.
  name: transcodeSettings
  type: object
- description: Skippability settings.
  name: skippableSettings
  type: object
- description: Whether OBA icons are enabled for this placement.
  name: obaEnabled
  type: boolean
- description: ''
  name: obaSettings
  type: object
- description: Video orientation setting.
  name: orientation
  type: string
- description: ''
  name: kind
  type: string
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-video-settings-schema.json
slug: google-campaign-manager-video-settings
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: VideoSettings
---
