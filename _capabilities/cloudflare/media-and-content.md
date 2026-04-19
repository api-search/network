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
- edge computing
- serverless
- list image variants.
- create a direct upload url.
- dns
- cloudflare
- security
- delete a video.
- images list images
- delete an image.
- ddos protection
- stream list live inputs
- cdn
- images list variants
- video
- stream get video
- list videos
- object storage
- stream list videos
- cloud
- create a direct upload url for images.
- containers
- web performance
- api gateway
- create a live streaming input.
- stream delete video
- video management.
- image management.
- ai gateway
- list videos.
- list all videos.
- get image details.
- media
- upload an image.
- get video details.
- artificial intelligence
- list all images.
- stream create live input
- platform
- images create direct upload
- upload a video from url.
- stream upload video
- real-time communication
- images get image
- images delete image
- list live streaming inputs.
- edge
- list images.
- images
- images upload image
- stream create direct upload
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
