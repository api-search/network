---
aid: replicate:replicate-trainingslist
name: Replicate List trainings
tags:
- Trainings
humanURL: 
properties: []
description: >-
  Get a paginated list of all trainings created by the user or organization associated with the provided API token.  This will include trainings created from the API and the website. It will return 100 records per page.  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/trainings ```  The response will be a paginated JSON array of training objects, sorted with the most recent training first:  ```json {   "next": null, ...

---
