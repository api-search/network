---
aid: replicate:replicate-trainingsget
name: Replicate Get a training
tags:
- Training
humanURL: 
properties: []
description: >-
  Get the current state of a training.  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/trainings/zz4ibbonubfz7carwiefibzgga ```  The response will be the training object:  ```json {   "completed_at": "2023-09-08T16:41:19.826523Z",   "created_at": "2023-09-08T16:32:57.018467Z",   "error": null,   "id": "zz4ibbonubfz7carwiefibzgga",   "input": {     "input_images": "https://example.com/my-input-images.zip"   },   "log...

---
