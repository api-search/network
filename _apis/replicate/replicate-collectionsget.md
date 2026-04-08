---
aid: replicate:replicate-collectionsget
name: Replicate Get a collection of models
tags:
- Collections
- Slug
humanURL: 
properties: []
description: >-
  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/collections/super-resolution ```  The response will be a collection object with a nested list of the models in that collection:  ```json {   "name": "Super resolution",   "slug": "super-resolution",   "description": "Upscaling models that create high-quality images from low-quality images.",   "models": [...] } ```

---
