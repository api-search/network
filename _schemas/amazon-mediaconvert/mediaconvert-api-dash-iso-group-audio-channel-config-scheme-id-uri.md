---
description: 'Use this setting only when your audio codec is a Dolby one (AC3, EAC3, or Atmos) and your downstream workflow requires that your DASH manifest use the Dolby channel configuration tag, rather than the MPEG one. For example, you might need to use this to make dynamic ad insertion work. Specify which audio channel configuration scheme ID URI MediaConvert writes in your DASH manifest. Keep the default value, MPEG channel configuration (MPEG_CHANNEL_CONFIGURATION), to have MediaConvert write this: urn:mpeg:mpegB:cicp:ChannelConfiguration. Choose Dolby channel configuration (DOLBY_CHANNEL_CONFIGURATION) to have MediaConvert write this instead: tag:dolby.com,2014:dash:audio_channel_configuration:2011.'
layout: schema
name: DashIsoGroupAudioChannelConfigSchemeIdUri
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-dash-iso-group-audio-channel-config-scheme-id-uri-schema.json
slug: mediaconvert-api-dash-iso-group-audio-channel-config-scheme-id-uri
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: DashIsoGroupAudioChannelConfigSchemeIdUri
---
