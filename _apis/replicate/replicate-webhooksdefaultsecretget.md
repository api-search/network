---
aid: replicate:replicate-webhooksdefaultsecretget
name: Replicate Get the signing secret for the default webhook
tags:
- Secrets
- Webhooks
humanURL: 
properties: []
description: >-
  Get the signing secret for the default webhook endpoint. This is used to verify that webhook requests are coming from Replicate.  Example cURL request:  ```console curl -s \   -H "Authorization: Bearer $REPLICATE_API_TOKEN" \   https://api.replicate.com/v1/webhooks/default/secret ```  The response will be a JSON object with a `key` property:  ```json {   "key": "..." } ```

---
