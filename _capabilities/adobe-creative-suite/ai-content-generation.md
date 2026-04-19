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
- generation job status
- generate images from a text prompt
- generate images visually similar to a reference image
- adobe
- similar image generation from reference
- generate images similar to a reference image
- generate video
- generative ai
- get job status
- ai object compositing
- fill a masked region of an image with ai-generated content
- generate composite
- firefly
- generate and composite an ai object into a scene
- video
- generative fill operations
- photography
- generate images
- generative image expansion
- expand an image beyond its original boundaries using generative ai
- fill a masked region with ai-generated content
- expand image
- generate one or more images from a text prompt using adobe firefly
- content generation
- ai video generation
- get the status of an asynchronous firefly generation job
- generate an ai object and composite it into a scene image
- creative
- generate a short video clip from a text prompt
- generate a video from a text prompt
- expand an image beyond its boundaries
- video generation
- text-to-image generation
- generate similar images
- design
- graphics
- image generation
- get the status of an async generation job
- fill image
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
