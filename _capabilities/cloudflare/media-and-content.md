---
consumed_apis:
- cloudflare-stream
- cloudflare-images
description: Media management combining Stream video platform and Images service for uploading, processing, and delivering video and image content at scale. Used by content creators and media engineers.
layout: capability
name: Cloudflare Media and Content
operations:
- description: List videos.
  method: GET
  name: list-videos
  path: /v1/videos
- description: List images.
  method: GET
  name: list-images
  path: /v1/images
personas: []
provider_name: Cloudflare
provider_slug: cloudflare
search_terms:
- stream list live inputs
- images upload image
- list all videos.
- create a direct upload url.
- upload an image.
- get image details.
- ddos protection
- cloudflare
- edge
- delete a video.
- images create direct upload
- media
- stream create direct upload
- video
- list images
- create a live streaming input.
- images delete image
- cdn
- upload a video from url.
- cloud
- web performance
- list images.
- list live streaming inputs.
- create a direct upload url for images.
- serverless
- images list images
- ai gateway
- delete an image.
- stream upload video
- object storage
- stream create live input
- security
- api gateway
- real-time communication
- dns
- get video details.
- edge computing
- image management.
- containers
- list all images.
- images
- list image variants.
- list videos
- platform
- video management.
- images get image
- images list variants
- stream delete video
- list videos.
- stream get video
- stream list videos
- artificial intelligence
slug: media-and-content
tags:
- Cloudflare
- Media
- Video
- Images
tools:
- description: List all videos.
  hints:
    openWorld: true
    readOnly: true
  name: stream-list-videos
- description: Upload a video from URL.
  hints:
    readOnly: false
  name: stream-upload-video
- description: Get video details.
  hints:
    readOnly: true
  name: stream-get-video
- description: Delete a video.
  hints:
    destructive: true
    idempotent: true
  name: stream-delete-video
- description: List live streaming inputs.
  hints:
    readOnly: true
  name: stream-list-live-inputs
- description: Create a live streaming input.
  hints:
    readOnly: false
  name: stream-create-live-input
- description: Create a direct upload URL.
  hints:
    readOnly: false
  name: stream-create-direct-upload
- description: List all images.
  hints:
    openWorld: true
    readOnly: true
  name: images-list-images
- description: Upload an image.
  hints:
    readOnly: false
  name: images-upload-image
- description: Get image details.
  hints:
    readOnly: true
  name: images-get-image
- description: Delete an image.
  hints:
    destructive: true
    idempotent: true
  name: images-delete-image
- description: List image variants.
  hints:
    readOnly: true
  name: images-list-variants
- description: Create a direct upload URL for images.
  hints:
    readOnly: false
  name: images-create-direct-upload
---
