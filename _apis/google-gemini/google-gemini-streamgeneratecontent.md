---
aid: google-gemini:google-gemini-streamgeneratecontent
name: Generates a streamed response from the model given an input GenerateContentRequest. Returns a stream of GenerateContentResponse chunks using server-sent events.
tags:
- Content Generation
humanURL: 
properties: []
description: >-
  Generates a streamed response from the model. This endpoint behaves identically to generateContent but returns partial responses incrementally as server-sent events. Each event contains a GenerateContentResponse with one or more candidate content parts. Use the alt=sse query parameter to enable streaming.

---
