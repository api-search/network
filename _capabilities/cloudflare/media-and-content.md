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
- cloudflare
- create a live streaming input.
- images upload image
- list videos
- list all videos.
- images create direct upload
- media
- stream list videos
- list all images.
- upload an image.
- list live streaming inputs.
- get video details.
- platform
- delete a video.
- get image details.
- list videos.
- api gateway
- web performance
- video management.
- images delete image
- cloud
- ddos protection
- images list images
- serverless
- delete an image.
- stream create live input
- stream upload video
- list image variants.
- images list variants
- stream get video
- edge computing
- ai gateway
- images get image
- stream delete video
- object storage
- stream create direct upload
- create a direct upload url for images.
- security
- dns
- edge
- cdn
- images
- containers
- video
- upload a video from url.
- real-time communication
- list images.
- artificial intelligence
- list images
- create a direct upload url.
- image management.
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
