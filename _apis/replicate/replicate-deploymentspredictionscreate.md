---
aid: replicate:replicate-deploymentspredictionscreate
name: Replicate Create a prediction using a deployment
tags:
- Deployments
- Name
- Owner
- Predictions
humanURL: 
properties: []
description: >-
  Create a prediction for the deployment and inputs you provide.  Example cURL request:  ```console curl -s -X POST -H 'Prefer: wait' \   -d '{"input": {"prompt": "A photo of a bear riding a bicycle over the moon"}}' \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   -H 'Content-Type: application/json' \   https://api.replicate.com/v1/deployments/acme/my-app-image-generator/predictions ```  The request will wait up to 60 seconds for the model to run. If this time is exceeded the prediction...

---
