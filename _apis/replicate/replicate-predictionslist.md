---
aid: replicate:replicate-predictionslist
name: Replicate List predictions
tags:
- Predictions
humanURL: 
properties: []
description: >-
  Get a paginated list of all predictions created by the user or organization associated with the provided API token.  This will include predictions created from the API and the website. It will return 100 records per page.  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/predictions ```  The response will be a paginated JSON array of prediction objects, sorted with the most recent prediction first:  ```json {   "nex...

---
