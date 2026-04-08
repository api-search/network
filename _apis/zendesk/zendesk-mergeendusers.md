---
aid: zendesk:zendesk-mergeendusers
name: Zendesk Put  Api V2 Users User_id Merge
tags:
- Users
humanURL: 
properties: []
description: >-
  Merges the end user specified in the path parameter into the existing end user specified in the request body.  Any two end users can be merged with the exception of end users created by sharing agreements.  To be eligible for merging, the user in the path parameter must be a requester on 10,000 or fewer tickets. Otherwise, the merge will be blocked.  Agents, admins, and users with more than 10,000 requested tickets cannot be merged.  For more information about how user data is merged, see [Me...

---
