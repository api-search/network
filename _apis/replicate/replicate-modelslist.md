---
aid: replicate:replicate-modelslist
name: Replicate List public models
tags:
- Models
humanURL: 
properties: []
description: >-
  Get a paginated list of public models.  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/models ```  The response will be a paginated JSON array of model objects:  ```json {   "next": null,   "previous": null,   "results": [     {       "url": "https://replicate.com/acme/hello-world",       "owner": "acme",       "name": "hello-world",       "description": "A tiny model that says hello",       "visibility": "public"...

---
