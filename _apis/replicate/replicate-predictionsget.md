---
aid: replicate:replicate-predictionsget
name: Replicate Get a prediction
tags:
- Predictions
humanURL: 
properties: []
description: >-
  Get the current state of a prediction.  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/predictions/gm3qorzdhgbfurvjtvhg6dckhu ```  The response will be the prediction object:  ```json {   "id": "gm3qorzdhgbfurvjtvhg6dckhu",   "model": "replicate/hello-world",   "version": "5c7d5dc6dd8bf75c1acaa8565735e7986bc5b66206b55cca93cb72c9bf15ccaa",   "input": {     "text": "Alice"   },   "logs": "",   "output": "hello Alice...

---
