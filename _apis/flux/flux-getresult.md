---
aid: flux:flux-getresult
name: Poll for generation result
tags:
- Results
humanURL: 
properties: []
description: >-
  Polls the status of an asynchronous image generation task by ID. Returns the current status (Pending, Processing, Ready, Error, or Content Moderated). When status is Ready, the response includes a sample field containing a pre-signed URL to download the generated image. The URL expires after a short time, so the image should be downloaded promptly.

---
