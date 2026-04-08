---
aid: replicate:replicate-collectionslist
name: Replicate List collections of models
tags:
- Collections
humanURL: 
properties: []
description: >-
  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/collections ```  The response will be a paginated JSON list of collection objects:  ```json {   "next": "null",   "previous": null,   "results": [     {       "name": "Super resolution",       "slug": "super-resolution",       "description": "Upscaling models that create high-quality images from low-quality images."     }   ] } ```

---
