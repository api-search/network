---
description: Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio + audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType.
layout: schema
name: AacAudioDescriptionBroadcasterMix
properties_list: []
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-aac-audio-description-broadcaster-mix-schema.json
slug: mediaconvert-api-aac-audio-description-broadcaster-mix
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: AacAudioDescriptionBroadcasterMix
---
