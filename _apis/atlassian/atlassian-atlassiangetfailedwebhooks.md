---
aid: atlassian:atlassian-atlassiangetfailedwebhooks
name: Get Failed Webhooks
tags:
- Webhooks
humanURL: 
properties: []
description: >-
  Returns webhooks that have recently failed to be delivered to the requesting app after the maximum number of retries.<br><br>After 72 hours the failure may no longer be returned by this operation.<br><br>The oldest failure is returned first.<br><br>This method uses a cursor-based pagination. To request the next page use the failure time of the last webhook on the list as the `failedAfter` value or use the URL provided in `next`.<br><br>**[Permissions](#permissions) required:** Only [Connect a...

---
