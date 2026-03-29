---
aid: flux:flux-generatefluxpro11
name: Generate image with FLUX 1.1 [pro]
tags:
- Generation
humanURL: 
properties: []
description: >-
  Submits an asynchronous image generation request using the FLUX 1.1 [pro] model, which offers improved prompt adherence and image quality over FLUX.1 [pro]. Returns a task ID and polling URL. The caller must poll GET /v1/get_result?id={id} until the status is Ready, then download the image from the returned sample URL.

---
