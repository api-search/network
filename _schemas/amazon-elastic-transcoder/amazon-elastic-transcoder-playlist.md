---
description: Use Only for Fragmented MP4 or MPEG-TS Outputs. If you specify a preset for which the value of Container is <code>fmp4</code> (Fragmented MP4) or <code>ts</code> (MPEG-TS), Playlists contains information about the master playlists that you want Elastic Transcoder to create. We recommend that you create only one master playlist per output format. The maximum number of master playlists in a job is 30.
layout: schema
name: Playlist
properties_list:
- description: ''
  name: Name
  type: object
- description: ''
  name: Format
  type: object
- description: ''
  name: OutputKeys
  type: object
- description: ''
  name: HlsContentProtection
  type: object
- description: ''
  name: PlayReadyDrm
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: StatusDetail
  type: object
provider_name: Amazon Elastic Transcoder
provider_slug: amazon-elastic-transcoder
schema_file: json-schema/amazon-elastic-transcoder-playlist-schema.json
slug: amazon-elastic-transcoder-playlist
tags:
- Amazon Web Services
- AWS
- Media
- Transcoding
- Video
title: Playlist
---
