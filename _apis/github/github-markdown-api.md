---
aid: github:github-markdown-api
name: GitHub Markdown API
tags:
  - Documents
  - Markdown
  - Mode
  - Raw
  - Render
baseURL: https://api.github.com/
humanURL: https://docs.github.com/en/rest/markdown?apiVersion=2022-11-28
overlays:
  - url: overlays/github-markdown--openapi-search.yml
    type: OpenAPI
properties:
  - url: openapi/github-markdown--openapi-original.yml
    type: OpenAPI
  - url: https://docs.github.com/en/rest/markdown
    type: Documentation
description: |-

  Use the REST API to render a Markdown document as an HTML page or as raw
  text.

---