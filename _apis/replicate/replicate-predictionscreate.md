---
aid: replicate:replicate-predictionscreate
name: Replicate Create a prediction
tags:
- Predictions
humanURL: 
properties: []
description: >-
  Create a prediction for the model version and inputs you provide.  Example cURL request:  ```console curl -s -X POST -H 'Prefer: wait' \   -d '{"version": "5c7d5dc6dd8bf75c1acaa8565735e7986bc5b66206b55cca93cb72c9bf15ccaa", "input": {"text": "Alice"}}' \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   -H 'Content-Type: application/json' \   https://api.replicate.com/v1/predictions ```  The request will wait up to 60 seconds for the model to run. If this time is exceeded the prediction wi...

---
