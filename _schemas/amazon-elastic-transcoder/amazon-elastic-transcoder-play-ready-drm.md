---
description: <p>The PlayReady DRM settings, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.</p> <p>PlayReady DRM encrypts your media files using <code>aes-ctr</code> encryption.</p> <p>If you use DRM for an <code>HLSv3</code> playlist, your outputs must have a master playlist.</p>
layout: schema
name: PlayReadyDrm
properties_list:
- description: ''
  name: Format
  type: object
- description: ''
  name: Key
  type: object
- description: ''
  name: KeyMd5
  type: object
- description: ''
  name: KeyId
  type: object
- description: ''
  name: InitializationVector
  type: object
- description: ''
  name: LicenseAcquisitionUrl
  type: object
provider_name: Amazon Elastic Transcoder
provider_slug: amazon-elastic-transcoder
schema_file: json-schema/amazon-elastic-transcoder-play-ready-drm-schema.json
slug: amazon-elastic-transcoder-play-ready-drm
tags:
- Amazon Web Services
- AWS
- Media
- Transcoding
- Video
title: PlayReadyDrm
---
