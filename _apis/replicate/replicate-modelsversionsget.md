---
aid: replicate:replicate-modelsversionsget
name: Replicate Get a model version
tags:
- Model
- Name
- Owner
- Version
humanURL: 
properties: []
description: >-
  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/models/replicate/hello-world/versions/5c7d5dc6dd8bf75c1acaa8565735e7986bc5b66206b55cca93cb72c9bf15ccaa ```  The response will be the version object:  ```json {   "id": "5c7d5dc6dd8bf75c1acaa8565735e7986bc5b66206b55cca93cb72c9bf15ccaa",   "created_at": "2022-04-26T19:29:04.418669Z",   "cog_version": "0.3.0",   "openapi_schema": {...} } ```  Every model describes its in...

---
