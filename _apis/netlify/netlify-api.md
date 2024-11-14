---
aid: netlify:netlify-api
name: Netlify API
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
baseURL: https://api.example.com
humanURL: https://docs.netlify.com/
overlays:
  - url: >-
      overlays/https://open-api.netlify.com/6dac5474-6daf-41e6-8a14-6d9bcb8aca52-openapi-search.yml
    type: APIs.io Search
properties:
  - url: https://open-api.netlify.com/
    type: Documentation
  - url: properties/netlify-openapi-original.yml
    type: OpenAPI
description: >-
  Netlify is a hosting service for the programmable web. It understands your
  documents and provides an API to handle atomic deploys of websites, manage
  form submissions, inject JavaScript snippets, and much more. This is a
  REST-style API that uses JSON for serialization and OAuth 2 for
  authentication.

---