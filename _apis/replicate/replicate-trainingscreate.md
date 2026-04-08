---
aid: replicate:replicate-trainingscreate
name: Replicate Create a training
tags:
- Model
- Name
- Owner
- Version
humanURL: 
properties: []
description: >-
  Start a new training of the model version you specify.  Example request body:  ```json {   "destination": "{new_owner}/{new_name}",   "input": {     "train_data": "https://example.com/my-input-images.zip",   },   "webhook": "https://example.com/my-webhook", } ```  Example cURL request:  ```console curl -s -X POST \   -d '{"destination": "{new_owner}/{new_name}", "input": {"input_images": "https://example.com/my-input-images.zip"}}' \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   -H 'C...

---
