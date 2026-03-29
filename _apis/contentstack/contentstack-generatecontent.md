---
aid: contentstack:contentstack-generatecontent
name: Generate AI content
tags:
- Generative AI
humanURL: 
properties: []
description: >-
  Processes a prompt using retrieval augmented generation (RAG) to produce AI-generated content aligned with the specified Brand Kit. When knowledge_vault is enabled, relevant content from the Brand Kit's Knowledge Vault is retrieved and used as context for the LLM. An optional voice_profile_uid can be specified to apply specific writing style guidelines to the generated content. Returns a streaming dictionary response. Rate limited to 10 requests per second per organization.

---
