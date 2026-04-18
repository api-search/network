---
channels:
- description: Webhook channel that receives video processing and live streaming event notifications from Cloudflare Stream.
  name: /webhook
  operation: publish
  operation_id: onStreamEvent
  summary: Receive Stream video event
description: Cloudflare Stream sends webhook notifications when videos finish processing and are ready to stream, or when a video enters an error state. Webhooks can also be configured for live streaming events. Configure a webhook URL in the Stream dashboard or via the API to receive these notifications.
layout: asyncapi
messages:
- description: Sent when a video upload has been successfully processed, encoded, and is available for playback. The payload includes the video UID, metadata, playback URLs, and duration.
  name: VideoReady
  summary: Notification that a video has been processed and is ready to stream
  title: Video Ready
- description: Sent when a video upload fails during processing or encoding. The payload includes error details and the video UID for troubleshooting.
  name: VideoError
  summary: Notification that video processing has encountered an error
  title: Video Error
- description: Sent when a live input begins receiving and broadcasting a live stream via RTMPS or SRT.
  name: LiveStreamStarted
  summary: Notification that a live stream has started
  title: Live Stream Started
- description: Sent when a live stream stops broadcasting. If recording is enabled, the recorded video will begin processing.
  name: LiveStreamEnded
  summary: Notification that a live stream has ended
  title: Live Stream Ended
name: Cloudflare Stream Webhooks
provider_name: Cloudflare
provider_slug: cloudflare
servers:
- description: Your configured webhook endpoint URL. Cloudflare Stream sends HTTP POST requests to this URL when video processing events occur. Validate the webhook-signing-key header to verify request authenticity.
  name: webhookEndpoint
  protocol: https
  url: '{webhookUrl}'
slug: cloudflare-stream-webhooks-asyncapi
spec_file: asyncapi/cloudflare-stream-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/cloudflare/refs/heads/main/asyncapi/cloudflare-stream-webhooks-asyncapi.yml
tags:
- AI Gateway
- API Gateway
- Artificial Intelligence
- CDN
- Cloud
- Containers
- DDoS Protection
- DNS
- Edge
- Edge Computing
- Object Storage
- Platform
- Real-Time Communication
- Security
- Serverless
- Web Performance
- AsyncAPI
- Webhooks
- Events
version: '1.0'
---
