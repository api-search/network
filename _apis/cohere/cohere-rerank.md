---
aid: cohere:cohere-rerank
name: Rerank documents by relevance
tags:
- Rerank
humanURL: 
properties: []
description: >-
  Takes a query and a list of text documents and returns them ordered by relevance with assigned relevance scores. It is recommended not to send more than 1000 documents in a single request. Long documents are automatically truncated to the value of max_tokens_per_doc. Structured data should be formatted as YAML strings for best performance.

---
