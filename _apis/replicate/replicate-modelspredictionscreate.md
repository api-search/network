---
aid: replicate:replicate-modelspredictionscreate
name: Replicate Create a prediction using an official model
tags:
- Model
- Name
- Owner
- Predictions
humanURL: 
properties: []
description: >-
  Create a prediction for the deployment and inputs you provide.  Example cURL request:  ```console curl -s -X POST -H 'Prefer: wait' \   -d '{"input": {"prompt": "Write a short poem about the weather."}}' \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   -H 'Content-Type: application/json' \   https://api.replicate.com/v1/models/meta/meta-llama-3-70b-instruct/predictions ```  The request will wait up to 60 seconds for the model to run. If this time is exceeded the prediction will be retu...

---
