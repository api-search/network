---
aid: replicate:replicate-modelscreate
name: Replicate Create a model
tags:
- Models
humanURL: 
properties: []
description: >-
  Create a model.  Example cURL request:  ```console curl -s -X POST \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   -H 'Content-Type: application/json' \   -d '{"owner": "alice", "name": "my-model", "description": "An example model", "visibility": "public", "hardware": "cpu"}' \   https://api.replicate.com/v1/models ```  The response will be a model object in the following format:  ```json {   "url": "https://replicate.com/alice/my-model",   "owner": "alice",   "name": "my-model",   "d...

---
