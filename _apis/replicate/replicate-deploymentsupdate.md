---
aid: replicate:replicate-deploymentsupdate
name: Replicate Update a deployment
tags:
- Deployments
- Name
- Owner
humanURL: 
properties: []
description: >-
  Update properties of an existing deployment, including hardware, min/max instances, and the deployment's underlying model [version](https://replicate.com/docs/how-does-replicate-work#versions).  Example cURL request:  ```console curl -s \   -X PATCH \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   -H "Content-Type: application/json" \   -d '{"min_instances": 3, "max_instances": 10}' \   https://api.replicate.com/v1/deployments/acme/my-app-image-generator ```  The response will be a JSO...

---
