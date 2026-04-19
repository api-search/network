---
description: When you mimic a multi-channel audio layout with multiple mono-channel tracks, you can tag each channel layout manually. For example, you would tag the tracks that contain your left, right, and center audio with Left (L), Right (R), and Center (C), respectively. When you don't specify a value, MediaConvert labels your track as Center (C) by default. To use audio layout tagging, your output must be in a QuickTime (.mov) container; your audio codec must be AAC, WAV, or AIFF; and you must set up your audio track to have only one channel.
layout: schema
name: AudioChannelTaggingSettings
properties_list:
- description: ''
  name: ChannelTag
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-audio-channel-tagging-settings-schema.json
slug: mediaconvert-api-audio-channel-tagging-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: AudioChannelTaggingSettings
---
