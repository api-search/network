---
aid: amazon-web-services:amazon-web-services-amazonwebservicescreatestreamkey
name: Createstreamkey
tags:
- API
humanURL: 
properties: []
description: >-
  Creates a stream key, used to initiate a stream, for the specified channel ARN. Note that CreateChannel creates a stream key. If you subsequently use CreateStreamKey on the same channel, it will fail because a stream key already exists and there is a limit of 1 stream key per channel. To reset the stream key on a channel, use DeleteStreamKey and then CreateStreamKey.

---
