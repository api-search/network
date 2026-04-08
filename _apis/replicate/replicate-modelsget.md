---
aid: replicate:replicate-modelsget
name: Replicate Get a model
tags:
- Model
- Name
- Owner
humanURL: 
properties: []
description: >-
  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/models/replicate/hello-world ```  The response will be a model object in the following format:  ```json {   "url": "https://replicate.com/replicate/hello-world",   "owner": "replicate",   "name": "hello-world",   "description": "A tiny model that says hello",   "visibility": "public",   "github_url": "https://github.com/replicate/cog-examples",   "paper_url": null,   ...

---
