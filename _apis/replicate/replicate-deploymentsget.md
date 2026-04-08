---
aid: replicate:replicate-deploymentsget
name: Replicate Get a deployment
tags:
- Deployments
- Name
- Owner
humanURL: 
properties: []
description: >-
  Get information about a deployment by name including the current release.  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/deployments/replicate/my-app-image-generator ```  The response will be a JSON object describing the deployment:  ```json {   "owner": "acme",   "name": "my-app-image-generator",   "current_release": {     "number": 1,     "model": "stability-ai/sdxl",     "version": "da77bc59ee60423279fd632efb4...

---
