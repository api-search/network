---
description: Settings specific to audio sources in an HLS alternate rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique audio track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the properties provided, the job fails. If no properties in hlsRenditionGroupSettings are specified, the default audio track within the video segment is chosen. If there is no audio within video segment, the alternative audio with DEFAULT=YES is chosen instead.
layout: schema
name: HlsRenditionGroupSettings
properties_list:
- description: ''
  name: RenditionGroupId
  type: object
- description: ''
  name: RenditionLanguageCode
  type: object
- description: ''
  name: RenditionName
  type: object
provider_name: Amazon MediaConvert
provider_slug: amazon-mediaconvert
schema_file: json-schema/mediaconvert-api-hls-rendition-group-settings-schema.json
slug: mediaconvert-api-hls-rendition-group-settings
tags:
- AWS
- Broadcasting
- Media Processing
- Media
title: HlsRenditionGroupSettings
---
