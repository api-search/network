---
aid: replicate:replicate-deploymentscreate
name: Replicate Create a deployment
tags:
- Deployments
humanURL: 
properties: []
description: >-
  Create a new deployment:  Example cURL request:  ```console curl -s \   -X POST \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   -H "Content-Type: application/json" \   -d '{         "name": "my-app-image-generator",         "model": "stability-ai/sdxl",         "version": "da77bc59ee60423279fd632efb4795ab731d9e3ca9705ef3341091fb989b7eaf",         "hardware": "gpu-t4",         "min_instances": 0,         "max_instances": 3       }' \   https://api.replicate.com/v1/deployments ```  The ...

---
