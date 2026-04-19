---
description: <p>The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20.</p> <p>To remove artwork or leave the artwork empty, you can either set <code>Artwork</code> to null, or set the <code>Merge Policy</code> to "Replace" and use an empty <code>Artwork</code> array.</p> <p>To pass through existing artwork unchanged, set the <code>Merge Policy</code> to "Prepend", "Append", or "Fallback", and use an empty <code>Artwork</code> array.</p>
layout: schema
name: Artwork
properties_list:
- description: ''
  name: InputKey
  type: object
- description: ''
  name: MaxWidth
  type: object
- description: ''
  name: MaxHeight
  type: object
- description: ''
  name: SizingPolicy
  type: object
- description: ''
  name: PaddingPolicy
  type: object
- description: ''
  name: AlbumArtFormat
  type: object
- description: ''
  name: Encryption
  type: object
provider_name: Amazon Elastic Transcoder
provider_slug: amazon-elastic-transcoder
schema_file: json-schema/amazon-elastic-transcoder-artwork-schema.json
slug: amazon-elastic-transcoder-artwork
tags:
- Amazon Web Services
- AWS
- Media
- Transcoding
- Video
title: Artwork
---
