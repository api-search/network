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
- list images
- object storage
- video management.
- artificial intelligence
- containers
- upload an image.
- image management.
- web performance
- list all videos.
- stream upload video
- create a direct upload url for images.
- video
- security
- upload a video from url.
- stream create live input
- cloudflare
- edge computing
- list images.
- platform
- get image details.
- stream list live inputs
- images list variants
- stream delete video
- list videos.
- real-time communication
- get video details.
- stream create direct upload
- list all images.
- dns
- images delete image
- images get image
- edge
- stream get video
- list image variants.
- serverless
- media
- stream list videos
- cloud
- images create direct upload
- list videos
- api gateway
- delete an image.
- cdn
- images upload image
- images
- delete a video.
- create a direct upload url.
- list live streaming inputs.
- ai gateway
- create a live streaming input.
- ddos protection
- images list images
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
