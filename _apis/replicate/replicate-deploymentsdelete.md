---
aid: replicate:replicate-deploymentsdelete
name: Replicate Delete a deployment
tags:
- Deployments
- Name
- Owner
humanURL: 
properties: []
description: >-
  Delete a deployment  Deployment deletion has some restrictions:  - You can only delete deployments that have been offline and unused for at least 15 minutes.  Example cURL request:  ```command curl -s -X DELETE \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/deployments/acme/my-app-image-generator ```  The response will be an empty 204, indicating the deployment has been deleted.

---
