---
aid: replicate:replicate-deploymentslist
name: Replicate List deployments
tags:
- Deployments
humanURL: 
properties: []
description: >-
  Get a list of deployments associated with the current account, including the latest release configuration for each deployment.  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/deployments ```  The response will be a paginated JSON array of deployment objects, sorted with the most recent deployment first:  ```json {   "next": "http://api.replicate.com/v1/deployments?cursor=cD0yMDIzLTA2LTA2KzIzJTNBNDAlM0EwOC45NjMwMDA...

---
