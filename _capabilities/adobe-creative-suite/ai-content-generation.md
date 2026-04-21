---
consumed_apis:
- firefly
description: AI-powered content generation workflow using Adobe Firefly for creating images, videos, and visual variations from text prompts. Used by content creators, marketers, and designers who need to rapidly produce visual assets using generative AI.
layout: capability
name: Adobe AI Content Generation
operations:
- description: Generate images from a text prompt
  method: POST
  name: generate-images
  path: /v1/generations
- description: Generate images similar to a reference image
  method: POST
  name: generate-similar-images
  path: /v1/generations/similar
- description: Expand an image beyond its boundaries
  method: POST
  name: expand-image
  path: /v1/expansions
- description: Fill a masked region with AI-generated content
  method: POST
  name: fill-image
  path: /v1/fills
- description: Generate and composite an AI object into a scene
  method: POST
  name: generate-composite
  path: /v1/composites
- description: Generate a video from a text prompt
  method: POST
  name: generate-video
  path: /v1/videos
- description: Get the status of an async generation job
  method: GET
  name: get-job-status
  path: /v1/jobs/{jobId}
personas: []
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
search_terms:
- creative
- design
- expand an image beyond its original boundaries using generative ai
- generative fill operations
- generate one or more images from a text prompt using adobe firefly
- adobe
- fill a masked region with ai-generated content
- generation job status
- generate video
- fill a masked region of an image with ai-generated content
- get the status of an asynchronous firefly generation job
- generate a video from a text prompt
- generate a short video clip from a text prompt
- video generation
- text-to-image generation
- ai video generation
- graphics
- image generation
- ai object compositing
- generative image expansion
- generate an ai object and composite it into a scene image
- generative ai
- generate composite
- generate and composite an ai object into a scene
- expand an image beyond its boundaries
- generate images
- video
- generate images from a text prompt
- similar image generation from reference
- generate images visually similar to a reference image
- content generation
- firefly
- get job status
- photography
- get the status of an async generation job
- generate similar images
- generate images similar to a reference image
- fill image
- expand image
slug: ai-content-generation
tags:
- Adobe
- Firefly
- Generative AI
- Content Generation
- Image Generation
- Video Generation
tools:
- description: Generate one or more images from a text prompt using Adobe Firefly
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: generate-images
- description: Generate images visually similar to a reference image
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: generate-similar-images
- description: Expand an image beyond its original boundaries using generative AI
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: expand-image
- description: Fill a masked region of an image with AI-generated content
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: fill-image
- description: Generate an AI object and composite it into a scene image
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: generate-composite
- description: Generate a short video clip from a text prompt
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: generate-video
- description: Get the status of an asynchronous Firefly generation job
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-job-status
---
